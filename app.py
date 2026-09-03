from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")

def home():
    return render_template("index.html")
app.run()


@app.route("/set-reminder", methods=["POST"])
def set_reminder():
    medication = request.form["medication"]
   
    
app.run()

    

