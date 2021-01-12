from flask import Flask, render_template,request
import pickle
app=Flask(__name__)
clf = pickle.load(open("heart_attach_calssifier.pkl","rb"))
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/',methods=['POST'])
def get_value():
    age=float(request.form['age'])
    gender=int(request.form['gender'])
    cp=float(request.form['cp'])
    trestbps=float(request.form['trestbps'])
    chol=float(request.form['chol'])
    fbs=float(request.form['fbs'])
    restecg=float(request.form['restecg'])
    thalach=float(request.form['thalach'])
    exang=float(request.form['exang'])
    oldpeak=float(request.form['oldpeak'])
    slope=float(request.form['slope'])
    ca=float(request.form['ca'])
    thal=float(request.form['thal'])
    #load data form pachient
    test = [[age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
    text=""
    if 0 in clf.predict(test):
        text="you are well"
    else:
        text="You are ill ,you should see a doctor"
    return render_template('pass.html',n=text)