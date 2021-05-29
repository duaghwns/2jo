import csv
import selenium
import bs4

# csv 파일 불러와서 리스트에 다시 담기
url = []
with open('test_url_list.csv','r',encoding='utf-8') as f:
    rdr = csv.reader(f)
    for i,line in enumerate(rdr):
        if i==0:
            url = line

print(url)