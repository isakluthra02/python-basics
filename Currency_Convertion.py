from flask import Flask, render_template, request
import requests

application=Flask(__name__)

fixerApi="SampleApi"

@application.route('/',methods=['GET', 'POST'])
def home():
    result = None
    if request.method == "POST":
        Day=request.form.get("Day")
        Month=request.form.get("Month")
        Year=request.form.get("Year")
        Currency=request.form.get("Currency")
        date=f"{Year}-{Month.zfill(2)}-{Day.zfill(2)}"
        link=f"http://data.fixer.io/api/{date}?access_key={fixerApi}"
        response=requests.get(link)
        data=response.json()
        if data.get("success") and Currency in data["rates"]:
            rate=data["rates"][Currency]
            result=f"Euro on {date}:- 1 EUR = {rate} {Currency}"
        else:
            result="Some error occured"
    return render_template("htmlfile.html",result=result)
if __name__ == '__main__':
    application.run(debug=True)