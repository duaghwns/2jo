import sqlite3 as sql

conn = sql.connect('./db/cool.db')
cur = conn.cursor()