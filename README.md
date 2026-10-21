# 🎓 AI Study Assistant

An AI-powered study assistant built with Python and Google's Gemini API to help students learn topics, prepare notes, practice questions, and understand code.

## ✨ Features

- 💬 **AI Chat** — Ask questions and receive AI-generated answers.
- 📚 **Topic Explanation** — Learn topics in simple, beginner-friendly language.
- 📝 **Study Notes** — Generate organized notes with headings, definitions, examples, and exam tips.
- ❓ **Quiz Generator** — Create multiple-choice questions with answers and explanations.
- 🎯 **Important Questions** — Generate short-answer, long-answer, and exam-focused questions.
- 📄 **Text Summarizer** — Extract summaries, main points, keywords, and facts.
- 💻 **Code Explainer** — Understand code and identify possible errors.
- 🧮 **Problem Solver** — Get step-by-step solutions.
- 🔄 **Retry Handling** — Retry certain temporary Gemini service errors.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google Gen AI Python SDK

## 📁 Project Structure

```text
ai_study_assistant/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Install Python

Install a compatible Python version if you haven't already.

### 2. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-study-assistant.git
cd ai-study-assistant
```

Replace `YOUR_GITHUB_USERNAME` with your GitHub username.

### 3. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Configure your Gemini API key

Create a `.env` file only if you also install and configure a package that loads it, or set the environment variable directly in PowerShell:

```powershell
$env:GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own API key. Never publish your real key or commit it to GitHub.

### 6. Run the application

```powershell
python main.py
```

Follow the numbered menu in the terminal to select a study feature.

## 🔐 Security

- Keep API keys private.
- Do not upload `.env` files or other secret credentials.
- Use `.gitignore` to exclude virtual environments and Python cache files.

## 👩‍💻 Author

**Chintha Chethana Sai Sree**

GitHub: [@chethansree77](https://github.com/chethansree77)
