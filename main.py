from flask import Flask, render_template

from utils import get_candidate, load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates = load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def get_candidate_by_id(candidate_id):
    candidate = get_candidate(candidate_id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidate_by_skills(skill):
    candidates = get_candidates_by_skill(skill.lower())
    return render_template("skill.html", candidates=candidates, count_candidates=len(candidates), skill=skill)


if __name__ == '__main__':
    app.run(debug=True)
