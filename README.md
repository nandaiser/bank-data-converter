# 📊 Bank Data Converter

A Python-based utility for converting and processing banking tabulation data. This tool allows you to convert Excel (`.xlsx`) files to JSON and generate rekap summaries (grouped totals and top accounts) back to Excel — great for marketing or finance analysis.

---

## 🔁 Features

- Convert each Excel sheet into a separate `.json` file
- Read `.json` data and aggregate saldo per `PRODUK` and `MARKETING`
- Count number of customers (`nasabah`) per group
- Identify top accounts ("pemenang") based on balance
- Export clean Excel summaries with multiple sheets

---

## 📂 Folder Structure
bank-data-converter/
├── excel_to_json.py # Convert Excel to JSON
├── rekap_generator.py # Process JSON and export Excel summary
├── requirements.txt
├── README.md
├── LICENSE
└── data/
└── Test Bank.xlsx # Input files (not pushed)


---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```
🧠 What I Learned
Using pandas and openpyxl for file I/O

Grouping and aggregating data with defaultdict

Reading/writing structured data formats (JSON, Excel)

Structuring multi-step data pipelines

📌 Future Plans
Make file names dynamic (CLI args)

Add error handling and input validation

Build CLI or Web interface for non-technical users

🧑‍💻 Author
Muhammad Bagus Prasetyo
GitHub - @nandaiser

🪪 License
MIT License — see LICENSE for details.



