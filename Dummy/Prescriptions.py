import sqlite3

con = sqlite3.connect("Prescriptions.db")

con.execute("create table Prescriptions (PatientPPSN TEXT PRIMARY KEY UNIQUE NOT NULL, PhysicianIMCN INTEGER UNIQUE NOT NULL,PatientName TEXT NOT NULL, PrescriptionContents TEXT NOT NULL, PrescriptionFreqDays INTEGER NOT NULL)")

print("Table created successfully")

con.close()