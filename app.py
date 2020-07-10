from flask import Flask
from flask import render_template
from flask import request
import csv


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')

if __name__ =='__main__':
    app.run(debug=True)

