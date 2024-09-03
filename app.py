from flask import Flask,render_template,request
import google.generativeai as palm
import os

api = os.getenv("MAKERSUITE_API_TOKEN") 
palm.configure(api_key=api)
model = { 'model': "models/text-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/financial_QA",methods=["GET","POST"])
def financial_QA():
    return(render_template("financial_QA.html"))

@app.route("/financial_news",methods=["GET","POST"])
def financial_news():
    return(render_template("financial_news.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    q = request.form.get("q")
    r = palm.generate_text(prompt=q, **model)
    return(render_template("makersuite.html",r=r.result))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

if __name__ == "__main__":
    app.run()
