from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Portfolio data storage
PORTFOLIO_FILE = 'portfolio_data.json'

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

if __name__ == '__main__':
    app.run(debug=True)
