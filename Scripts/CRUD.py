from flask import *
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
import sqlite3


# class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
#     Column: Callable  # Use the typing to tell the IDE what the type is.
#     String: Callable
#     Integer: Callable

# app = Flask(__name__, template_folder='/Users/cianwalker/Desktop/AdvProgCA/Scripts/Templates', static_folder='/Users/cianwalker/Desktop/AdvProgCA/Scripts/Static')

app = Flask(__name__,template_folder='templates', static_folder= 'templates/static')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prescriptions.sqlite3'
# app.config['SECRET_KEY'] = "secret key"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/PhysicianPrescribe.html')
def submit():
    return render_template("PhysicianPrescribe.html")

@app.route('/PhysicianAmmend.html')
def ammend():
    return render_template("PhysicianAmmend.html")

@app.route('/PharmacyRetrieve.html')
def retrieve():
    return render_template("PharmacyRetrieve.html")

@app.route('/PhysicianRegister.html')
def regdoc():
    return render_template("PhysicianRegister.html")

@app.route('/PharmacyRegister.html')
def regchem():
    return render_template("PharmacyRegister.html")

@app.route('/GetPrescription.html')
def getpresc():
    return render_template("GetPrescription.html")

# @app.route('/')
# def getpresc():
#     return render_template('GetPrescription.html', prescriptions=prescriptions.query.all())

@app.route('/GetPrescription2Ammend.html')
def getpresc2():
    return render_template("GetPrescription2Ammend.html")

@app.route('/PrescriptionSubmitted.html')
def submitted():
    return render_template("PrescriptionSubmitted.html")

# db = SQLAlchemy(app)
#
# class prescriptions(db.Model):
#     __tablename__ = "prescrptions"
#     PatientPPSN = db.Column(db.String, primary_key=True)
#     PhysicianIMCN = db.Column(db.Integer(10))
#     PatientName = db.Column(db.String(50))
#     PrescriptionContents = db.Column(db.String(200))
#     PrecriptionFreq = db.Column(db.Integer(2))
#
#     def __init__(self, PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq):
#         self.PatientPPSN = PatientPPSN
#         self.PhysicianIMCN = PhysicianIMCN
#         self.PatientName = PatientName
#         self.PrescriptionContents = PrescriptionContents
#         self.PrecriptionFreq = PrecriptionFreq
#
# @app.route('/PhysicianPrescribe', methods=['GET', 'POST'])
# def prescribe():
#     if request.method == 'POST':
#         if not request.form['PatientPPSN'] or not request.form['PhysicianIMCN'] or not request.form['PrescriptionContents'] or not request.form['PrecriptionFreq']:
#             flash('Please enter all the fields', 'error')
#         else:
#             employee = prescriptions(request.form['name'], request.form['salary'],
#                                  request.form['age'], request.form['pin'])
#
#             db.session.add(employee)
#             db.session.commit()
#             flash('Record was successfully added')
#             return redirect(url_for('list_employees'))
#     return render_template('add.html')

# @app.route('/PhysicianPrescribe.html', methods = ["POST", "GET"])
# def prescribe():
#     msg = "msg"
#     db = sqlite3.connect('prescriptions.db')
#     if request.method == "POST":
#         try:
#             PatientPPSN = request.form["PatientPPSN"]
#             PhysicianIMCN = request.form["PhysicianIMCN"]
#             PatientName = request.form["PatientName"]
#             PrescriptionContents = request.form["PrescriptionContents"]
#             PrecriptionFreq = request.form["PrecriptionFreq"]
#             with sqlite3.connect("Prescriptions.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT  into prescriptions (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?, ?, ?, ?, ?)" , (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
#                 con.commit
#                 msg = "Prescription Submitted"
#         finally:
#             return render_template("GetPrescription.html", msg = msg)
#             con.close()

@app.route("/PhysicianPrescribe.html",methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        PatientPPSN=request.form['PatientPPSN']
        PhysicianIMCN=request.form['PhysicianIMCN']
        PatientName = request.form['PatientName']
        PrescriptionContents = request.form['PrescriptionContents']
        PrecriptionFreq = request.form['PrecriptionFreq']
        con=sqlite3.connect("prescriptions.db")
        cur=con.cursor()
        cur.execute("insert into prescriptions(PatientPPSN,PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?,?,?,?,?)",(PatientPPSN,PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
        con.commit()
        flash('Prescription Submitted','success')
        return redirect(url_for("GetPrescription.html"))
    return render_template("GetPrescription.html")




# @app.route('/PhysicianPrescribe.html', methods = ['PUT'])
# def prescribe():
#     if request.method == 'PUT':
#         msg  = "msg"
#         try:
#             PatientPPSN = request.form["PatientPPSN"]
#             PhysicianIMCN = request.form["PhysicianIMCN"]
#             PatientName = request.form["PatientName"]
#             PrescriptionContents = request.form["PrescriptionContents"]
#             PrecriptionFreq = request.form["PrecriptionFreq"]
#             with sqlite3.connect("venv/Prescriptions.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT into Prescriptions (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?,?,?)", (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
#                 con.commit()
#                 msg = "Prescription successfully Added"
#         except:
#             con.rollback()
#             msg = "Prescription Could Not be Added!"
#         finally:
#             return render_template("GetPrescription.html", msg=msg)
#             con.close()






# @app.route('/GetPrescription.html')
# def fetch():
#     con = sqlite3.connect("venv/Prescriptions.db")
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("select * from Prescriptions")
#     rows = cur.fetchall()
#     return render_template("GetPrescription.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True, host="localhost")






