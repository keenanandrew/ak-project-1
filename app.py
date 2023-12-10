from flask import Flask, render_template, request
import os
import numpy as np 
import pandas as pd 
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__) # initialise a Flask app

@app.route('/', methods = ['GET'])
def homePage():
    return render_template("index.html") # opens the html file in templates/index.html

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)