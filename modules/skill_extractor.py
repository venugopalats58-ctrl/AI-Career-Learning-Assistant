import re


# Skills that our system can recognize
SKILLS = {
    "Python": ["python"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "TensorFlow": ["tensorflow"],
    "Keras": ["keras"],
    "PyTorch": ["pytorch"],
    "Machine Learning": ["machine learning", "machine-learning"],
    "Deep Learning": ["deep learning", "deep-learning"],
    "Artificial Intelligence": [
        "artificial intelligence",
        "ai"
    ],
    "NLP": [
        "nlp",
        "natural language processing"
    ],
    "Generative AI": [
        "generative ai",
        "genai"
    ],
    "LLM": [
        "llm",
        "large language model"
    ],
    "RAG": [
        "rag",
        "retrieval augmented generation"
    ],
    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql"],
    "MongoDB": ["mongodb"],
    "HTML": ["html"],
    "CSS": ["css"],
    "JavaScript": ["javascript"],
    "React": ["react", "reactjs"],
    "Bootstrap": ["bootstrap"],
    "Java": ["java"],
    "C": ["c programming"],
    "R": ["r programming"],
    "Git": ["git"],
    "GitHub": ["github"],
    "Streamlit": ["streamlit"],
    "Flask": ["flask"],
    "Django": ["django"],
    "Docker": ["docker"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure"],
    "Power BI": ["power bi"],
    "Tableau": ["tableau"]
}


def extract_skills(text):
    """
    Extract known skills from resume text.
    """

    text_lower = text.lower()

    detected_skills = []

    for skill, keywords in SKILLS.items():

        for keyword in keywords:

            pattern = r"\b" + re.escape(keyword.lower()) + r"\b"

            if re.search(pattern, text_lower):

                detected_skills.append(skill)

                break

    return detected_skills