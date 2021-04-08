from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home_page.html')
@app.route("/big_money")
def render_dog():
    return render_template('wealth.html',bill=wealth_ammount())
@app.route("/action"):
    def render_dog():
    return render_template('action.html',bill=wealth_ammount())
def wealth_ammount():
    with open('billionaires.json') as f:
        data = json.load(f)
    amountOfmoney = []
    options=""
    for x in data:
        if not x['wealth']['worth in billions'] in amountOfmoney:
            amountOfmoney.append(x['wealth']['worth in billions'])
    print("data")
    for number in amountOfmoney:
        options += Markup("<option value=\"" + str(number) + "\">" + str(number) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
if __name__ =="__main__":
    app.run(debug=False,port=54321)
    
