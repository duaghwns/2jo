import sqlite3 as sql

conn = sql.connect('./db/ssd.db')
cur = conn.cursor()