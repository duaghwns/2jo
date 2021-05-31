import sqlite3 as sql

conn = sql.connect('./db/hdd.db')
cur = conn.cursor()