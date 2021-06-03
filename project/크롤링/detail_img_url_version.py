import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import pandas as pd
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# 크롤링 페이지 설정
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver') # hojoon
# driver = webdriver.Chrome('./chromedriver.exe') # gayoung
driver.set_window_position(0, 0)
driver.set_window_size(10, 10)

u ='mainboard'
category = 'main'
page = 54

# csv 파일 불러와서 리스트에 다시 담기
url = []
with open(f'../크롤링_가영/{u}/{category}({page}).csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for i, line in enumerate(rdr):
        if i == 0:
            url = line

# test
url = url[0:3]
print(url)
print(len(url))

col_list = []
col_name = []
col_value = []
img_list = []

z = 0
for i in url:
    driver.get(i)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", attrs={"class" : "table700_border"})

    # 상세 이미지에 넣을 url 정보 리스트에 추가하기
    img_list.append(i)
    print(f'image url : {i}')

    # 컬럼명, 데이터 가져오기
    col_name.append(table.find_all("td", attrs={"class" : "bg_grey"}))
    col_value.append(table.find_all("td", attrs={"bgcolor" : "#ffffff"}))
    z+=1
    print(f'{len(url)-z} 번 남았습니다.')

print(len(col_name))
print(len(col_value))
print(len(img_list))

for i in range(len(col_name)):
    col = {}
    for j in range(len(col_name[i])):
        col[(col_name[i][j]).get_text()] = (col_value[i][j]).get_text().strip().replace('\t', '')
        col['상세이미지'] = img_list[i]

    col_list.append(col)
print(col_list)

# # 엑셀, csv로 저장
# data = pd.DataFrame(col_list)
# data.to_excel(f'{category}({page}).xlsx')
# print(data.head())
