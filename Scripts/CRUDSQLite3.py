from flask import *
import sqlite3





app = Flask(__name__,template_folder='templates', static_folder= 'templates/static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/PhysicianPrescribe.html')
def submit():
    return render_template("PhysicianPrescribe.html")

@app.route('/prescribe', methods=["POST", "GET"])
def savedetails():
    msg = "msg"
    if request.method == "POST":
        try:
            PatientPPSN = request.form["PatientPPSN"]
            PhysicianIMCN = request.form["PhysicianIMCN"]
            PatientName = request.form["PatientName"]
            PrescriptionContents = request.form["PrescriptionContents"]
            PrecriptionFreq = request.form["PrecriptionFreq"]
            with sqlite3.connect("mypharmaSQLite3.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into prescriptions (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?,?,?, ?, ?)", (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
                con.commit()
                msg = "Prescription successfully Added"
        except:
            con.rollback()
            msg = "We can not add the prescription"
        finally:
            return render_template("successPresc.html", msg=msg)
            con.close()


@app.route('/successPresc.html')
def success():
    return render_template("successPresc.html")

@app.route('/ViewPrescription.html')
def ViewPrescription():
    return render_template("ViewPrescription.html")

@app.route('/PharmacyRetrieve.html')
def PharmacyRetrieve():
    return render_template("PharmacyRetrieve.html")

@app.route('/ViewRetPrescription')
def ViewRetPrescription():
    con = sqlite3.connect("mypharmaSQLite3.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from prescriptions")
    rows = cur.fetchall()
    return render_template("ViewRetPrescription.html", rows=rows)

@app.route('/PhysicianRegister.html')
def regdoc():
    return render_template("PhysicianRegister.html")


@app.route('/GPReg', methods=["POST", "GET"])
def GPReg():
    msg = "msg"
    if request.method == "POST":
        try:
            PhysicianIMCN = request.form["PhysicianIMCN"]
            SurgeryName = request.form["SurgeryName"]
            SurgeryPhone = request.form["SurgeryPhone"]
            SurgeryAddress = request.form["SurgeryAddress"]
            SurgeryEmail = request.form["SurgeryEmail"]
            with sqlite3.connect("mypharmaSQLite3.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into physicians (PhysicianIMCN, SurgeryName, SurgeryPhone, SurgeryAddress, SurgeryEmail) values (?,?,?, ?, ?)", (PhysicianIMCN, SurgeryName, SurgeryPhone, SurgeryAddress, SurgeryEmail))
                con.commit()
                msg = "Surgery/Physician successfully Added"
        except:
            con.rollback()
            msg = "We can not add the Surgery/Physician"
        finally:
            return render_template("successRegGP.html", msg=msg)
            con.close()

@app.route('/PharmacyRegister.html')
def regchem():
    return render_template("PharmacyRegister.html")

@app.route('/PharmaReg', methods=["POST", "GET"])
def PharmaReg():
    msg = "msg"
    if request.method == "POST":
        try:
            PSIReg = request.form["PSIReg"]
            PharmaName = request.form["PharmaName"]
            PharmaPhone = request.form["PharmaPhone"]
            PharmaAddress = request.form["PharmaAddress"]
            PharmaEmail = request.form["PharmaEmail"]
            with sqlite3.connect("mypharmaSQLite3.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into pharmacies (PSIReg, PharmaName, PharmaPhone, PharmaAddress, PharmaEmail) values (?,?,?, ?, ?)", (PSIReg, PharmaName, PharmaPhone, PharmaAddress, PharmaEmail))
                con.commit()
                msg = "Pharmacy successfully registered"
        except:
            con.rollback()
            msg = "We can not register the Pharmacy"
        finally:
            return render_template("successRegPharm.html", msg=msg)
            con.close()


@app.route('/GetPrescription2Ammend.html')
def getpresc2():
    return render_template("GetPrescription2Ammend.html")

@app.route('/PrescriptionSubmitted.html')
def submitted():
    return render_template("PrescriptionSubmitted.html")
















@app.route('/PhysicianAmmend.html')
def ammend():
    return render_template("PhysicianAmmend.html")

@app.route('/PharmacyRetrieve.html')
def retrieve():
    return render_template("PharmacyRetrieve.html")

#Banked Retrieve:





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






