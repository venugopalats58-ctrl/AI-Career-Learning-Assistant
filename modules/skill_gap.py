import pandas as pd
import os


def load_job_roles(file_path="data/job_roles.csv"):

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Job roles file not found: {file_path}"
        )

    df = pd.read_csv(
        file_path,
        encoding="utf-8-sig"
    )

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # Clean text values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )

    return df


def calculate_skill_gap(user_skills, target_role):

    df = load_job_roles()

    # Check CSV columns
    if "job_role" not in df.columns:
        raise ValueError(
            f"'job_role' column not found. "
            f"Available columns: {list(df.columns)}"
        )

    if "required_skills" not in df.columns:
        raise ValueError(
            f"'required_skills' column not found. "
            f"Available columns: {list(df.columns)}"
        )

    # Find target role
    role_data = df[
        df["job_role"].str.strip().str.lower()
        == target_role.strip().lower()
    ]

    if role_data.empty:
        return [], [], 0

    # Required skills for selected role
    required_skills = [
        skill.strip()
        for skill in str(
            role_data.iloc[0]["required_skills"]
        ).split(",")
        if skill.strip()
    ]

    # User skills
    user_skills_lower = {
        skill.strip().lower()
        for skill in user_skills
        if skill.strip()
    }

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in user_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Career readiness
    if required_skills:
        readiness = (
            len(matched_skills)
            / len(required_skills)
        ) * 100
    else:
        readiness = 0

    return matched_skills, missing_skills, readiness