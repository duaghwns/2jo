import sqlite3 as sql

conn = sql.connect('./db/main.db')
cur = conn.cursor()