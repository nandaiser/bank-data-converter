import json
from openpyxl import Workbook
from collections import defaultdict

totals = defaultdict(float)
pemenang = {}

# List of biggest account numbers to find
biggest = [
    21020001467,
    21020001129,
    21020001676,
    21020001671,
    21020001266
]

with open("FEBRUARI.json") as f:
    data = json.load(f)

# Sum total saldo tabungan grouped by (PRODUK, MARKETING)
for row in data:
    key = (row["PRODUK"], row["MARKETING"])
    totals[key] += row["SALDO TABUNGAN"]

# Find winners (pemenang) based on NOACC
for row in data:
    if row["PRODUK"] == 1 and row["NOACC"] in biggest:
        nama = row.get(" NAMA") or row.get("NAMA")  # Handle spacing issue
        saldo = row.get("SALDO TABUNGAN")  # Corrected key
        pemenang[nama] = saldo

total_nasabah = defaultdict(int)
for row in data:
    key =(row["PRODUK"],row["MARKETING"])
    total_nasabah[key] += 1
         
        

# Write to Excel
wb = Workbook()
ws = wb.active
ws.title = "Rekap Total"

ws.append(["PRODUK", "MARKETING", "TOTAL SALDO"])
for (produk, marketing), total in totals.items():
    ws.append([produk, marketing, total])

sorted_pemenang = sorted(pemenang.items(), key=lambda x: x[1], reverse=True)

# Add winners to a new sheet (disorted paling tinggi)
ws2 = wb.create_sheet("Pemenang")
ws2.append(["NAMA", "SALDO TABUNGAN"])
for nama, saldo in sorted_pemenang:
    ws2.append([nama, saldo])
print("saved")
print (total_nasabah)
wb.save("feb_summary.xlsx")
