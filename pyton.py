import sqlite3
db = sqlite3.connect("app.db")

db.execute("create if not exists table skills(name text, progress,)")
