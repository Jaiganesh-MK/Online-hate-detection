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

df = pd.read_csv("labeled_data.csv")
vectorizer = CountVectorizer()
vectorizer.fit_transform(df['tweet'].values.astype('U'))
# load the trained model
rf = joblib.load('NM_classifier.pkl')

def predict(str):
    return rf.predict(vectorizer.transform([str]))

@app.route("/")
def index():
    return ("Default route")

@app.route('/_get_data/', methods=['POST'])
def _get_data():
    data = {}
    data["success"] = False
    if request.method == "POST":
        data["hate"] = []
        content = request.form.get("data")
        a = str(content).split()
        hate = []
        for i in range(0,len(a)):
            if(predict(a[i])==1):
                data['hate'].append(a[i])
        data["success"] = True
        
   
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

