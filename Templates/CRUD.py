from flask import *
import sqlite3

app = Flask(__name__,template_folder='/Users/cianwalker/Desktop/AdvProgCA/Templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/PhysicianPrescribe.html')
def submit():
    return render_template("PhysicianPrescribe.html")

@app.route('/PhysicianAmmend.html')
def prescribe():
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

@app.route('/GetPrescription2Ammend.html')
def getpresc2():
    return render_template("GetPrescription2Ammend.html")

@app.route('/PrescriptionSubmitted.html')
def submitted():
    return render_template("PrescriptionSubmitted.html")




if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)






