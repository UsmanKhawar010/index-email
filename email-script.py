import smtplib
from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/about')
def about():
    # Your about page logic here
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    receiver_email = request.form['receiver_email']
    subject = request.form['subject']
    message = request.form['message']

    send_email(email, receiver_email, subject, message)

    return redirect(url_for('index'))

def send_email(email, receiver_email, subject, message):
    text = f"Subject: {subject} \n \n {message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "zsnm fvta xoeb fuov")
    server.sendmail(email, receiver_email, text)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
