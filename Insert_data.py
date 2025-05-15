# import sqlite3

# # Connect to SQLite database (or create if it doesn't exist)
# conn = sqlite3.connect("indian_banks.db")
# cursor = conn.cursor()

# # Create the tables
# cursor.executescript("""
# DROP TABLE IF EXISTS banks;
# DROP TABLE IF EXISTS branches;
# DROP VIEW IF EXISTS bank_branches;

# CREATE TABLE banks (
#     name TEXT,
#     id INTEGER PRIMARY KEY
# );

# CREATE TABLE branches (
#     ifsc TEXT PRIMARY KEY,
#     bank_id INTEGER,
#     branch TEXT,
#     address TEXT,
#     city TEXT,
#     district TEXT,
#     state TEXT,
#     FOREIGN KEY (bank_id) REFERENCES banks(id)
# );

# CREATE VIEW bank_branches AS
# SELECT
#     branches.ifsc,
#     branches.bank_id,
#     branches.branch,
#     branches.address,
#     branches.city,
#     branches.district,
#     branches.state,
#     banks.name AS bank_name
# FROM branches
# JOIN banks ON branches.bank_id = banks.id;
# """)

# conn.commit()

# import sqlite3
# import pandas as pd
# # Connect to SQLite database (or create if it doesn't exist)
# conn = sqlite3.connect("indian_banks.db")
# cursor = conn.cursor()



# # Load the CSV
# df = pd.read_csv("bank_branches.csv")

# # Separate bank and branch data
# banks_df = df[['bank_id', 'bank_name']].drop_duplicates().rename(columns={'bank_name': 'name', 'bank_id': 'id'})
# branches_df = df.drop(columns=['bank_name'])

# # Insert into banks table
# banks_df.to_sql('banks', conn, if_exists='append', index=False)

# # Insert into branches table
# branches_df.to_sql('branches', conn, if_exists='append', index=False)

# conn.commit()


# TESTING IT INSERT WORKED
import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("indian_banks.db")
cursor = conn.cursor()
# Fetch data from the view
cursor.execute("SELECT * FROM branches WHERE ifsc = 'ABHY0065001';")
for row in cursor.fetchall():
    print(row)
