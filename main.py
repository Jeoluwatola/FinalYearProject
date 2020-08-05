from google.cloud import bigquery
from google.oauth2 import service_account
import smtplib
from flask import Flask, render_template, request, redirect
import random


app = Flask(__name__)
address = []
coden = []
add1 = []
pass1 = []


@app.route("/")
def index():
    return render_template("SignIn.html", chk1="1", chk2="1")


@app.route("/SignUp")
def signup():
    return render_template("SignUp.html")


@app.route("/Signed", methods=["POST"])
def signed():
    global email1    
    global user_idu
    global password1    
    email1 = request.form.get("Email")
    username = email1.split("@")[0]
    password1 = request.form.get("Password")
    email1 = email1.lower()
    results = biggquery()
    user_id1 = 0    
    password = encryption()
    for row in results:
        user_id0 = int(row['User_id'])
        if user_id0 > user_id1:
            user_id1 = user_id0
        # if ((row['Email'] == email1) and (row['VERIFIED'] == 'YES')):
        if ((row['Email'] == email1)):
            return render_template("SignIn.html", chk2="2", chk1="1")
    user_idu = user_id1 + 1
    credentials = service_account.Credentials.from_service_account_file(
            'JSONKEY.json')
    project_id = 'instant-binder-251011'
    client = bigquery.Client(credentials=credentials, project=project_id)
    query_job = client.query(
        """INSERT INTO QUICK_LEARN.User_Information (User_id, Email, Password, Username)
        VALUES ({},'{}','{}','{}')""".format(user_idu, email1, password, username))
    return redirect("/")


@app.route("/verify", methods=["POST"])
def verify():    
    email1 = request.form.get("Email")
    password1 = request.form.get("Password")
    email1 = email1.lower()
    add1.append(email1)
    pass1.append(password1)
    results = biggquery()
    for row in results:
        if ((row['Email'] == email1) and (row['VERIFIED'] == 'YES')):
            return render_template("SignIn.html", chk2="2", chk1="1")
    codelist = random.sample(range(0, 9), 6)
    codex = ''.join(str(e) for e in codelist)
    coden.append(codex) 
    message = "Your verification code is " + codex
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("templark4@gmail.com", "bdlcxsrfnqhitqiz")
    server.sendmail("templark4@gmail.com", email1, message)
    return render_template("Verify.html", chk3="1")


def biggquery():
    credentials = service_account.Credentials.from_service_account_file(
        'JSONKEY.json')
    project_id = 'instant-binder-251011'
    client = bigquery.Client(credentials=credentials, project=project_id)
    query_job = client.query(
        """SELECT * FROM QUICK_LEARN.User_Information LIMIT 1000""")
    results = query_job.result()
    return results


def encryption():
    a = 2
    f = ""
    l = len(password1)
    for e in password1:
        i = password1.find(e)
        p = i+a
        if p > l-1:
            p = (p-l)-1
        f += (password1[p])
        a = a+1
    return f


@app.route("/courses", methods=["POST"])
def courses():
    global user_id
    global password1
    email = request.form.get("Email")
    password1 = request.form.get("Password")
    password = encryption()
    email = email.lower()
    results = biggquery()
    for row in results:
        if (((row['Email'] == email) or row['Username'] == email) and (row['Password'] == password)):
            user_id = str(row['User_id'])
            address.append(email)
            return render_template("Courses.html", USER_ID=user_id)
    return render_template("SignIn.html", chk1="2", chk2="1")


@app.route("/Courses")
def courses2():
    return render_template("Courses.html", USER_ID=user_id)


@app.route("/profile")  
def profile():
    return render_template("Profile.html", USER_ID=user_id)


@app.route("/SignIn", methods=["POST"])
def signin(): 
    red = coden[-1]
    email1 = add1[-1]
    password1 = pass1[-1]
    password = encryption()
    username = email1.split("@")[0]
    user_id1 = 0    
    results = biggquery()
    for row in results:
        user_id0 = int(row['User_id'])
        if user_id0 > user_id1:
            user_id1 = user_id0        
    user_idu = user_id1 + 1
    coder = request.form.get("vcode")
    if (coder == red):
        credentials = service_account.Credentials.from_service_account_file(
            'JSONKEY.json')
        project_id = 'instant-binder-251011'
        client = bigquery.Client(credentials=credentials, project=project_id)
        query_job = client.query(
            """INSERT INTO QUICK_LEARN.User_Information (User_id, Email, Password, Username)
            VALUES ({},'{}','{}','{}')""".format(user_idu, email1, password, username))
        return redirect("/")
    else: 
        return render_template("Verify.html", chk3="2")


@app.route("/citiesbypopulation")
def coursevideo1():
    return render_template("Course_video.html", USER_ID=user_id)


@app.route("/wealthiestcountries")
def coursevideo2():
    return render_template("Course_video.html", USER_ID=user_id)


@app.route("/brandsbyrevenue")
def coursevideo3():
    return render_template("Course_video.html", USER_ID=user_id)


@app.route("/highestimports")
def coursevideo4():
    return render_template("Course_video.html", USER_ID=user_id)


@app.route("/internetusers")
def coursevideo5():
    return render_template("Course_video.html", USER_ID=user_id)


@app.route("/citiesbypopulation/assessment")
def assess1():
    return render_template("Assessment1.html", USER_ID=user_id)


@app.route("/wealthiestcountries/assessment")
def assess2():
    return render_template("Assessment2.html", USER_ID=user_id)


@app.route("/brandsbyrevenue/assessment")
def assess3():
    return render_template("Assessment3.html", USER_ID=user_id)


@app.route("/highestimports/assessment")
def assess4():
    return render_template("Assessment4.html", USER_ID=user_id)


@app.route("/internetusers/assessment")
def assess5():
    return render_template("Assessment5.html", USER_ID=user_id)


@app.route("/submit", methods=["POST"])
def submit():
    q1 = request.form.get("q1")
    q2 = request.form.get("q2")
    q3 = request.form.get("q3")
    q4 = request.form.get("q4")
    q5 = request.form.get("q5")
    q6 = request.form.get("q6")
    q7 = request.form.get("q7")
    q8 = request.form.get("q8")
    q9 = request.form.get("q9")
    q10 = request.form.get("q10")
    i = 0
    if(q1 == 'True'):
        i = i+1
    if(q2 == 'True'):
        i = i+1
    if(q3 == 'True'):
        i = i+1
    if(q4 == 'True'):
        i = i+1
    if(q5 == 'True'):
        i = i+1
    if(q6 == 'True'):
        i = i+1
    if(q7 == 'True'):
        i = i+1
    if(q8 == 'True'):
        i = i+1
    if(q9 == 'True'):
        i = i+1
    if(q10 == 'True'):
        i = i+1
    email = address[-1]
    credentials = service_account.Credentials.from_service_account_file(
            'JSONKEY.json')
    project_id = 'instant-binder-251011'
    client = bigquery.Client(credentials=credentials, project=project_id)
    query_job = client.query(
        """UPDATE QUICK_LEARN.User_Information SET Assessment_score = {} WHERE Email ='{}' """.format(i, email))
    return render_template("Thankyou.html", i=i, USER_ID=user_id)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)