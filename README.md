# InkRidden-AI utility tool for Text Summarization and Keyword extraction

## Overview

**InkRidden** is a simple AI-powered utility that allows users to extract keywords or generate summaries from plain text or uploaded documents. The app leverages **LLaMA 3** via **Ollama** to provide smart language processing, all wrapped in a clean **Streamlit UI**.

---

## Features

- ✂️ **Keyword Extraction**: Identifies key concepts from your input.
- 🧠 **Text Summarization**: Condenses large chunks of text into a brief summary.
- 📁 **Multi-Format Support**: Accepts `.txt`, `.pdf`, and `.docx` files for processing.
- 🖥️ **User-Friendly Interface**: Toggle between tasks and input types with ease.

---

## How It Works

1. **User chooses a task** (Keyword Extraction or Summarization).
2. **Input is provided** via direct text or document upload.
3. Input text is converted into a **prompt** and sent to **LLaMA 3 via Ollama**.
4. The model returns **keywords** or a **3-line summary** as output.

---

## Tech Stack

| Component       | Technology              |
|----------------|--------------------------|
| Frontend       | Streamlit                |
| Backend Model  | LLaMA 3 via Ollama       |
| File Parsing   | PyMuPDF, python-docx     |

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inkridden.git
   cd inkridden
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate     # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run LLaMA 3 in the background:
   ```bash
   ollama run llama3
   ```

5. Launch the app:
   ```bash
   streamlit run main.py
   ```

---

## Sample Use Cases

- 📚 Students summarizing research papers.
- 🌿 Herbalists extracting plant-based knowledge.
- 📝 Writers gathering key ideas from long content.

---

## Future Enhancements

- 🔍 Add Named Entity Recognition (NER)
- 🌐 Add support for web URLs
- 💾 Option to export outputs

---

## Contact

Got suggestions or questions?  
📧 **v.ukrishnan8@gmail.com**

--- 
## Screenshots

![image](https://github.com/user-attachments/assets/6b56fce8-6297-4f5b-8176-c1e913ff7128)

![image](https://github.com/user-attachments/assets/828eb720-9334-480e-821b-830d5195662c)

![image](https://github.com/user-attachments/assets/cad40f2a-b042-40a9-b83b-c85da80703ec)


