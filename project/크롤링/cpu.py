from bs4 import BeautifulSoup
import os
import sqlite3 as sql
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

conn = sql.connect('./db/cpu.db')
cur = conn.cursor()

cur.execute('''
create table CPU (
cpu_id varchar2(20) primary key ,
cpu_name varchar2(100) not null ,
cpu_category varchar2(20) not null ,
cpu_price number default 0 ,
cpu_year date  ,
cpu_img varchar2(100)  ,
cpu_detail_img varchar2(100)  ,
cpu_maker varchar2(100)  ,
cpu_type varchar2(50)  ,
cpu_socket varchar2(50)  ,
cpu_mm number  ,
cpu_core number  ,
cpu_thread number  ,
cpu_clock float(20)  ,
cpu_bit number  ,
cpu_memory_bus number  ,
cpu_gpu varchar2(10)  ,
cpu_codename varchar2(50)  
)
''')



