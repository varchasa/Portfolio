from flask import Flask, render_template,request,jsonify
import firebase
from firebase import Firebase


app = Flask(__name__)
config = {
   "apiKey": "**************",
  "authDomain": "**************",
  "databaseURL": "**************",
  "projectId": "**************",
  "storageBucket": "**************",
  "messagingSenderId": "**************",
  "appId": "**************",
  "measurementId": "**************"
}
firebase = Firebase(config)
db = firebase.database()

@app.route("/")
def home():
    #name=request.form.get("name")
    #mail=request.form.get("mail")
    #suggestion=request.form.get("suggestion")

    return render_template('home.html')

@app.route("/send_message", methods=["GET","POST"])
def send_message():
    try:
        if request.method == 'POST':
            
            name=request.form['name']
            gmail=request.form['email']
            suggestion=request.form['suggestion'] 
            data={'name':name,'email':gmail,'msg':suggestion}
            db.child("users").push(data)
            return render_template("home.html")
    except:
        return('PLEASE FILL OUT THE REQUIRED DATA')
        
if __name__ == '__main__':
    app.run(host="192.168.43.141",debug=True)
