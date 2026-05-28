import streamlit as st
from analyzer import extract_text
from skills import check_skills
from score import calculate_score

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf"])

if uploaded_file is not None:

    # Extract text from PDF
    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Text")
    st.write(resume_text)

    # Skill Detection
    found_skills = check_skills(resume_text)

    st.subheader("Skills Detected")

    for skill in found_skills:
        st.success(skill)

    # Resume Score
    score = calculate_score(found_skills)

    st.subheader("Resume Score")
    st.info(f"{score}/100")

    # Suggestions
    st.subheader("Suggestions")

    if score < 50:
        st.warning("Add more technical skills and projects.")
    elif score < 80:
        st.warning("Add certifications and improve resume format.")
    else:
        st.success("Excellent Resume!")