# 🐼 Pandas Exercises

This repository contains beginner-friendly exercises and examples for learning and practicing **data cleaning and manipulation using Python and pandas**.

## 📁 Files Included

- `wrong_data.csv` – Sample CSV file with duplicate data.
- `wrong_data.py` – Python script to read CSV, clean duplicates.
- `cleaning_empty_cells.py` – Example for handling missing values (coming soon).
- More exercises will be added progressively.

---

## 🧪 Example: Remove Duplicates

### 📄 wrong_data.csv

```csv
Name,Duration
Alice,30
Bob,45
Charlie,50
Alice,30
David,60
Bob,45
Eve,55
🐍 wrong_data.py
python
Copy
Edit
import pandas as pd

# Load CSV file
df = pd.read_csv("wrong_data.csv")

# Show original data
print("Original Data:")
print(df)

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Show cleaned data
print("\nAfter Removing Duplicates:")
print(df_cleaned)
✅ What You’ll Learn
How to load CSV files using pandas

Access and modify specific cells

Handle duplicate rows using .drop_duplicates()

Print full DataFrames using .to_string()

💻 Requirements
Python 3.10+

pandas

Install with pip:

 
pip install pandas
