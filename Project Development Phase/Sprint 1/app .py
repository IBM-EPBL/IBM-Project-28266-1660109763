from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/forgot")
def forgot():
    return render_template('forgot.html')

@app.route("/dashbord")
def about():
    return render_template('dashboard.html')
