import json
import os


def load_candidates_from_json():
    with open(os.path.join("candidates.json"), encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    candidates = load_candidates_from_json()

    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate
    return "Такого кандидата нет"


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
            return result
    return "Такого кандидата нет"


def get_candidates_by_skill(skill):
    candidates = load_candidates_from_json()

    candidates_by_skills = []
    for candidate in candidates:
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            candidates_by_skills.append(candidate)
            return candidates_by_skills
    return "Такого навыка нет"

