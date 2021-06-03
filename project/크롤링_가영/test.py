import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# 크롤링 페이지 화면 안보이게 하기
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")

# 위에 창 조절 테스트를 위해 임시로 주석처리
# driver = webdriver.Chrome('./chromedriver.exe')
# driver = webdriver.Chrome('./chromedriver_2')

driver.implicitly_wait(5)
time.sleep(5)

# driver = webdriver.Chrome('../크롤링/chromedriver') # hojoon

driver.set_window_position(0, 0)
driver.set_window_size(10, 10)

category = 'cooler'
page = 157

# csv 파일 불러와서 리스트에 다시 담기
url = []
with open(f'./{category}/{category}({page}).csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for i, line in enumerate(rdr):
        if i == 0:
            url = line

print(len(url))

col_list = []
col_name = []
col_value = []
# img_list = []
url_list = []

for i in url:
    driver.get(i)
    url_list.append(i)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    try:
        table = soup.find("table", attrs={"class" : "table700_border"})

        if table == None:
            table = soup.find("table", attrs={"class": "table700"})
    except Exception as e:
        print(e)

    # 이미지 가져오기
    # try:
    #     span = driver.find_element_by_class_name('prod_info_image')

    #     if span != None:
    #         img_list.append(span.find_element_by_tag_name('img').get_attribute('src'))
    # except Exception as e:
    #     img_list.append('')

    # 컬럼명, 데이터 가져오기
    col_name.append(table.find_all("td", attrs={"class" : "bg_grey"}))
    col_value.append(table.find_all("td", attrs={"bgcolor" : "#ffffff"}))

print(len(col_name))
print(len(col_value))
# print(len(img_list))
# print(col_name)
# print(col_value)
# print(img_list)

for i in range(len(col_name)):
    col = {}
    for j in range(len(col_name[i])):
        # print((col_name[i][j]).get_text())
        # print((col_value[i][j]).get_text().strip().replace('\t', ''))
        col[(col_name[i][j]).get_text()] = (col_value[i][j]).get_text().strip().replace('\t', '')
        # col['상세이미지'] = img_list[i]
        col['url'] = url_list[i]

    # print(col)
    col_list.append(col)

# print(col_list)

# 엑셀, csv로 저장
# print(col_list)
data = pd.DataFrame(col_list)
data.to_excel(f'{category}({page}).xlsx')
# # data.to_csv('table_test.csv')
print(data.head())
