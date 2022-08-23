import sqlite3

con = sqlite3.connect("mypharmaSQLite3.db")

print("Database opened successfully")

con.execute("create table prescriptions (priscid INTEGER PRIMARY KEY AUTOINCREMENT, PatientPPSN TEXT UNIQUE, PhysicianIMCN INTEGER,PatientName TEXT, PrescriptionContents TEXT, PrecriptionFreq INTEGER)")

print("Table created successfully")

con.close()
