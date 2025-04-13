import subprocess
import streamlit as st
import fitz  # PyMuPDF
import docx

# --- Prompt Builders ---
def build_keyword_prompt(text):
    return f"""
You are an expert language model helping to extract relevant keywords from text.

Instructions:
- Extract only meaningful, non-generic keywords.
- Return them in a comma-separated list.
- Do NOT include explanations.

Text:
\"\"\"{text.strip()}\"\"\"

Output only the keywords:
"""

def build_summary_prompt(text):
    return f"""
You are an expert summarizer.

Instructions:
- Summarize the given text in 3 short, clear lines.
- Avoid unnecessary repetition or generic statements.

Text:
\"\"\"{text.strip()}\"\"\"

Output:
"""

# --- Text Extractor ---
def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif file.name.endswith(".docx"):
        docx_file = docx.Document(file)
        return "\n".join([para.text for para in docx_file.paragraphs])
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return None

# --- LLaMA Call ---
def query_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.2", prompt],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    return result.stdout.strip()

# --- Streamlit UI ---
st.set_page_config(page_title="InkRidden - AI Utility", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🧠 InkRidden: AI Utility Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Effortlessly extract <b>keywords</b> or generate concise <b>summaries</b> from your content.</p>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar - task selection
st.sidebar.markdown("## ⚙️ Task Options")
task = st.sidebar.radio("Choose a Task", ["🔑 Keyword Extraction", "📝 Text Summarization"])

# Input method
st.markdown("### ✍️ Select Input Method")
input_method = st.radio("", ["Paste Text", "Upload File"])

text = ""

if input_method == "Paste Text":
    user_input = st.text_area("📋 Enter your text below", height=200, placeholder="Paste any paragraph or passage here...")
    if user_input.strip():
        text = user_input.strip()

else:
    uploaded_file = st.file_uploader("📁 Upload a document (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
    if uploaded_file:
        text = extract_text(uploaded_file)
        if not text:
            st.error("⚠️ Could not extract text. Please try a valid document.")

# Run button
if st.button("🚀 Run"):
    if not text:
        st.error("❌ Please provide some text to proceed.")
    else:
        st.success(f"✅ Running {task.split()[1]}...")
        prompt = build_keyword_prompt(text[:2000]) if "Keyword" in task else build_summary_prompt(text[:2000])
        response = query_ollama(prompt)
        st.markdown("### ✅ Output:")
        st.info(response)
