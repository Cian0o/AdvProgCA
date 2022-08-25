from flask import *
import sqlite3

app = Flask(__name__, template_folder='/Users/cianwalker/Desktop/AdvProgCA/Templates', static_folder='/Users/cianwalker/Desktop/AdvProgCA/Static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/PhysicianPrescribe.html')
def submit():
    return render_template("PhysicianPrescribe.html")

@app.route('/PhysicianAmmendReq.html')
def ammend():
    return render_template("PhysicianAmmendReq.html")

@app.route('/PharmacyRetrieve.html')
def retrieve():
    return render_template("PharmacyRetrieve.html")

@app.route('/PhysicianRegister.html')
def regdoc():
    return render_template("PhysicianRegister.html")

@app.route('/PharmacyRegister.html')
def regchem():
    return render_template("PharmacyRegister.html")

@app.route('/ViewPrescription.html')
def getpresc():
    return render_template("ViewPrescription.html")

@app.route('/GetPrescription2Ammend.html')
def getpresc2():
    return render_template("GetPrescription2Ammend.html")

@app.route('/PrescriptionSubmitted.html')
def submitted():
    return render_template("PrescriptionSubmitted.html")

@app.route('/PhysicianPrescribe.html', methods = ['POST', 'GET'])
def prescribe():
    if request.method == 'POST':
        try:
            PatientPPSN = request.form["PatientPPSN"]
            PhysicianIMCN = request.form["PhysicianIMCN"]
            PatientName = request.form["PatientName"]
            PrescriptionContents = request.form["PrescriptionContents"]
            PrecriptionFreq = request.form["PrecriptionFreq"]
            with sqlite3.connect("Prescriptions.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Prescriptions (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq) values (?,?,?)", (PatientPPSN, PhysicianIMCN, PatientName, PrescriptionContents, PrecriptionFreq))
                con.commit()
                msg = "Prescription successfully Added"
        except:
            con.rollback()
            msg = "Prescription Could Not be Added!"
        finally:
            return render_template("ViewPrescription.html", msg=msg)
            con.close()




if __name__ == "__main__":
    app.run(debug=True, host="localhost")






