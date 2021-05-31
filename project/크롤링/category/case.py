import sqlite3 as sql

conn = sql.connect('./db/case.db')
cur = conn.cursor()