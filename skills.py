import re

def check_skills(resume_text):

    skills = [
        "Python",
        "Java",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Machine Learning",
        "Communication",
        "C",
        "C++"
    ]

    found_skills = []

    for skill in skills:

        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, resume_text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills