# Credit Card Default Analysis - Power BI Dashboard

This project is focused on analyzing credit card default data and building an interactive dashboard using Power BI. The goal is to understand key metrics like default rate, credit utilization, and the impact of education levels on defaults.

---

## 📊 Dashboard Overview

The Power BI dashboard visualizes:
- Total Customers
- Number of Defaulters
- Default Rate %
- Credit Utilization %
- Default Payment Distribution
- Default vs Non-Default Customers
- Default Rate by Education Level

---

## 🔄 Data Pipeline

### 1. Data Source
- **Dataset**: Credit Card Default dataset downloaded from [Kaggle](https://www.kaggle.com/).
- **Format**: CSV file

### 2. Upload to PostgreSQL
- Used a Python script `upload.py` to upload the CSV into a PostgreSQL database.
- **Table Name**: `credit_card`

### 3. Data Cleaning
- A Jupyter Notebook was created to load the data from PostgreSQL.
- Performed necessary data cleaning and transformation.
- Cleaned data was saved:
  - Back into PostgreSQL in a new table named `credit_card_transformed`
  - Exported to a new CSV file `credit_card_transformed.csv` for optional use

### 4. Power BI Integration
- Power BI was connected to the PostgreSQL database.
- Imported the `credit_card_transformed` table.
- Created interactive visualizations and filters to analyze the data efficiently.

---