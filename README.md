 # 🐼 Pandas Exercises

This repository contains beginner-friendly exercises and examples for learning and practicing **data cleaning and manipulation using Python and pandas**.

## 📁 Folder Structure

pandas_exercises/
├── wrong_data.csv
├── wrong_data.py
├── cleaning_empty_cells.py
└── more_exercises_coming_soon.py

yaml
Copy
Edit

---

## 📌 Example: Removing Duplicates

### File: `wrong_data.csv`

Sample data with duplicate entries:

```csv
Name,Duration
Alice,30
Bob,45
Charlie,50
Alice,30
David,60
Bob,45
Eve,55
File: wrong_data.py
python
Copy
Edit
import pandas as pd

# Load the data
df = pd.read_csv("wrong_data.csv")

# Display original data
print("Original Data:")
print(df)

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Display cleaned data
print("\nAfter Removing Duplicates:")
print(df_cleaned)
✅ Topics Covered
Reading CSV files using pandas.read_csv

Fixing specific cell values using .loc[]

Converting columns to datetime using pd.to_datetime

Removing duplicate rows using .drop_duplicates()

Printing full DataFrames with .to_string()

🔧 Requirements
Python 3.10 or later

pandas

Install pandas if you haven't:

bash
Copy
Edit
pip install pandas
🚀 More exercises coming soon...
Handling missing values

Filtering rows

Aggregation and grouping

Merging datasets

Plotting with pandas & matplotlib

👨‍💻 Author
Ashok Dahal
📍 Nepal
