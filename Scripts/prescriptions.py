import sqlite3

con = sqlite3.connect("prescriptions.db")

c = con.cursor()

# con.execute("create table prescriptions (PatientPPSN TEXT PRIMARY KEY UNIQUE NOT NULL, PhysicianIMCN INTEGER UNIQUE NOT NULL,PatientName TEXT NOT NULL, PrescriptionContents TEXT NOT NULL, PrescriptionFreqDays INTEGER NOT NULL)")

c.execute("""CREATE TABLE prescriptions ( 
    PatientPPSN TEXT PRIMARY KEY UNIQUE NOT NULL, 
    PhysicianIMCN INTEGER UNIQUE NOT NULL,
    PatientName TEXT NOT NULL, 
    PrescriptionContents TEXT NOT NULL, 
    PrescriptionFreqDays INTEGER NOT NULL
)""")

con.commit()

print("Table created successfully")

con.close()