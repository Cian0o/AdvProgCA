import sqlite3
import pandas as pd
import openpyxl

con = sqlite3.connect("mypharmaSQLite3.db")

print("Database opened successfully")

con.execute("create table prescriptions (PatientPPSN TEXT PRIMARY KEY, PhysicianIMCN INTEGER, PatientName TEXT, PrescriptionContents TEXT, PrecriptionFreq INTEGER)")

con.execute("create table physicians (PhysicianIMCN INTEGER PRIMARY KEY, SurgeryName TEXT, SurgeryPhone INTEGER, SurgeryAddress TEXT, SurgeryEmail EMAIL)")

con.execute("create table pharmacies (PSIReg INTEGER PRIMARY KEY, PharmaName TEXT, PharmaPhone INTEGER, PharmaAddress TEXT, PharmaEmail EMAIL)")

con.execute("create table pharmaValidate (Registration Number INTEGER PRIMARY KEY, Trading Name TEXT, Street1 TEXT, Street2 TEXT, Street3 TEXT, Town TEXT, County TEXT, RPB Owner TEXT, Eircode TEXT, Address1 TEXT)")

Validator = pd.read_excel(("/Users/cianwalker/Desktop/AdvProgCA/Extract of Pharmacies - PSI.xlsx"), skiprows=[0,1])

Validator.to_sql('pharmaValidate', con, if_exists='replace',index=False)

print("Table created successfully")

con.close()
