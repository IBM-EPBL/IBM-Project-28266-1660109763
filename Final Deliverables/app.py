from flask import Flask,render_template, request, url_for, flash, redirect
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME= 815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tbl04832;PWD=MkD3JwscnFmh9wJm",'','')
print(conn)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')
@app.route("/register")
def register():
    return render_template('register.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM students WHERE name =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,name)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('login.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO students VALUES (?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, password)

      ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Data saved successfuly..")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/forgot")
def forgot():
    return render_template('forgot.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/wdashboard")
def wdashboard():
    return render_template('wdashboard.html')

@app.route("/a1dashboard")
def a1dashboard():
    return render_template('a1dashboard.html')

@app.route("/a2dashboard")
def a2dashboard():
    return render_template('a2dashboard.html')

@app.route("/a3dashboard")
def a3dashboard():
    return render_template('a3dashboard.html')

@app.route("/a4dashboard")
def a4dashboard():
    return render_template('a4dashboard.html')


@app.route("/wallet")
def wallet():
    return render_template('wallet.html')

@app.route("/expenses")
def expenses():
    return render_template('expenses.html')

@app.route("/e1expenses")
def e1expenses():
    return render_template('e1expenses.html')

@app.route("/e2expenses")
def e2expenses():
    return render_template('e2expenses.html')

@app.route("/e3expenses")
def e3expenses():
    return render_template('e3expenses.html')

@app.route("/e4expenses")
def e4expenses():
    return render_template('e4expenses.html')


@app.route("/email")
def email():
    return render_template('email.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')
