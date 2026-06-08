from app import app
from flask import render_template

@app.route('/agence/<int:agence_id>')
def agence(agence_id):
    return render_template('agence.html', agence_id=agence_id)
