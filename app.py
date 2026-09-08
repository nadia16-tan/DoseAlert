from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)

def init_db():
    connection = sqlite3.connect("reminders.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            medication TEXT NOT NULL,
            email TEXT NOT NULL,
            reminder_time TEXT NOT NULL, 
        )
        """) 
    connection.commit()          
                   
                   
    
    
@app.route("/")

def home():
    return render_template("index.html")



@app.route("/set-reminder", methods=["POST"])
def set_reminder():
    medication = request.form["medication"]
    email= request.form["email"]
    reminder= request.form["reminder_time"]
    
    return "reminder saved successfully"

    
    
   
    
app.run()

    

