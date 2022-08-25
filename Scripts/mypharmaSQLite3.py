import sqlite3

con = sqlite3.connect("mypharmaSQLite3.db")

print("Database opened successfully")

con.execute("create table prescriptions (PatientPPSN TEXT PRIMARY KEY, PhysicianIMCN INTEGER, PatientName TEXT, PrescriptionContents TEXT, PrecriptionFreq INTEGER)")

con.execute("create table physicians (PhysicianIMCN INTEGER PRIMARY KEY, SurgeryName TEXT, SurgeryPhone INTEGER, SurgeryAddress TEXT, SurgeryEmail EMAIL)")

con.execute("create table pharmacies (PSIReg INTEGER PRIMARY KEY, PharmaName TEXT, PharmaPhone INTEGER, PharmaAddress TEXT, PharmaEmail EMAIL)")


print("Table created successfully")

con.close()
