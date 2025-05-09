from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello Group 2 has the test been corrected!'
