from selenium import webdriver

cpu = '873'
main_board = '875'
memory = '874'
graphic_card = '876'
ssd = '32617'
hdd = '877'
case = '879'
power = '880'
cooler = '887'

list_all = []

def f_get_list(item, page):
    url = 'http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=product&categorySeq='
    url += item
    url += '&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&productRegisterAreaSeq=4&categorySeq1=861&categorySeq2=876&categorySeq3=0&categorySeq4=0&selectOptionList[]=654&selectOptionList[]=655&selectOptionList[]=6857&selectOptionList[]=658&selectOptionList[]=657&selectOptionList[]=659&selectOptionList[]=6858&selectOptionList[]=665&selectOptionList[]=661&selectOptionList[]=663&selectOptionList[]=664&selectOptionList[]=6201&selectOptionList[]=6574&selectOptionList[]=680&selectOptionList[]=16333&selectOptionList[]=20550&selectOptionList[]=31689&selectOptionList[]=7599&selectOptionList[]=321985&selectOptionList[]=684&selectOptionList[]=666&selectOptionList[]=682&selectOptionList[]=32778&selectOptionList[]=37388&selectOptionList[]=32182&selectOptionList[]=321958&goodsCount=916&page='
    url += str(page)
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    list = driver.find_elements_by_xpath('/html/body/div/div[3]/div[2]/div[2]/table/tbody/tr')

    # 상품 번호만 추출해서 상세보기 url
    item_list = []

    for i in list:
        # print(i.get_attribute('class').split("_")[1])
        url = 'http://shop.danawa.com/pc/?controller=estimateDeal&methods=productInformation&productSeq='
        url += str( (i.get_attribute('class').split("_")[1]) )
        item_list.append(url)

    return item_list


# 아이템, 페이지 지정해서 상품 상세보기 링크 리스트에 저장 (다차원 배열)
for i in range(1, 26):
    list_all.append(f_get_list(memory, i))

# print(list_all)

length = len(list_all)

# print(length)

# 1차원 배열로 저장
list_url = []

for i in range(0, int(length)):
    for j in list_all[i]:
        list_url.append(j)

print(list_url)
print(len(list_url))