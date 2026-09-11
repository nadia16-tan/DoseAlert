from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)

def init_db():
    connection = sqlite3.connect("reminders.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    medication = request.form["medication"]
    email= request.form["email"]
    reminder= request.form["reminder_time"]
      
    
    connection=sqlite3.connect("reminders.db")
    cursor=connection.cursor()
    
    cursor.execute("""
        INSERT INTO reminders (medication, email, reminder_time)
        VALUES(?, ?, ?)
    """,(medication, email, reminder))     
    
    connection.commit()

    connection.close()      
    
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

    

