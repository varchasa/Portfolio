from flask import Flask, render_template,request,jsonify
from flask_mail import Mail, Message

import smtplib

app = Flask(__name__)
mail = Mail(app)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'varchasa.tech@gmail.com',
	MAIL_PASSWORD = 'varchasa@0602'
	)
mail = Mail(app)

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
            to = 'varchasa.tech@gmail.com'
            print("done4")
        
    
            text = Message(name, sender = gmail, recipients=[to])
            text.body=suggestion+" "+gmail+"\n"+"portfolio data"
            
            
            print("done3")
            
            print("done1")
            mail.send(text)
            return render_template("home.html")
    except:
        return('PLEASE FILL OUT THE REQUIRED DATA')
        
if __name__ == '__main__':
    app.run(debug=True)