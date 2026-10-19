from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
DATA_FILE = 'projects.json'

# Data load karne ka function
def load_projects():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Data save karne ka function
def save_projects(projects):
    with open(DATA_FILE, 'w') as file:
        json.dump(projects, file, indent=4)

# Home Page
@app.route('/')
def home():
    return render_template('index.html', projects=load_projects())

# Naya App Add Karne ka Page
@app.route('/add', methods=['GET', 'POST'])
def add_app():
    if request.method == 'POST':
        new_app = {
            "name": request.form['name'],
            "type": request.form['type'],
            "description": request.form['description'],
            "download_link": request.form['download_link'],
            "version": request.form['version'],
            "size": request.form['size']
        }
        projects = load_projects()
        projects.append(new_app)
        save_projects(projects)
        return redirect(url_for('home'))
    return render_template('add.html')

# ==========================================
# YEH HISSA INTERNET (RENDER) PAR CHALANE KE LIYE HAI
# ==========================================
if __name__ == '__main__':
    # Render humein ek 'PORT' deta hai, agar local PC par ho toh 5000 use hoga
    port = int(os.environ.get('PORT', 5000))
    # host='0.0.0.0' lagana zaroori hai taake bahar se koi website khol sake
    app.run(host='0.0.0.0', port=port, debug=True)