from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Levels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(25), unique=True, nullable=False)

    def __str__(self):
        return "Level: {}".format(self.level)
    
    def serialize(self):
        return {
            "id": self.id,
            "level": self.level
        }


class Technologies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    technology_name = db.Column(db.String(25), unique=True, nullable=False)
    type = db.Column(db.String(25), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False) 

    def __str__(self):
        return "Technology: {}".format(self.technology_name)
    
    def serialize(self):
        return {
            "id": self.id,
            "technology_name": self.technology_name,
            "type": self.type,
            "level_id": self.level_id
        }


class Tools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(25), unique=True, nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False) 

    def __str__(self):
        return "Tool: {}".format(self.tool_name)
    
    def serialize(self):
        return {
            "id": self.id,
            "tool_name": self.tool_name,
            "level_id": self.level_id
        }


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(25), unique=True, nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False) 

    def __str__(self):
        return "Skill: {}".format(self.skill)

    def serialize(self):
        return {
            "id": self.id,
            "skill": self.skill,
            "level_id": self.level_id
        }


class Universities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    university_name = db.Column(db.String(50), unique=True, nullable=False)
    university_city = db.Column(db.String(25), nullable=False)
    university_state = db.Column(db.String(25), nullable=False)
    university_country = db.Column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "university_name": self.university_name,
            "university_city": self.university_city,
            "university_state": self.university_state,
            "university_country": self.university_country
        }


class Course_Technologies(db.Model):
    __tablename__ = 'course_technologies'
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('technologies.id'), primary_key=True)

    def serialize(self):
        return {
            "course_id": self.course_id,
            "technology_id": self.technology_id
        }


class Course_Tools(db.Model):
    __tablename__ = 'course_tools'
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tools.id'), primary_key=True)

    def serialize(self):
        return {
            "course_id": self.course_id,
            "tool_id": self.tool_id
        }


class Course_Skills(db.Model):
    __tablename__ = 'course_skills'
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), primary_key=True)

    def serialize(self):
        return {
            "course_id": self.course_id,
            "skill_id": self.skill_id
        }


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), unique=True, nullable=False)
    course_description = db.Column(db.String(200), nullable=False)
    platform_id = db.Column(db.Integer, db.ForeignKey('platforms.id'), nullable=False)
    certificate_url = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "course_description": self.course_description,
            "platform_id": self.platform_id,
            "certificate_url": self.certificate_url
        }


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(25), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('universities.id'), nullable=False)
    start_date = db.Column(db.String(15), nullable=False)
    end_date = db.Column(db.String(15), nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    degree_url = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "degree": self.degree,
            "university_id": self.university_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "gpa": self.gpa,
            "degree_url": self.degree_url
        }


class Platforms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform_name = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "platform_name": self.platform_name
        }


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(50), nullable=False)
    project_description = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "project_description": self.project_description
        }


class Projects_Technologies(db.Model):
    __tablename__ = 'projects_technologies'
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey('technologies.id'), primary_key=True)

    def serialize(self):
        return {
            "project_id": self.project_id,
            "technology_id": self.technology_id
        }


class Projects_Tools(db.Model):
    __tablename__ = 'projects_tools'
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tools.id'), primary_key=True)

    def serialize(self):
        return {
            "project_id": self.project_id,
            "tool_id": self.tool_id
        }


class Projects_Skills(db.Model):
    __tablename__ = 'projects_skills'
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), primary_key=True)

    def serialize(self):
        return {
            "project_id": self.project_id,
            "skill_id": self.skill_id
        }


class About_Me(db.Model):
    __tablename__ = 'about_me'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    about_me = db.Column(db.String(500), nullable=False)
    start_date = db.Column(db.String(15), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "about_me": self.about_me,
            "start_date": self.start_date
        }