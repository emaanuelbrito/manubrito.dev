import logging
from datetime import date
from Models import (db, Levels, Skills, Technologies, Tools, Universities, Course_Skills, 
                    Course_Technologies, Course_Tools, Courses, Education, Platforms, 
                    Projects, Projects_Skills, Projects_Technologies, Projects_Tools, About_Me
                )

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Function to fetch data
def fetch_serialized_data(model):
    return [item.serialize() for item in model.query.all()]

def get_levels():
    """Fetch all levels data"""
    try:
        return fetch_serialized_data(Levels)
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching levels data: {e}")
        return None

def get_technologies_data():
    """Fetch all technologies data"""
    try:
        return fetch_serialized_data(Technologies)
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching technologies data: {e}")
        return None
    
def get_tools_data():
    """Fetch all tools data"""
    try:
        return fetch_serialized_data(Tools)
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching tools data: {e}")
        return None

def get_skills_data():
    """Fetch all skills data"""
    try:
        return fetch_serialized_data(Skills)
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching skills data: {e}")
        return None
    
def get_about_data():
    """Fetch all about me data"""
    try:
        return fetch_serialized_data(About_Me)
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching about me data: {e}")
        return None

def get_courses_data():
    """Fetch all courses data"""
    try:
        return {
            "courses": fetch_serialized_data(Courses),
            "course_skills": fetch_serialized_data(Course_Skills),
            "course_technologies": fetch_serialized_data(Course_Technologies),
            "course_tools": fetch_serialized_data(Course_Tools),
            "platforms": fetch_serialized_data(Platforms)
        }
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching courses data: {e}")
        return None

def get_education_data():
    """Fetch all education data"""
    try:
        return {
            "education": fetch_serialized_data(Education),
            "universities": fetch_serialized_data(Universities)
        }
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching education data: {e}")
        return None
    
def get_projects_data():
    """Fetch all projects data"""
    try:
        return {
            "projects_count": db.session.query(Projects).count(),
            "projects": fetch_serialized_data(Projects),
            "projects_skills": fetch_serialized_data(Projects_Skills),
            "projects_technologies": fetch_serialized_data(Projects_Technologies),
            "projects_tools": fetch_serialized_data(Projects_Tools)
        }
    except Exception as e:
        logger.error(f"[SERVER]: Error fetching projects data: {e}")
        return None
    
def calculate_experience(start_date):
    current_date = date.today()
    years = current_date.year - start_date.year
    months = current_date.month - start_date.month
    days = current_date.day - start_date.day
    if days < 0:
        months -= 1
    
    if months < 0 or (months == 0 and days < 0):
        years -= 1
        months += 12

    return {"years": years, "months": max(months, 0)}

def get_all_data():
    return {
        "levels": get_levels(),
        "about_me": get_about_data(),
        "technologies": get_technologies_data(),
        "tools": get_tools_data(),
        "skills": get_skills_data(),
        **get_courses_data(),
        **get_education_data(),
        **get_projects_data(),
    }