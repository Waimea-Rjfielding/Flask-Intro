from flask import Flask
from random import randint

app = Flask(__name__)


@app.get("/")
def home():
    return "<h1>Hello, World!</h1>"

@app.get("/random/")
def random():
    return str(randint(1,100000000000000000))