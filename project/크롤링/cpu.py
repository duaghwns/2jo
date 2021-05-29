from bs4 import BeautifulSoup
import os
import sqlite3 as sql
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

conn = sql.connect('./db/cpu.db')
cur = conn.cursor()



