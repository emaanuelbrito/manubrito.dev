from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/education')
def education():
    return render_template('education.html', active_page='education')

# app.py
if __name__ == '__main__':
    app.run(debug=True)  # Auto-reload enabled