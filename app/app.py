import logging
from flask import Flask, request, render_template, jsonify
from Models import db, Skills, Universities, Course_Skills, Courses, Education, Platforms, Projects, Projects_Skills, About_Me
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
        # Get data from the database
        about_me = About_Me.query.all()
        skills = Skills.query.all()
        universities = Universities.query.all()
        course_skills = Course_Skills.query.all()
        courses = Courses.query.all()
        education = Education.query.all()
        platforms = Platforms.query.all()
        projects = Projects.query.all()
        projects_skills = Projects_Skills.query.all()
        

        about_me_list = [me.serialize() for me in about_me]
        skills_list = [skill.serialize() for skill in skills]
        universities_list = [university.serialize() for university in universities]
        course_skills_list = [course_skill.serialize() for course_skill in course_skills]
        courses_list = [course.serialize() for course in courses]
        education_list = [edu.serialize() for edu in education]
        platforms_list = [platform.serialize() for platform in platforms]
        projects_list = [project.serialize() for project in projects]
        projects_skills_list = [project_skill.serialize() for project_skill in projects_skills]

        return render_template("index.html", about_me=about_me_list, skills=skills_list, universities=universities_list, course_skills=course_skills_list,
                            courses=courses_list, educations=education_list, platforms=platforms_list, projects=projects_list,
                            project_skills=projects_skills_list), 200
    except Exception:
        logger.exception("[SERVER]: Error retrieving data")
        return jsonify({"message": "An internal error occurred"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=4000)