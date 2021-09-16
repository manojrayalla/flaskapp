from flask import Flask
app = Flask(__name__)
@app.route('/')
import pyodbc
server = 'manojtest.database.windows.net'
database = 'manojtest'
username = 'manojtest'
password = 'Manoj@143Archu'   
driver= '{ODBC Driver 17 for SQL Server}'

def getagent_number():
    agentnumber = request.args.get("agentnumber")
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
    cursor.execute("select * from dimagent where agentnum = {}".format(agentnumber)
    row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
            result = json.loads(row)        
    cursor.close()
    return result
    
    
