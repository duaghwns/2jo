import sqlite3 as sql

conn = sql.connect('./db/gpu.db')
cur = conn.cursor()