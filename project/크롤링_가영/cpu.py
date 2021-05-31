from bs4 import BeautifulSoup
import selenium
import os
import random
import sqlite3 as sql

conn = sql.connect('./db/cpu.db')
cur = conn.cursor()

