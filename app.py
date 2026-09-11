from flask import Flask, render_template,request
import sqlite3
import boto3
app = Flask(__name__)
dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
table = dynamodb.Table("MedicationSchedules")
ses = boto3.client("ses", region_name="eu-north-1")

def init_db():
    connection = sqlite3.connect("reminders.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            medication TEXT NOT NULL,
            email TEXT NOT NULL,
            reminder_time TEXT NOT NULL
        )
        """) 
    connection.commit()  
    
    connection.close()   
    
init_db()   
                   
                   
    
    
@app.route("/")

def home():
    return render_template("index.html")



@app.route("/set-reminder", methods=["POST"])
def set_reminder():
    name = request.form["name"]
    medication = request.form["medication"]
    email= request.form["email"]
    reminder= request.form["reminder_time"]
      
    
    connection=sqlite3.connect("reminders.db")
    cursor=connection.cursor()
    
    cursor.execute("""
        INSERT INTO reminders (name, medication, email, reminder_time)
        VALUES(?, ?, ?, ?)
    """,(name, medication, email, reminder))     
    
    connection.commit()

    connection.close()   
    
    table.put_item(
        Item={
            "user_id": email,
            "name": name,
            "email": email,
            "medication_name": medication,
            "schedule_times": [reminder]
        }
    )   
    
    return "reminder saved successfully"
    
   

@app.route("/reminders")
def reminders():
    connection = sqlite3.connect("reminders.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM reminders")
    data = cursor.fetchall()
    
    connection.close()

    
    return str(data)

    
    
   
    
app.run()

    

