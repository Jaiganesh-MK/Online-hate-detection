# Chrome Extension

-Hides inappropriate/offensive content in the web pages

### Main algo/model/idea

-Random Forest

### Tech stack 
- Python 
- NLP
- JavaScript, HTML

### Installation 
- Create a virtual environment in root project directory - `virtualenv env` 
- Activate the env - `source env/bin/activate` - 
- Install dependencies - `pip install -r requirements.txt` ... 
- Run `export FLASK_APP=app.py` in terminal
- Run `flask run`
- In Chrome run `chrome://extensions/`
- Turn Developer Mode On
- Click Load Unpacked and navigate to the folder containing the extension


### Known issues 
- Classifier needs more data
- Takes time to hide the text

### TODO 
- improve the classifier
- make the response faster
