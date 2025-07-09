# 🎤 AI-Powered Interview Coach (LLM-Agnostic Version)

A web app that evaluates your job interview answers using **any AI Language Model API**, such as OpenAI, Anthropic Claude, Cohere, or Hugging Face. Tailor the model to your needs via a `.env` file.

---

## 🚀 Features

- 🤖 Works with **any LLM provider** (OpenAI, Claude, Cohere, etc.)
- 💼 Role-specific questions (Dev, PM, Analyst, Designer)
- 📚 Real-time feedback: relevance, grammar, confidence
- 🧠 Flesch Reading Ease readability score
- 🛠 Simple setup using Streamlit and REST

---

## 🧱 Tech Stack

- Python 3.9+
- Streamlit for UI
- `requests` for API integration
- `textstat` for readability metrics
- `.env` config for portable API usage

---

## ⚙️ Configuration

### `.env` File
Create a `.env` file in your project root:
```env
LLM_API_KEY=your-api-key-here
LLM_API_URL=https://api.openai.com/v1/chat/completions   # Replace with your LLM endpoint
