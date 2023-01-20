import pandas as pd
import sqlite3
con = sqlite3.connect("font.db")
sql = """
SELECT * FROM FONT

"""

df = pd.read_sql_query(sql,con)

print(df)

