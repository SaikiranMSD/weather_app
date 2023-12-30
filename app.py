from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/template",methods=["POST","GET"])
def hello_world():
    param={
        'q':request.form.get("city"),
        'appid':request.form.get("appid"),
        'units':request.form.get("units"),
    }
    data=requests.get("https://api.openweathermap.org/data/2.5/weather",params=param)
    return data.json()


@app.route("/")
def rendertemplate():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)
