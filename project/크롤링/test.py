import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import bs4

# 크롤링 페이지 화면 안보이게 하기
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")

# 위에 창 조절 테스트를 위해 임시로 주석처리
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=opt)
driver = webdriver.Chrome('./chromedriver')

driver.set_window_position(0,0)
driver.set_window_size(10,10)

# csv 파일 불러와서 리스트에 다시 담기
url = []
with open('test_url_list.csv','r',encoding='utf-8') as f:
    rdr = csv.reader(f)
    for i,line in enumerate(rdr):
        if i==0:
            url = line

print(url)

def table():
    driver.get()