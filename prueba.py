from flask import Flask,render_template,request,redirect
from flask.globals import request
import os
import random

from flask.helpers import locked_cached_property

app = Flask(__name__)

@app.route('/')
def inicio():
    title="Menu Principal"
    return render_template('Ej21.html',title=title)

if __name__=="__main__":
    app.run(debug=True)