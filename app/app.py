import logging
from flask import Flask, request, render_template, jsonify
from datetime import date
from Models import db
from data_service import get_all_data, calculate_experience
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "database", "data.db")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Routes start here
@app.route("/")
def index():
    try:
        # 1. Bring the data
        context = get_all_data()
        projects = context["projects"]
        technologies = context["technologies"]
        projects_technologies = context["projects_technologies"]

        # 2. Badge limit
        display_limit = 2

        # 3. Tech list for each project
        for project in projects:
            # 3.1. IDs for used techs in this project
            tech_ids = [
                project_technology["technology_id"]
                for project_technology in projects_technologies
                if project_technology["project_id"] == project["id"]
            ]
            # 3.2. Filtered tech
            project["techs"] = [
                tech for tech in technologies
                if tech["id"] in tech_ids
            ]

        # 4. Insert processed data into context
        context["projects"] = projects
        context["display_limit"] = display_limit

        # 5. Calculate experience and other variables
        start_date = date(2024, 9, 1)
        experience = calculate_experience(start_date)
        context.update({"experience": experience, "current_date": date.today()})
        return render_template("index.html", **context), 200
    except Exception as e:
        logger.error(f"[SERVER]: Error retrieving data")
        return render_template("index.html", context=(jsonify({"error": "Error retrieving data"}))), 500
    

if __name__ == "__main__":
    app.run(debug=True, port=4000)