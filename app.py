from flask import Flask
import pyodbc
import json
import uuid
import requests
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session  # https://pythonhosted.org/Flask-Session
import msal
import app_config

app = Flask(__name__)
app.config.from_object(app_config)
Session(app)
@app.route('/')
def getagent_number():
    server = 'manojtest.database.windows.net'
    database = 'manojtest'
    username = 'manojtest'
    password = 'Manoj@143Archu'   
    driver= '{ODBC Driver 17 for SQL Server}'
    agentnumber = request.args.get('agentnumber')
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute("select * from dimagent where agentnum = {}".format(agentnumber))
    check = cursor.fetchone()
    columns = [column[0] for column in cursor.description]
    data = dict(zip(columns, check))
    return data
    
    
