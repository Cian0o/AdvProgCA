from flask import *
import sqlite3

app = Flask(__name__,template_folder='/templates')


@app.route('/PhysicianPrescribe.html')
def prescribe():
    return render_template("PhysicianPrescribe.html")

@app.route('/PrescriptionSubmitted.html')
def submitted():
    return render_template("PrescriptionSubmitted.html")

@app.route('/PharmacyRetrieve.html')
def retrieve():
    return render_template("PharmacyRetrieve.html")

@app.route('/GetPrescription.html')
def getp():
    return render_template("GetPrescription.html")








if __name__ == "__main__":
    app.run(debug=True)