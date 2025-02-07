# Portfolio Maker

A simple Flask web application that helps you create and showcase your professional portfolio.

## Features

- Easy-to-use form-based portfolio creation
- Clean and responsive design
- Skills and projects showcase
- Contact information display
- Professional layout

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Click on "Create Portfolio" to start building your portfolio
2. Fill in your information in the form:
   - Full name
   - Professional title
   - About me section
   - Skills (comma-separated)
   - Projects (one per line)
   - Contact information
3. Submit the form to create your portfolio
4. View your portfolio at any time by clicking "View Portfolio"

## Directory Structure

```
portfolio_maker/
│── static/          # CSS, JS, images
│── templates/       # HTML files
│── app.py          # Main Flask application
│── requirements.txt # Dependencies
│── README.md       # Project documentation