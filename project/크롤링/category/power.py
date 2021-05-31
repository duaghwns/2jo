import sqlite3 as sql

conn = sql.connect('./db/power.db')
cur = conn.cursor()