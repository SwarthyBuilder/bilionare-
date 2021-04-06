from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home_page.html')
@app.route("/big_money")
def render_dog():
    return render_template('wealth.html')

def wealth_ammount():
    with open('billionaires.json') as f:
        data = json.load(f)
    listOfStates = []
    for x in data:
        if data['State'] in listOfStates:
            listOfStates.append('State')
    print("data")

if __name__ =="__main__":
    app.run(debug=False,port=54321)
