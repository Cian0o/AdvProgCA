import sqlite3
import pandas as pd

con = sqlite3.connect("mypharmaSQLite3.db")

curs = con.cursor()

Validator = pd.read_csv("/Users/cianwalker/Desktop/AdvProgCA/PharmaSocietyIreland.csv")

Validator.to_sql('pharmaValidate', con, if_exists='replace')

con.close
