import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import pandas as pd

# 크롤링 페이지 화면 안보이게 하기
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")

# 위에 창 조절 테스트를 위해 임시로 주석처리
driver = webdriver.Chrome('./chromedriver.exe')

driver.set_window_position(0,0)
driver.set_window_size(10,10)

# csv 파일 불러와서 리스트에 다시 담기
url = []
with open('test_url_list_1.csv', 'r',encoding='utf-8') as f:
    rdr = csv.reader(f)
    for i, line in enumerate(rdr):
        if i == 0:
            url = line

col_list = []

for i in url:
    driver = webdriver.Chrome('./chromedriver.exe')

    driver.set_window_position(0, 0)
    driver.set_window_size(10, 10)

    driver.get(i)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", attrs={"class" : "table700_border"})

    col_name = []
    col_value = []
    col = {}

    # 컬럼명, 데이터 가져오기
    col_name += table.find_all("td", attrs={"class" : "bg_grey"})
    col_value += table.find_all("td", attrs={"bgcolor" : "#ffffff"})

    # 데이터 get_text 해주고 공백제거
    for i in range(0, len(col_value)):
        col[col_name[i].get_text()] = col_value[i].get_text().strip().replace('\t', '')
        col_list.append(col)
        # list_col.append(col_value[i].get_text().strip().replace('\t', ''))

# 엑셀, csv로 저장
# print(col_list)
data = pd.DataFrame(col_list)
data.to_excel('table_test.xlsx')
data.to_csv('table_test.csv')
print(data.head())

# csv 형식으로 url 리스트 저장(코드가 길어서 객체지향 방식으로 작업하기 위해)
# with open('table_test.xlsx', 'w', newline='') as f:
#     wri = csv.writer(f)
#     wri.writerow(col_list)