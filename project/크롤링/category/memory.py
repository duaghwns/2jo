import sqlite3 as sql

conn = sql.connect('./db/memory.db')
cur = conn.cursor()