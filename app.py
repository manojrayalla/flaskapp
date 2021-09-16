from flask import Flask
import pyodbc
import json
from flask import request
app = Flask(__name__)
@app.route('/')
def getagent_number():
    return "manoj"
    
    
