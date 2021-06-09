import random
# 성
firstName = '''김,이,박,최,정,강,조,윤,장,임,한,오,서,신,권,황,안,송,전,홍,류,고,문,량,손,
배,조,백,허,유,남,심,로,정,하,곽,성,차,주,우,구,신,임,전,민,유,류,나,진,지,
엄,채,원,천,방,공,강,현,함,변,염,양,변,여,추,노,도,소,신,석,선,설,마,길,주,
연,방,위,표,명,기,반,라,왕,금,옥,육,인,맹,제,모,장,탁,국,여,진,어,은,편,
남궁,독고,황보,제갈,사공,선우,서문,어금,망절,무본,황목,등정,장곡,강전'''

# 이름
lastName = '''성,영,상,재,종,정,동,용,승,경,
호,수,석,철,훈,현,진,영,환,식,
미,은,선,혜,지,덕,방,원,우,다,
희,숙,자,순,주,솔,별,국,민,일,
바,휴,왕,웅,범,대,익,중,낙,택,
권,황,율,률,술,걸,탁,백,룡,건,
애,난,소,분,아,매,말,녀,름,자,
란,임,라,충,슬,준,옥,찬,림,례,
필,규,한,예'''

# 쓸데없는거 제거
firstName = firstName.replace('\n','')
lastName = lastName.replace('\n','')
# 리스트로 나누기
firstName = firstName.split(',')
lastName = lastName.split(',')

# 이름 합치기
def name():
    return random.choice(firstName) + random.choice(lastName) + random.choice(lastName)

# 성별
sexx = ['M','F']
# 더미 컬럼
id = []
names = []
purpose = []
password = []
mail = []
sex = []
hp = []
bir = []

pur = ['GAME','WORD','STREAM','ETC']
def birth():
    rst =''
    year = random.randint(1950,2000)
    month = random.randint(1,12)
    day = random.randint(1,31)

    if month > 9:
        rst += str(year) +"-" + str(month)
    else:
        rst += str(year) +"-0" + str(month)
    if day > 9:
        rst += "-" +str(day)
    else:
        rst += "-0" + str(day)
    return rst

print(birth())

# 리스트에 넣기
for i in range(30):
    id.append('dummy00'+str(i))
    bir.append(birth())
    names.append(name())
    purpose.append(pur[random.randint(0,3)])
    password.append('0000')
    sex.append(random.choice(sexx))
    hp.append('010-1234-5678')

# 메일넣기
mailList = ['naver.com','google.com','nextit.com','github.com']
for i in id:
    mail.append(i+'@'+random.choice(mailList))

import sqlite3 as sql

conn = sql.connect('dummy.db')
cur = conn.cursor()

# 멤버 테이블 생성

cur.execute('''
create table MEMBER (
mem_id varchar2(20) primary key ,
mem_name varchar2(20) not null ,
mem_pass varchar2(20) not null ,
mem_mail varchar2(20) not null ,
mem_reg_date date default sysdate ,
mem_sex varchar2(20) not null ,
mem_bir date  ,
mem_zip varchar2(20) not null ,
mem_add1 varchar2(20) not null ,
mem_add2 varchar2(50)  ,
mem_hp varchar2(20) not null ,
mem_purpose varchar2(20) not null ,
mem_mileage number default 0 ,
mem_delete varchar2(20) default 'N'
)
''')

def insertId(j):
    a = "'" + id[j] + "' ,"
    a += "'" + bir[j] + "', "
    a+= "'" + names[j] +"', "
    a+= "'" + password[j] +"', "
    a+= "'" + mail[j] +"', "
    a+= "'" + purpose[j] +"', "
    a+= "'" + sex[j] +"', "
    a+= "'" + hp[j] +"',"
    a+= "000000, 'asdf','asdf'"
    return a

def colm(i):
    columnList = ''
    columnList +=  "insert into member (mem_id, mem_bir ,mem_name, mem_pass, mem_mail, mem_purpose, mem_sex, mem_hp, mem_zip, mem_add1, mem_add2) " \
                   "values (" + insertId(i) + ") "
    return columnList


for i in range(len(id)):
    cur.execute(colm(i))

conn.commit()
conn.close()