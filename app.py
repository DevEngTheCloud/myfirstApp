from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello Group 1, this is workshop 2! New changes!!'
