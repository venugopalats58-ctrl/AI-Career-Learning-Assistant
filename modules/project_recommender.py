# ==========================================
# AI PROJECT RECOMMENDER
# ==========================================

PROJECTS = [

    {
        "name": "House Price Prediction",
        "career": "Data Scientist",
        "level": "Beginner",
        "skills": [
            "Python",
            "Pandas",
            "NumPy",
            "Machine Learning"
        ],
        "description": "Build a machine learning model to predict house prices."
    },

    {
        "name": "Customer Churn Prediction",
        "career": "Data Scientist",
        "level": "Intermediate",
        "skills": [
            "Python",
            "Pandas",
            "Scikit-learn",
            "Machine Learning",
            "SQL"
        ],
        "description": "Predict which customers are likely to leave a service."
    },

    {
        "name": "Sales Forecasting",
        "career": "Data Scientist",
        "level": "Intermediate",
        "skills": [
            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Machine Learning"
        ],
        "description": "Analyze historical sales data and forecast future sales."
    },

    {
        "name": "Image Classification",
        "career": "Machine Learning Engineer",
        "level": "Intermediate",
        "skills": [
            "Python",
            "TensorFlow",
            "Deep Learning",
            "CNN"
        ],
        "description": "Build a deep learning model that classifies images."
    },

    {
        "name": "AI Chatbot",
        "career": "AI Engineer",
        "level": "Intermediate",
        "skills": [
            "Python",
            "NLP",
            "LLM",
            "RAG"
        ],
        "description": "Build an AI chatbot capable of answering user questions."
    },

    {
        "name": "Resume Analyzer",
        "career": "AI Engineer",
        "level": "Advanced",
        "skills": [
            "Python",
            "NLP",
            "LLM",
            "RAG",
            "Embeddings"
        ],
        "description": "Create an AI system that analyzes resumes and extracts useful career information."
    },

    {
        "name": "Data Analytics Dashboard",
        "career": "Data Analyst",
        "level": "Beginner",
        "skills": [
            "Python",
            "Pandas",
            "SQL",
            "Power BI"
        ],
        "description": "Build an interactive dashboard for business data analysis."
    },

    {
        "name": "Portfolio Website",
        "career": "Web Developer",
        "level": "Beginner",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "description": "Create a responsive personal portfolio website."
    },

    {
        "name": "React E-Commerce Website",
        "career": "Web Developer",
        "level": "Intermediate",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React"
        ],
        "description": "Build a complete e-commerce frontend using React."
    }
]


def recommend_projects(user_skills, target_role):

    user_skills_lower = {
        skill.strip().lower()
        for skill in user_skills
    }

    recommendations = []

    for project in PROJECTS:

        # Match target career
        career_match = (
            project["career"].lower()
            == target_role.strip().lower()
        )

        if not career_match:
            continue

        project_skills = project["skills"]

        matched_count = sum(
            skill.lower() in user_skills_lower
            for skill in project_skills
        )

        total_skills = len(project_skills)

        if total_skills > 0:

            match_percentage = (
                matched_count / total_skills
            ) * 100

        else:

            match_percentage = 0

        recommendations.append({
            "name": project["name"],
            "level": project["level"],
            "skills": project["skills"],
            "description": project["description"],
            "match": match_percentage
        })

    # Highest matching projects first
    recommendations.sort(
        key=lambda x: x["match"],
        reverse=True
    )

    return recommendations