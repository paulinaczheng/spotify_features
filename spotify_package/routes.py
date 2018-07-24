from flask import render_template, jsonify, json
from spotify_package.models import *
from spotify_package import *
from spotify_package.dashboard import app

@app.server.route('/conclusions')
def findings():
    return render_template('conclusions.html')
