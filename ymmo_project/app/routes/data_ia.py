from app import app
from flask import render_template

@app.route('/data-ia')
def data_ia():
    return render_template('data_ia.html')
