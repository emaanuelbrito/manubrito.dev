import sqlite3 as sql
import os

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, "data.db")
DB_PATH = database_path

def create_DB():
    conn = sql.connect(DB_PATH)
    conn.commit()
    conn.close()


def create_table():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS levels (
            id INTEGER,
            level TEXT NOT NULL,
            PRIMARY KEY (id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS technologies (
                id INTEGER,
                technology_name TEXT NOT NULL UNIQUE,
                type TEXT NOT NULL,
                level_id INTEGER,
                PRIMARY KEY (id),
                FOREIGN KEY (level_id) REFERENCES levels(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS tools (
                id INTEGER,
                tool_name TEXT NOT NULL UNIQUE,
                level_id INTEGER,
                PRIMARY KEY (id),
                FOREIGN KEY (level_id) REFERENCES levels(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS skills (
            id INTEGER,
            skill TEXT NOT NULL UNIQUE,
            level_id INTEGER,
            PRIMARY KEY (id),
            FOREIGN KEY (level_id) REFERENCES levels(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects (
            id INTEGER,
            project_name TEXT NOT NULL UNIQUE,
            project_description TEXT NOT NULL,
            PRIMARY KEY (id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects_skills (
            project_id INTEGER,
            skill_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects_technologies (
            project_id INTEGER,
            technology_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (technology_id) REFERENCES technologies(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects_tools (
            project_id INTEGER,
            tool_id INTEGER,
            FOREIGN KEY (project_id) REFERENCES projects(id),
            FOREIGN KEY (tool_id) REFERENCES tools(id)   
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS universities (
            id INTEGER,
            university_name TEXT NOT NULL UNIQUE,
            university_city TEXT NOT NULL,
            university_state TEXT NOT NULL,
            university_country TEXT NOT NULL,
            PRIMARY KEY (id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS education (
            id INTEGER,
            degree TEXT NOT NULL UNIQUE,
            university_id INTEGER,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            GPA NUMERIC NOT NULL,
            degree_url TEXT NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (university_id) REFERENCES universities(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS platforms (
            id INTEGER,
            platform_name TEXT NOT NULL UNIQUE,
            PRIMARY KEY (id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS courses (
            id INTEGER,
            course_name TEXT NOT NULL,
            course_description TEXT NOT NULL,
            platform_id INTEGER,
            certificate_url TEXT NOT NULL,
            PRIMARY KEY (id),
            FOREIGN KEY (platform_id) REFERENCES platforms(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS course_skills (
            course_id INTEGER,
            skill_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (skill_id) REFERENCES skills(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS course_technologies (
            course_id INTEGER,
            technology_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (technology_id) REFERENCES technologies(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS course_tools (
            course_id INTEGER,
            tool_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id)
            FOREIGN KEY (tool_id) REFERENCES tools(id)
        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS about_me (
            id INTEGER,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            about_me TEXT NOT NULL,
            start_date TEXTO NOT NULL,
            PRIMARY KEY (id)
        )""")
    conn.commit()
    conn.close()

def add_levels():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    levels = [(1, "Principiante"),
            (2, "Elemental"),
            (3, "Intermedio"),
            (4, "Avanzado")]
    for level in levels:
        cursor.execute("INSERT OR IGNORE INTO levels (id, level) VALUES (?, ?)", level)
    conn.commit()
    conn.close()


def add_technologies():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    technologies = [(1, "Python", "core", 3),
                    (2, "Flask", "framework", 2),
                    (3, "SQLAlchemy", "ORM", 2),
                    (4, "SQLite", "database", 3),
                    (5, "HTML", "core", 2),
                    (6, "CSS", "core", 2),
                    (7, "Bootstrap", "framework", 2),
                    (8, "Tailwind CSS", "framework", 2),
                    (9, "JavaScript", "core", 1),
                    (10, "Git", "core", 3),
                    (11, "Linux", "core", 3),
                    (12, "Docker", "containerization", 1)]
    for technology in technologies:
        cursor.execute("INSERT OR IGNORE INTO technologies (id, technology_name, type, level_id) VALUES (?, ?, ?, ?)", technology)
    conn.commit()
    conn.close()


def add_tools():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    tools = [(1, "VS Code", 3),
            (2, "Figma", 3),
            (3, "Trello", 2),
            (4, "Notion", 3),
            (5, "Obsidian", 2),
            (6, "Wireshark", 2),
            (7, "VirtualBox", 2),
            (8, "GitHub", 3),
            (9, "Docker", 1),
            (10, "AI", 3),
            (11, "Cisco Packet Tracer", 2)]
    for tool in tools:
        cursor.execute("INSERT OR IGNORE INTO tools (id, tool_name, level_id) VALUES (?, ?, ?)", tool)
    conn.commit()
    conn.close()


def add_skills():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    skills = [(1, "Programación", 3),
            (2, "Estructura de Datos", 2),
            (3, "Algoritmos", 2),
            (4, "Bases de Datos", 3),
            (5, "Desarrollo Backend", 2),
            (6, "Diseño Frontend", 3),
            (7, "Desarrollo Frontend", 2),
            (8, "Ciberseguridad", 3),
            (9, "Detección de Amenazas", 2),
            (10, "Vulnerabilidades de Red", 2),
            (11, "Direcciones IPv4", 3),
            (12, "Medios de Red", 2),
            (13, "Tipos de Red", 2),
            (14, "Servicios Capa de Aplicación", 2),
            (15, "Protocolos Estándar", 2),
            (16, "Diseños Jerárquicos de Red", 2),
            (17, "Protocolos Capa de Red", 2),
            (18, "Dispositivos Cisco", 2),
            (19, "Cisco IOS", 2),
            (20, "Sistemas Binarios", 3),
            (21, "Protocolos Capa de Transporte", 2),
            (22, "DHCP", 2),
            (23, "DNS", 2),
            (24, "ARP", 2),
            (27, "Contenerización", 2)]
    for skill in skills:
        cursor.execute("INSERT OR IGNORE INTO skills (id, skill, level_id) VALUES (?, ?, ?)", skill)
    conn.commit()
    conn.close()


def add_universities():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    universities = [(1, "Instituto Universitario Politécnico Santiago Mariño", "Porlamar", "Nueva Esparta", "Venezuela"), 
                    (2, "Universidad Nacional Abierta", "La Asuncion", "Nueva Esparta", "Venezuela")]
    for university in universities:
        cursor.execute("INSERT OR IGNORE INTO universities (id, university_name, university_city, university_state, university_country) VALUES (?, ?, ?, ?, ?)", university)
    conn.commit()
    conn.close()


def add_courses():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    courses = [(1, "Networking Basics", "Start learning the basics of computer networking and discover how networks operate.", 1, 
                "https://drive.google.com/file/d/1vqqwKtbQA1aNMQkzxYE7wzMhRu6j9uNO/view?usp=drive_link"),
            (2, "Tools of the Trade: Linux and SQL", "Explain the relationship between operating systems, applications, and hardware", 2, 
            "https://coursera.org/share/a829bb846dd83910708b469c8fd69681"),
            (3, "Connect and Protect: Networks and Network Security", "Define the types of networks and components of networks", 2, 
            "https://coursera.org/share/722744d1f980a18d0c1ffaa0c8323d1f"),
            (4, "Introduction to Cybersecurity", "Explore the exciting field of cybersecurity and why cybersecurity is a future-proof career.", 1, 
            "https://drive.google.com/file/d/1H7tK2CaCnJOP23kNVSrKpSZuihI1o__z/view?usp=sharing"),
            (5, "Play It Safe: Manage Security Risks", "Identify the primary threats, risks, and vulnerabilities to business operations.", 2, 
            "https://coursera.org/share/abe07e4eed84e29f6c6bb63ed0b59b3d"),
            (6, "Foundations of Cybersecurity", "Recognize core skills and knowledge needed to become a cybersecurity analyst", 2, 
            "https://www.coursera.org/account/accomplishments/verify/B7B6J8XPR6M8"),
            (7, "CS50’s Introduction to Computer Science", "An introduction to the intellectual enterprises of computer science and the art of programming.", 6, 
            "https://certificates.cs50.io/80ff37c5-33ff-40e2-943a-0904bf1e2268.pdf?size=letter"),
            (8, "CS50’s Introduction to Programming with Python", "An introduction to programming using a language called Python.", 6, 
            "Por obtener"),
            (9, "CS50’s Introduction to Databases with SQL", "An introduction to databases using a language called SQL (Structured Query Language).", 6, 
            "Por obtener"),
            (10, "Dispositivos de Red y Configuración Inicial", "Este curso cubre los aspectos esenciales de los dispositivos de red y cómo configurarlos.", 1, 
            "https://drive.google.com/file/d/1h-jvHmYqYaY9sfkCtQYG2lwAT4skWy-Z/view?usp=sharing")]
    for course in courses:
        cursor.execute("INSERT OR IGNORE INTO courses (id, course_name, course_description, platform_id, certificate_url) VALUES (?, ?, ?, ?, ?)", course)
    conn.commit()
    conn.close()


def add_platforms():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    platforms = [(1, "CISCO Networking Academy"), 
                (2, "Coursera"), 
                (3, "Platzi"), 
                (4, "Udemy"), 
                (5, "Academia Fermín Toro"), 
                (6, "Harvard Online"), 
                (7, "Academia Hola Mundo"), 
                (8, "MoureDevPro")]
    for platform in platforms:
        cursor.execute("INSERT OR IGNORE INTO platforms (id, platform_name) VALUES (?, ?)", platform)
    conn.commit()
    conn.close()

def add_education():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    education = [(1, "Ingeniero Civil", 1, "Septiembre 2014", "Abril 2021", 2.3, "Por obtener"),
                (2, "Ingeniero en Sistemas", 2, "Marzo 2025", "Presente", 0, "Por obtener")]
    for edu in education:
        cursor.execute("INSERT OR IGNORE INTO education (id, degree, university_id, start_date, end_date, GPA, degree_url) VALUES (?, ?, ?, ?, ?, ?, ?)", edu)
    conn.commit()
    conn.close()


def add_course_technologies():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    course_technologies = [(2, 11),
                        (3, 11),
                        (7, 1),
                        (7, 2),
                        (7, 4),
                        (7, 5),
                        (7, 6),
                        (7, 7),
                        (7, 9),
                        (8, 1),
                        (9, 4)]
    for course_technology in course_technologies:
        cursor.execute("INSERT OR IGNORE INTO course_technologies (course_id, technology_id) VALUES (?, ?)", course_technology)
    conn.commit()
    conn.close()


def add_course_tools():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    course_tools = [(1, 11),
                    (7, 1),
                    (7, 10),
                    (8, 1),
                    (8, 10),
                    (9, 1),
                    (9, 10),
                    (10, 6),
                    (10, 7),
                    (10, 11)]
    for course_tool in course_tools:
        cursor.execute("INSERT OR IGNORE INTO course_tools (course_id, tool_id) VALUES (?, ?)", course_tool)
    conn.commit()
    conn.close()


def add_course_skills():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    course_skills = [(1, 11),
                    (1, 12),
                    (1, 13),
                    (1, 14),
                    (1, 15),
                    (2 ,4),
                    (3, 10),
                    (3, 13),
                    (4, 8),
                    (4, 9),
                    (4, 10),
                    (5, 9),
                    (5, 10),
                    (6, 8),
                    (6, 9),
                    (6, 10),
                    (7, 1),
                    (7, 2),
                    (7, 3),
                    (7, 4),
                    (7, 5),
                    (7, 7),
                    (8, 1),
                    (8, 2),
                    (8, 3),
                    (9, 4),
                    (10, 16),
                    (10, 17),
                    (10, 18),
                    (10, 19),
                    (10, 20),
                    (10, 21),
                    (10, 22),
                    (10, 23),
                    (10, 24)]
    for course_skill in course_skills:
        cursor.execute("INSERT OR IGNORE INTO course_skills (course_id, skill_id) VALUES (?, ?)", course_skill)
    conn.commit()
    conn.close()

def add_projects():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    projects = [(1, "manubritodev", "Personal website to showcase my projects and skills"),
                (2, "Password Generator", "Simple password generator using Python")]
    for project in projects:
        cursor.execute("INSERT OR IGNORE INTO projects (id, project_name, project_description) VALUES (?, ?, ?)", project)
    conn.commit() 
    conn.close()


def add_projects_technologies():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    projects_technologies = [(1, 1),
                            (1, 2),
                            (1, 3),
                            (1, 4),
                            (1, 5),
                            (1, 6),
                            (1, 8),
                            (1, 9),
                            (1, 10),
                            (2, 1),
                            (2, 2),
                            (2, 4),
                            (2, 5),
                            (2, 6),
                            (2, 7),
                            (2, 9)]
    for project_technology in projects_technologies:
        cursor.execute("INSERT OR IGNORE INTO projects_technologies (project_id, technology_id) VALUES (?, ?)", project_technology)
    conn.commit()
    conn.close()


def add_projects_tools():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    projects_tools = [(1 ,1),
                    (1, 2),
                    (1, 3),
                    (1, 5),
                    (1, 8),
                    (1, 10),
                    (2 ,1),
                    (2, 10)]
    for project_tool in projects_tools:
        cursor.execute("INSERT OR IGNORE INTO projects_tools (project_id, tool_id) VALUES (?, ?)", project_tool)
    conn.commit()
    conn.close()


def add_projects_skills():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    project_skills = [(1, 1,),
                    (1, 2),
                    (1, 3),
                    (1, 4),
                    (1, 5),
                    (1, 6),
                    (1, 7),
                    (2, 1),
                    (2, 3),
                    (2, 5),
                    (2, 7)]
    for project_skill in project_skills:
        cursor.execute("INSERT OR IGNORE INTO projects_skills (project_id, skill_id) VALUES (?, ?)", project_skill)
    conn.commit()
    conn.close()


def about_me():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    about_me = [(1, "Emanuel", "Brito", "ing.emanuelbrito@gmail.com", """Me apasiona aprender y aplicar la tecnología para resolver problemas. 
                Actualmente estudio un grado en Ingeniería de Sistemas y trabajo en proyectos personales para mejorar mis habilidades.""", "09/01/2024")]
    for about in about_me:
        cursor.execute("INSERT OR IGNORE INTO about_me (id, first_name, last_name, email, about_me, start_date) VALUES (?, ?, ?, ?, ?, ?)", about)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_DB()
    create_table()
    add_levels()
    add_technologies()
    add_tools()
    add_skills()
    add_universities()
    add_courses()
    add_platforms()
    add_education()
    add_course_technologies()
    add_course_tools()
    add_course_skills()
    add_projects()
    add_projects_technologies()
    add_projects_tools()
    add_projects_skills()
    about_me()
    print("Database created and populated successfully")