import sqlite3

con = sqlite3.connect("mypharma.db")

print("Database opened successfully")

con.execute("create table prescriptions (PatientPPSN TEXT PRIMARY KEY, PhysicianIMCN INTEGER,PatientName TEXT, PrescriptionContents TEXT, PrecriptionFreq INTEGER)")

print("Table created successfully")

con.close()
