# AI Career & Learning Assistant

An AI-powered career guidance and personalized learning platform built with Python, Streamlit, and Large Language Models (LLMs). It helps users analyze their skills, identify career opportunities, discover skill gaps, and follow personalized learning roadmaps.

## 🚀 Project Overview

The AI Career & Learning Assistant helps students and aspiring developers understand their current technical skills and prepare for their desired careers.

The application combines Machine Learning, Natural Language Processing, Retrieval-Augmented Generation (RAG), and locally running LLMs to provide an interactive career-learning experience.

## ✨ Key Features

### 1. Dashboard
- Career readiness overview.
- Skill analysis and progress visualization.
- Personalized career insights.

### 2. Resume Analyzer
- Upload and analyze resumes.
- Extract relevant technical skills.
- Identify skills from resume content.

### 3. Career Matcher
- Compare existing skills with career requirements.
- Identify matched and missing skills.
- Calculate career readiness percentage.

### 4. Personalized Learning Roadmap
- Select a target career.
- Identify missing technical skills.
- Generate learning topics for each missing skill.
- Explore a structured path for skill development.

### 5. Project Recommendations
- Get project suggestions based on technical skills.
- Discover practical projects to improve development experience.

### 6. RAG Learning Assistant
- Upload PDF, DOCX, and TXT study materials.
- Extract and process document content.
- Generate text embeddings.
- Retrieve relevant information using FAISS.
- Ask questions and receive context-based answers using a local LLM.

### 7. AI Interview
- Generate technical interview questions.
- Select job roles and difficulty levels.
- Practice technical interview preparation.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Data Processing | Pandas, NumPy |
| Data Visualization | Plotly |
| Machine Learning | Scikit-learn |
| Deep Learning | PyTorch |
| Natural Language Processing | Transformers, Sentence Transformers |
| Large Language Model | Ollama – Qwen 2.5 (3B) |
| Vector Database | FAISS |
| Document Processing | PyPDF, python-docx |
| API Communication | Requests |
| Version Control | Git, GitHub |

## 📂 Project Structure

```text
AI-Career-Learning-Assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── job_roles.csv
│   ├── learning_resources.csv
│   └── skills.csv
│
├── modules/
│   ├── __init__.py
│   ├── interview.py
│   ├── project_recommender.py
│   ├── resume_parser.py
│   ├── roadmap.py
│   ├── skill_extractor.py
│   └── skill_gap.py
│
└── rag/
    ├── __init__.py
    ├── answer_generator.py
    ├── document_loader.py
    ├── embeddings.py
    ├── retriever.py
    ├── text_splitter.py
    └── vector_store.py
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/venugopalats58-ctrl/AI-Career-Learning-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Career-Learning-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install and Start Ollama

Install Ollama from:

https://ollama.com/

Download the Qwen model:

```bash
ollama pull qwen2.5:3b
```

Make sure Ollama is running before using AI-powered features.

### 6. Run the Application

```bash
streamlit run app.py
```

Open the local application in your browser:

```text
http://localhost:8501
```

## 🧠 AI Model Information

This project uses **Qwen 2.5 (3B)** through Ollama for local language model generation.

The RAG pipeline uses:

- Sentence Transformers for text embeddings.
- FAISS for similarity-based document retrieval.
- Retrieved document content as context for answer generation.

## 🎯 Project Objectives

- Provide personalized career guidance.
- Identify technical skill gaps.
- Generate career-specific learning roadmaps.
- Support document-based learning through RAG.
- Improve technical interview preparation.
- Encourage practical project-based learning.

## 🔮 Future Enhancements

- Advanced resume scoring and recommendations.
- More career paths and comprehensive skill databases.
- Learning progress tracking.
- Personalized weekly learning schedules.
- Improved AI interview evaluation.
- Cloud-based AI model integration.

## 👨‍💻 Developer

**Venugopala T S**

BCA Student | Aspiring AI & ML Engineer

GitHub: https://github.com/venugopalats58-ctrl

LinkedIn: https://linkedin.com/in/venugopala-t-s-943bb1349/

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, Machine Learning, and Generative AI.**
