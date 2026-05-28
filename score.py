def calculate_score(found_skills):

    score = len(found_skills) * 10

    if score > 100:
        score = 100

    return score