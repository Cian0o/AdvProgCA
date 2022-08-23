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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mypharmaSQLA.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

# db.mypharma.init_app(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prescriptions.sqlite3'
# app.config['SECRET_KEY'] = "secret key"


class mypharma(db.Model):
    __tablename__ = "prescriptions"

    patientppsn = db.Column(db.String, primary_key=True)
    physicianimcn = db.Column(db.Integer(), unique=True)
    patientname = db.Column(db.String())
    prescription = db.Column(db.String())
    presfreq = db.Column(db.Integer())

    def __init__(self, patientppsn, physicianimcn, patientname, prescriptioncont, prescfreq):
        self.patientppsn = patientppsn
        self.physicianimcn = physicianimcn
        self.patientname = patientname
        self.prescriptioncont = prescriptioncont
        self.prescfreq = prescfreq

    def __repr__(self):
        return f"{self.patientppsn}:{self.physicianimcn}{self.patientname}:{self.prescriptioncont}{self.prescfreq}"

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mypharma.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mypharma.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.Model.init_app(app)



@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/PhysicianRegister.html')
def regdoc():
    return render_template("PhysicianRegister.html")

@app.route('/PharmacyRegister.html')
def regchem():
    return render_template("PharmacyRegister.html")

@app.route('/ViewPrescription.html')
def getpresc():
    return render_template("ViewPrescription.html")

@app.route('/GetPrescription')
def GetPrescription():
    return render_template('ViewPrescription.html')

@app.route('/GetPrescription2Ammend.html')
def getpresc2():
    return render_template("GetPrescription2Ammend.html")

@app.route('/PrescriptionSubmitted.html')
def submitted():
    return render_template("PrescriptionSubmitted.html")

@app.route('/successPresc.html')
def success():
    return render_template("successPresc.html")

@app.route('/PhysicianPrescribe.html')
def submit():
    return render_template("PhysicianPrescribe.html")

@app.route('/prescribe', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('PhysicianPrescribe.html')

    if request.method == 'POST':
        patientppsn = request.form['patientppsn']
        physicianimcn = request.form['physicianimcn']
        patientname = request.form['patientname']
        prescriptioncont = request.form['prescriptioncont']
        prescfreq = request.form['prescfreq']
        prescription = mypharma(patientppsn=patientppsn, physicianimcn=physicianimcn, patientname=patientname, prescriptioncont=prescriptioncont,prescfreq=prescfreq)
        db.session.add(prescription)
        db.session.commit()
        return redirect('/successPresc.html')

@app.route('/PharmacyRetrieve.html')
def PharmacyRetrieve():
    return render_template("PharmacyRetrieve.html")

@app.route('/RetrievePrescription')
def RetrievePrescription(patientppsn):
    prescription = mypharma.query.filter_by(patientppsn=id).first()
    if prescription:
        return render_template('data.html', prescription = prescription)
    return f"Patient with PPS ={patientppsn} Doens't exist"

app.run(host='localhost', port=5000)






# @app.route('/savedetails', methods=["POST", "GET"])
# def savedetails():
#     msg = "msg"
#     if request.method == "POST":
#         try:
#             PatientPPSN = request.form["PatientPPSN"]
#             PhysicianIMCN = request.form["PhysicianIMCN"]
#             PatientName = request.form["PatientName"]
#             PrescriptionContents = request.form["PrescriptionContents"]
#             PrecriptionFreq = request.form["PrecriptionFreq"]
#             with sqlite3.connect("mypharma.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT into prescriptions (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?,?,?, ?, ?)", (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
#                 con.commit()
#                 msg = "Prescription successfully Added"
#         except:
#             con.rollback()
#             msg = "We can not add the prescription"
#         finally:
#             return render_template("successPresc.html", msg=msg)
#             con.close()



@app.route('/PhysicianAmmend.html')
def ammend():
    return render_template("PhysicianAmmend.html")

@app.route('/PharmacyRetrieve.html')
def retrieve():
    return render_template("PharmacyRetrieve.html")

# #Banked Retrieve:
# @app.route('/view')
# def view():
#     con = sqlite3.connect("mypharma.db")
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("select * from prescriptions")
#     rows = cur.fetchall()
#     return render_template("successPresc.html", rows=rows)



# @app.route('/view')
# def view():
#     PatientPPSN = request.form["PatientPPSN"]
#     con = sqlite3.connect("mypharma.db")
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("select * from prescriptions where PatientPPSN = ?", PatientPPSN)
#     rows = cur.fetchall()
#     return render_template("successPresc.html", rows=rows)

# @app.route('/view', methods=["GET"])
# def deleterecord():
#     id = request.form["id"]
#     with sqlite3.connect("employee.db") as con:
#         try:
#             cur = con.cursor()
#             cur.execute("delete from Employees where id = ?", id)
#             msg = "record successfully deleted"
#         except:
#             msg = "can't be deleted"
#         finally:
#             return render_template("delete record.html", msg=msg)











# @app.route('/GetPrescription')
# def showpresc():
#     return render_template("ViewPrescription.html")

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

# @app.route('/PhysicianPrescribe', methods = ["POST", "GET"])
# def PhysicianPrescribe():
#     msg = "msg"
#     # con = sqlite3.connect('prescriptions.db')
#     if request.method == "POST":
#         try:
#             PatientPPSN = request.form["PatientPPSN"]
#             PhysicianIMCN = request.form["PhysicianIMCN"]
#             PatientName = request.form["PatientName"]
#             PrescriptionContents = request.form["PrescriptionContents"]
#             PrecriptionFreq = request.form["PrecriptionFreq"]
#             with sqlite3.connect("prescriptions.db") as con:
#                 cur = con.cursor()
#                 cur.execute("INSERT  into prescriptions (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?, ?, ?, ?, ?)" , (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
#                 con.commit
#                 msg = "Prescription Submitted"
#         except:
#             con.rollback()
#             msg = "We cannot add to list"
#         finally:
#             return render_template("ViewPrescription.html", msg = msg)
#             con.close()

# @app.route("/PhysicianPrescribe.html",methods=['POST'])
# def PhysicianPrescribe():
#     # if request.method=='POST':
#     PatientPPSN=request.form.get('PatientPPSN')
#     PhysicianIMCN=request.form.get('PhysicianIMCN')
#     PatientName = request.form.get('PatientName')
#     PrescriptionContents = request.form.get('PrescriptionContents')
#     PrecriptionFreq = request.form.get('PrecriptionFreq')
#     con=sqlite3.connect("prescriptions.db")
#     cur=con.cursor()
#     cur.execute("insert into prescriptions(PatientPPSN,PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?,?,?,?,?)",(PatientPPSN,PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
#     con.commit()
#     flash('Prescription Submitted','success')
#         # return redirect(url_for("ViewPrescription.html"))
#     return render_template("ViewPrescription.html")




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
#             return render_template("ViewPrescription.html", msg=msg)
#             con.close()






# @app.route('/ViewPrescription.html')
# def fetch():
#     con = sqlite3.connect("venv/Prescriptions.db")
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.execute("select * from Prescriptions")
#     rows = cur.fetchall()
#     return render_template("ViewPrescription.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True, host="localhost")






