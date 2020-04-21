import requests
from flask import Flask,jsonify,request,render_template
import pandas as pd 
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier



app = Flask(__name__)


@app.route("/")
def index():
    return ("Default route")

@app.route('/_get_data/', methods=['POST'])
def _get_data():
    data = request.form.get("data")
    df = pd.read_csv("labeled_data.csv")
    vectorizer = CountVectorizer()
    vectorizer.fit_transform(df['tweet'].values.astype('U'))
    # load the trained model
    rf = joblib.load('NM_classifier.pkl')
    a = str(data).split()
    hate = ['dafuq']
    for i in range(0,len(a)):
        if(rf.predict(vectorizer.transform([a[i]]))==1):
            hate.append(a[i])
   
    return jsonify({"rate":hate})

