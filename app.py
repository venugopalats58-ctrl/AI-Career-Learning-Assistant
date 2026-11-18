import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from modules.resume_parser import extract_resume_text
from modules.skill_extractor import extract_skills
from modules.skill_gap import calculate_skill_gap
from modules.roadmap import generate_roadmap
from modules.project_recommender import recommend_projects
from rag.answer_generator import generate_answer
import os

from rag.document_loader import load_document
from rag.text_splitter import split_text
from rag.embeddings import create_embeddings
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_documents
from modules.interview import generate_interview_question



# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Career & Learning Assistant",
    page_icon="🚀",
    layout="wide"
)

# Store detected resume skills
if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []

if "rag_chunks" not in st.session_state:
    st.session_state.rag_chunks = []

if "rag_vector_store" not in st.session_state:
    st.session_state.rag_vector_store = None

# ==========================================
# HEADER
# ==========================================

st.title("🚀 AI Career & Learning Assistant")

st.write(
    "An intelligent platform for career planning, "
    "skill-gap analysis, personalized learning and interview preparation."
)

st.divider()

page = st.sidebar.selectbox(
    "Choose a module",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "💼 Career Matcher",
        "🗺️ Learning Roadmap",
        "💡 Project Recommendations",
        "📚 RAG Learning Assistant",
        "🎤 AI Interview"
    ],
    index=0
)

# ==========================================
# DASHBOARD
# ==========================================

if page == "🏠 Dashboard":

    st.header("Welcome 👋")

    st.write(
        "Your AI-powered career companion. "
        "Analyze your resume, identify missing skills, "
        "create a learning roadmap and prepare for interviews."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Skills Detected", "0")

    with col2:
        st.metric("Career Readiness", "0%")

    with col3:
        st.metric("Recommended Projects", "0")

    with col4:
        st.metric("Learning Progress", "0%")

    st.divider()

    st.subheader("✨ Application Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
            📄 **Resume Analyzer**

            Upload your resume and extract
            skills, education and experience.
            """
        )

        st.success(
            """
            💼 **Career Matcher**

            Compare your skills with
            job-role requirements.
            """
        )

        st.warning(
            """
            📊 **Skill Gap Analysis**

            Find the skills you need to learn
            for your target career.
            """
        )

    with col2:

        st.info(
            """
            🗺️ **Learning Roadmap**

            Get a personalized step-by-step
            learning path.
            """
        )

        st.success(
            """
            📚 **RAG Learning Assistant**

            Ask questions from your
            uploaded study materials.
            """
        )

        st.warning(
            """
            🎤 **AI Interview**

            Practice technical interviews
            and receive feedback.
            """
        )


# ==========================================
# RESUME ANALYZER
# ==========================================

elif page == "📄 Resume Analyzer":

    st.header("📄 Resume Analyzer")

    st.write(
        "Upload your resume and extract the text automatically."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success(
            f"✅ {uploaded_file.name} uploaded successfully!"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "File Size",
                f"{uploaded_file.size / 1024:.2f} KB"
            )

        with col2:
            st.metric(
                "File Type",
                uploaded_file.name.split(".")[-1].upper()
            )

        with col3:
            st.metric(
                "Status",
                "Uploaded"
            )

        st.divider()

        # ------------------------------------------
        # Extract Resume Text
        # ------------------------------------------

        try:

            resume_text = extract_resume_text(uploaded_file)

            if resume_text.strip():

                st.success(
                    "✅ Resume text extracted successfully!"
                )

                word_count = len(resume_text.split())
                character_count = len(resume_text)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Word Count",
                        word_count
                    )

                with col2:
                    st.metric(
                        "Character Count",
                        character_count
                    )

                st.subheader("📄 Extracted Resume Text")

                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=400
                )

                # ------------------------------------------
                # Skill Extraction
                # ------------------------------------------

                st.divider()

                st.subheader("🧠 Detected Skills")

                detected_skills = extract_skills(resume_text)
                st.session_state.resume_skills = detected_skills

                if detected_skills:

                    st.success(
                        f"Found {len(detected_skills)} skills in your resume."
                    )

                    columns = st.columns(3)

                    for index, skill in enumerate(detected_skills):

                        with columns[index % 3]:
                            st.write(f"✅ **{skill}**")

                else:

                    st.warning(
                        "No recognized skills were found in the resume."
                    )

            else:

                st.warning(
                    "⚠️ No text could be extracted from this resume."
                )

                st.info(
                    "If this is a scanned PDF, OCR support "
                    "can be added later."
                )

        except Exception as e:

            st.error(
                f"❌ Error while reading resume: {e}"
            )
# ==========================================
# CAREER MATCHER
# ==========================================

elif page == "💼 Career Matcher":

    st.header("💼 Career Matcher")

    st.write(
        "Compare your skills with the requirements "
        "of your target career."
    )

    target_role = st.selectbox(
        "🎯 Select Target Career",
        [
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Analyst",
            "Python Developer",
            "Web Developer"
        ]
    )

    st.divider()

    st.subheader("🧠 Enter Your Skills")

    skills_input = st.text_input(
        "Enter your skills separated by commas",
        placeholder="Python, Pandas, NumPy, SQL, Machine Learning"
    )

    if skills_input:

        user_skills = [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ]

        matched_skills, missing_skills, readiness = calculate_skill_gap(
            user_skills,
            target_role
        )

        st.divider()

        st.subheader("🎯 Career Readiness")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Target Role",
                target_role
            )

        with col2:
            st.metric(
                "Skills You Have",
                len(matched_skills)
            )

        with col3:
            st.metric(
                "Career Readiness",
                f"{readiness:.1f}%"
            )

        st.divider()

        st.subheader("✅ Skills You Have")

        if matched_skills:

            for skill in matched_skills:
                st.write(f"✅ **{skill}**")

        else:

            st.warning(
                "No matching skills found."
            )

        st.divider()

        st.subheader("❌ Skills You Need to Learn")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"❌ **{skill}**")

        else:

            st.success(
                "🎉 You have all the required skills!"
            )

# ==========================================
# PERSONALIZED LEARNING ROADMAP
# ==========================================

elif page == "🗺️ Learning Roadmap":

    st.header("🗺️ Personalized Learning Roadmap")

    st.write(
        "Create a learning path based on the skills "
        "you need for your target career."
    )

    target_role = st.selectbox(
        "🎯 Select Target Career",
        [
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Analyst",
            "Python Developer",
            "Web Developer"
        ]
    )

    st.divider()

    st.subheader("🧠 Enter Your Current Skills")

    skills_input = st.text_input(
        "Enter your skills separated by commas",
        placeholder="Python, Pandas, NumPy, SQL"
    )

    if skills_input:

        user_skills = [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ]

        matched_skills, missing_skills, readiness = calculate_skill_gap(
            user_skills,
            target_role
        )

        st.subheader("📊 Career Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Target Career",
                target_role
            )

        with col2:
            st.metric(
                "Missing Skills",
                len(missing_skills)
            )

        with col3:
            st.metric(
                "Career Readiness",
                f"{readiness:.1f}%"
            )

        st.divider()

        if missing_skills:

            st.subheader("🗺️ Your Personalized Roadmap")

            roadmap = generate_roadmap(missing_skills)

            for index, item in enumerate(roadmap, start=1):

                with st.expander(
                    f"Step {index}: {item['skill']} — {item['level']}"
                ):

                    st.write(
                        f"### 📚 Learn {item['skill']}"
                    )

                    st.write(
                        f"**Level:** {item['level']}"
                    )

                    st.write("**Topics to learn:**")

                    for topic in item["topics"]:
                        st.write(f"• {topic}")

                    st.info(
                        f"🎯 Practice {item['skill']} "
                        "by building a small project."
                    )

        else:

            st.success(
                "🎉 You already have all the required skills "
                "for this career!"
            )

# ==========================================
# PROJECT RECOMMENDATIONS
# ==========================================

elif page == "💡 Project Recommendations":

    st.header("💡 AI Project Recommendations")

    st.write(
        "Get project ideas based on your target career "
        "and current skills."
    )

    # ------------------------------------------
    # TARGET CAREER
    # ------------------------------------------

    target_role = st.selectbox(
        "🎯 Select Target Career",
        [
            "Data Scientist",
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Analyst",
            "Python Developer",
            "Web Developer"
        ]
    )

    st.divider()

    # ------------------------------------------
    # RESUME SKILLS
    # ------------------------------------------

    st.subheader("🧠 Your Current Skills")

    resume_skills = st.session_state.get(
        "resume_skills",
        []
    )

    if resume_skills:

        st.success(
            f"Using {len(resume_skills)} skills detected "
            "from your resume."
        )

        st.write("### 🧠 Detected Resume Skills")

        for skill in resume_skills:
            st.write(f"✅ {skill}")

        user_skills = resume_skills

    else:

        st.info(
            "No resume skills detected. "
            "Enter your skills manually."
        )

        skills_input = st.text_input(
            "Enter your skills separated by commas",
            placeholder="Python, Pandas, NumPy, SQL"
        )

        if skills_input:

            user_skills = [
                skill.strip()
                for skill in skills_input.split(",")
                if skill.strip()
            ]

        else:

            user_skills = []

    # ------------------------------------------
    # PROJECT RECOMMENDATION
    # ------------------------------------------

    if user_skills:

        projects = recommend_projects(
            user_skills,
            target_role
        )

        st.divider()

        st.subheader("💡 Recommended Projects")

        if projects:

            for index, project in enumerate(
                projects[:5],
                start=1
            ):

                with st.expander(
                    f"{index}. {project['name']} — "
                    f"{project['level']}"
                ):

                    st.write(
                        f"### 🚀 {project['name']}"
                    )

                    st.write(
                        f"**Difficulty:** "
                        f"{project['level']}"
                    )

                    st.write(
                        f"**Skill Match:** "
                        f"{project['match']:.1f}%"
                    )

                    st.write(
                        f"**Description:** "
                        f"{project['description']}"
                    )

                    st.write(
                        "**Skills required:**"
                    )

                    user_skill_set = {
                        skill.lower()
                        for skill in user_skills
                    }

                    for skill in project["skills"]:

                        if skill.lower() in user_skill_set:

                            st.write(
                                f"✅ {skill}"
                            )

                        else:

                            st.write(
                                f"📚 {skill}"
                            )

        else:

            st.warning(
                "No projects found for this career."
            )

# ==========================================
# RAG LEARNING ASSISTANT
# ==========================================

elif page == "📚 RAG Learning Assistant":

    st.header("📚 RAG Learning Assistant")

    st.write(
        "Upload your study materials and ask questions "
        "based on the content of your documents."
    )

    st.divider()

    # ------------------------------------------
    # UPLOAD STUDY MATERIALS
    # ------------------------------------------

    st.subheader("📄 Upload Study Materials")

    documents = st.file_uploader(
        "Upload PDF, TXT or DOCX files",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True,
        key="rag_file_uploader"
    )

    # Process documents only when button is clicked
    if st.button("🚀 Process Documents", key="process_rag"):

        if not documents:

            st.warning("Please upload at least one document.")

        else:

            all_chunks = []

            os.makedirs(
                "documents/study_materials",
                exist_ok=True
            )

            with st.spinner("Processing your documents..."):

                for document in documents:

                    try:

                        # Save uploaded document
                        file_path = os.path.join(
                            "documents",
                            "study_materials",
                            document.name
                        )

                        with open(file_path, "wb") as file:
                            file.write(document.getbuffer())

                        # Extract document text
                        text = load_document(file_path)

                        if not text or not text.strip():

                            st.warning(
                                f"No text found in {document.name}"
                            )
                            continue

                        # Split document into chunks
                        chunks = split_text(text)

                        all_chunks.extend(chunks)

                        st.success(
                            f"{document.name}: "
                            f"{len(chunks)} chunks created"
                        )

                    except Exception as e:

                        st.error(
                            f"Error processing {document.name}: {e}"
                        )

                # Create embeddings and vector store
                if all_chunks:

                    try:

                        with st.spinner("Creating embeddings..."):

                            embeddings = create_embeddings(all_chunks)

                        with st.spinner("Creating vector database..."):

                            vector_store = create_vector_store(embeddings)

                        # Store processed data
                        st.session_state.rag_chunks = all_chunks

                        st.session_state.rag_vector_store = vector_store

                        st.success(
                            f"Knowledge base created successfully! "
                            f"{len(all_chunks)} chunks are ready."
                        )

                    except Exception as e:

                        st.session_state.rag_chunks = []
                        st.session_state.rag_vector_store = None

                        st.error(f"Error creating knowledge base: {e}")

                else:

                    st.warning(
                        "No valid text was extracted from the uploaded documents."
                    )

    # ------------------------------------------
    # KNOWLEDGE BASE STATUS
    # ------------------------------------------

    st.divider()

    st.subheader("📊 Knowledge Base Status")

    current_chunks = st.session_state.rag_chunks

    if current_chunks:

        st.success(
            f"Knowledge base ready: {len(current_chunks)} chunks"
        )

    else:

        st.info("No documents processed yet.")

    # Clear knowledge base
    if st.button("🗑️ Clear Knowledge Base"):

        st.session_state.rag_chunks = []
        st.session_state.rag_vector_store = None

        st.success("Knowledge base cleared successfully.")

        st.rerun()

    # ------------------------------------------
    # ASK QUESTIONS
    # ------------------------------------------

    st.divider()

    st.subheader("❓ Ask Your Question")

    question = st.text_input(
        "Ask something about your study materials",
        placeholder="What is normalization?",
        key="rag_question"
    )

    if st.button("🤖 Generate Answer"):

        vector_store = st.session_state.rag_vector_store

        chunks = st.session_state.rag_chunks

        if not chunks or vector_store is None:

            st.warning(
                "Please upload and process study materials first."
            )

        elif not question.strip():

            st.warning("Please enter a question.")

        else:

            try:

                with st.spinner("Searching study materials..."):

                    results = retrieve_documents(
                        question,
                        vector_store,
                        chunks,
                        top_k=3
                    )

                if not results:

                    st.warning(
                        "No relevant information found in your documents."
                    )

                else:

                    with st.spinner("Qwen AI is generating your answer..."):

                        answer = generate_answer(
                            question,
                            results
                        )

                    st.divider()

                    st.subheader("🤖 AI Answer")

                    st.write(answer)

                    st.divider()

                    st.subheader("🔎 Relevant Study Content")

                    for index, result in enumerate(results, start=1):

                        with st.expander(f"📚 Result {index}"):

                            st.write(result["text"])

                            st.caption(
                                f"Similarity score: {result['score']:.4f}"
                            )

            except Exception as e:

                st.error(f"Error generating answer: {e}")

    # ------------------------------------------
    # Ask Question
    # ------------------------------------------

    st.subheader("❓ Ask Your Question")

    question = st.text_input(
        "Ask something about your study materials",
        placeholder="What is normalization?"
    )

    if question:

        vector_store = (
            st.session_state.rag_vector_store
        )

        chunks = (
            st.session_state.rag_chunks
        )

        if vector_store is None or not chunks:

            st.warning(
                "⚠️ Please upload study materials "
                "before asking a question."
            )

        else:

            with st.spinner(
                "Searching your study materials..."
            ):

                results = retrieve_documents(
                    question,
                    vector_store,
                    chunks,
                    top_k=3
                )
            answer = generate_answer(
               question,
               results
            )

            st.divider()

            st.subheader("🤖 AI Answer")

            st.write(answer)

            st.divider()

            st.subheader(
                "🔎 Relevant Study Content"
            )

            if results:

                for index, result in enumerate(
                    results,
                    start=1
                ):

                    with st.expander(
                        f"📚 Result {index}"
                    ):

                        st.write(
                            result["text"]
                        )

                        st.caption(
                            f"Similarity score: "
                            f"{result['score']:.4f}"
                        )

            else:

                st.warning(
                    "No relevant information found "
                    "in your study materials."
                )



# ==========================================
# AI INTERVIEW
# ==========================================

elif page == "🎤 AI Interview":

    st.header("🎤 AI Interview Assistant")

    st.write("Practice technical interviews using local Qwen AI.")

    role = st.selectbox(
        "Select Job Role",
        [
            "Machine Learning Engineer",
            "AI Engineer",
            "Data Scientist",
            "Data Analyst",
            "Python Developer"
        ]
    )

    difficulty = st.selectbox(
        "Select Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    if "interview_question" not in st.session_state:
        st.session_state.interview_question = ""

    if st.button("Generate Interview Question"):

        with st.spinner("Qwen AI is generating your question..."):

            question = generate_interview_question(
                role,
                difficulty
            )

            st.session_state.interview_question = question

    if st.session_state.interview_question:

        st.subheader("🎯 Interview Question")

        st.write(st.session_state.interview_question)

        if st.button("Generate Next Question"):

            with st.spinner("Generating next question..."):

                question = generate_interview_question(
                    role,
                    difficulty
                )

                st.session_state.interview_question = question

            st.rerun()
