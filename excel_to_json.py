import pandas as pd
import openpyxl

xls = pd.read_excel("Test Bank Umum Milik NBP.xlsx", sheet_name= None, engine= "openpyxl")

for sheet_name, df in xls.items():
    df.to_json(f"{sheet_name}.json", orient= "records", indent= 4)