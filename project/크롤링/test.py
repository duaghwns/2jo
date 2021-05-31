import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from bs4 import BeautifulSoup
import csv

# 크롤링 페이지 화면 안보이게 하기
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")

# 드라이버세팅
driver = webdriver.Chrome('./chromedriver')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
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
print(len(url))


test_data=[]


def start(index):
    driver.get(url[index])
    table = driver.find_elements_by_xpath('//*[@id="content"]/table[2]/tbody/tr/td')
    for i in table:
        test_data.append(i.text)

for i in range(1,len(url)):
    start(i)

print(test_data)
# with open('test_data.csv','w'):







