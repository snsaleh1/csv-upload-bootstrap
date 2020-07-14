from flask import Flask
from flask import render_template
from flask import request
import csv


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method=='POST':
        user_csv = request.form.get('user_csv')
        print(user_csv)

if __name__ =='__main__':
    app.run(debug=True)

