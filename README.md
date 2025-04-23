# 📄 PDF Chatbot

An AI-powered chatbot that can read and interact with the contents of PDF documents using the Mistral model via [Ollama](https://ollama.com). Choose between a modern Streamlit UI or a terminal-based chatbot experience.

---

## 🚀 Features

- Chat with any PDF document
- Powered by Mistral via Ollama
- Choose between terminal or Streamlit UI
- Lightweight and local setup

---

## 🛠️ Installation & Setup

Follow the steps below to get started with the project.

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

---

### 2. Create and Activate a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure `requirements.txt` includes necessary libraries like:

```txt
streamlit
PyPDF2
langchain
openai
```

---

### 4. Download & Install Ollama

Follow the instructions on the official [Ollama installation page](https://ollama.com/download) for your operating system.

---

### 5. Run Mistral Model via Ollama

Once Ollama is installed, open a new terminal and run:

```bash
ollama run mistral
```

This will pull the Mistral model if it’s not already downloaded and start it.

---

### 6. Navigate Back to the Project Directory

Make sure your virtual environment is still active.

---

### 7. Run the Chatbot

You can choose to run the chatbot in:

#### Option A: Streamlit App

```bash
streamlit run app.py
```

#### Option B: Terminal Mode

```bash
python chatbot_terminal.py
```

---

## 📁 Project Structure

```
pdf-chatbot/
├── app.py                 # Streamlit interface
├── chatbot_core.py        # Contains the core logic of the chatbot    
├── chatbot_terminal.py    # Terminal-based interface
├── utils/                 # Utility functions (PDF parser, etc.)
├── requirements.txt
└── README.md
```

---

## ✅ Notes

- Make sure Ollama is running **before** using the chatbot.
- You can edit `app.py` or `chatbot_terminal.py` to customize the prompt behavior or add PDF upload features.

---

## 🧠 Powered By

- [Mistral](https://mistral.ai) (via Ollama)
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://faiss.ai/index.html)