import sqlite3
import pandas as pd

# Step 1. Load data file
df = pd.read_csv('data.csv')

# Step 2. Data Clean Up
df.columns = df.columns.str.strip()

# Step 3. Create/connect to a SQLite database
connection = sqlite3.connect('spotify_database.db')

# Step 4. Load data file to SQLite
df.to_sql('spotify_analytics', connection, if_exists= 'replace')

# Step 5. Close connection
connection.close()