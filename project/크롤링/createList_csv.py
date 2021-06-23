from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import csv
from webdriver_manager.chrome import ChromeDriverManager

# 크롤링 페이지 화면 안보이게 하기
opt = Options()
opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
opt.add_argument("--headless")

# 위에 창 조절 테스트를 위해 임시로 주석처리
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=opt)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.set_window_position(0,0)
driver.set_window_size(10,10)


# url 카테고리, 61번 라인에 key 값으로 활용
category = {'cpu':'873','memory':'874','main':'875','gpu':'876',"hdd":'877','case':'879','power':'880','cooler':'887','ssd':'32617'}


list_all = []

def f_get_list(item, page):
    url = 'http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=product&categorySeq='
    url += item
    url += '''&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30
    &attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0
    &ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3
    &categoryName=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&productRegisterAreaSeq=4
    &categorySeq1=861&categorySeq2=876&categorySeq3=0&categorySeq4=0&selectOptionList[]=654
    &selectOptionList[]=655&selectOptionList[]=6857&selectOptionList[]=658&selectOptionList[]=657
    &selectOptionList[]=659&selectOptionList[]=6858&selectOptionList[]=665&selectOptionList[]=661
    &selectOptionList[]=663&selectOptionList[]=664&selectOptionList[]=6201&selectOptionList[]=6574
    &selectOptionList[]=680&selectOptionList[]=16333&selectOptionList[]=20550&selectOptionList[]=31689
    &selectOptionList[]=7599&selectOptionList[]=321985&selectOptionList[]=684&selectOptionList[]=666
    &selectOptionList[]=682&selectOptionList[]=32778&selectOptionList[]=37388&selectOptionList[]=32182&selectOptionList[]=321958&goodsCount=916&page='''
    url += str(page)
    driver.get(url)


    list = driver.find_elements_by_xpath('/html/body/div/div[3]/div[2]/div[2]/table/tbody/tr')

    # 상품 번호만 추출해서 상세보기 url
    item_list = []

    for i in list:
        url = 'http://shop.danawa.com/pc/?controller=estimateDeal&methods=productInformation&productSeq='
        url += str( (i.get_attribute('class').split("_")[1]) )
        item_list.append(url)

    return item_list

# 검색할 페이지
searchPage = 35

# 아이템, 페이지 지정해서 상품 상세보기 링크 리스트에 저장 (다차원 배열)
for i in range(1, searchPage):
    list_all += f_get_list(category['gpu'], i)


# csv 형식으로 url 리스트 저장(코드가 길어서 객체지향 방식으로 작업하기 위해)
csv_title = 'test_url_list.csv'
with open(csv_title, 'w', newline='') as f:
    wri = csv.writer(f)
    wri.writerow(list_all)

print(csv_title+' 생성 완료')