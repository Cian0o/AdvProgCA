import sqlite3

con = sqlite3.connect("Prescriptions.db")

con.execute("create table Prescriptions (PrescriptionID INTEGER PRIMARY KEY AUTOINCREMENT, PatientPPSN TEXT UNIQUE NOT NULL, PhysicianIMCN INTEGER UNIQUE NOT NULL, PrescriptionContents TEXT NOT NULL, PrescriptionFreqDays INTEGER NOT NULL)")

print("Table created successfully")

con.close()