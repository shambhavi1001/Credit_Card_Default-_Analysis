import pandas as pd
from sqlalchemy import create_engine

DB_NAME = "ccdb"
USER = "postgres"
PASSWORD = "root"
HOST = "localhost"
PORT = "5432"
# Create a connection engine
engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')

# Load CSV into a pandas DataFrame
csv_file = "payments.csv"  # Update with your CSV file path
df = pd.read_csv(csv_file)

# Define table name
table_name = "credit_default"

# Upload DataFrame to PostgreSQL (creates table if it doesn't exist)
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data uploaded successfully to table '{table_name}'")
