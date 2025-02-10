from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Portfolio data storage
PORTFOLIO_FILE = 'portfolio_data.json'

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def load_portfolio():
    if os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_portfolio(data):
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    portfolio = load_portfolio()
    return render_template('index.html', portfolio=portfolio)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        portfolio_data = {
            'name': request.form.get('name'),
            'title': request.form.get('title'),
            'about': request.form.get('about'),
            'skills': request.form.get('skills').split(','),
            'projects': request.form.get('projects').split('\n'),
            'contact': {
                'email': request.form.get('email'),
                'linkedin': request.form.get('linkedin'),
                'github': request.form.get('github')
            }
        }
        save_portfolio(portfolio_data)
        return redirect(url_for('portfolio'))
    return render_template('create.html')

@app.route('/portfolio')
def portfolio():
    portfolio = load_portfolio()
    return render_template('portfolio.html', portfolio=portfolio)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        portfolio = load_portfolio()
        if 'images' not in portfolio:
            portfolio['images'] = []
        portfolio['images'].append(file_path)
        save_portfolio(portfolio)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
