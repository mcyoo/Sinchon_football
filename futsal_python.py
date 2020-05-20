# -*- coding: utf-8 -*-
#!/usr/sh
#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import datetime

URL_A = "https://share.siheung.go.kr/space/list.do?searchCategory=3&searchDetailCategory=38&searchCondition=title&pageIndex=3&key=206000&use_date=&space_no=&searchPositonDong=&searchReserve=&searchStartTime=&searchEndTime=&searchStartDate=&searchEndDate=&searchKeyword="
URL_B = "https://share.siheung.go.kr/space/list.do?searchCategory=3&searchDetailCategory=38&searchCondition=title&pageIndex=1&key=206000&use_date=&space_no=&searchPositonDong=&searchReserve=&searchStartTime=&searchEndTime=&searchStartDate=&searchEndDate=&searchKeyword="
URL_soccer = "https://share.siheung.go.kr/space/list.do?searchCategory=3&searchDetailCategory=35&searchCondition=title&pageIndex=1&key=201000&use_date=&space_no=&searchPositonDong=&searchReserve=&searchStartTime=&searchEndTime=&searchStartDate=&searchEndDate=&searchKeyword=#"

dayString = ["(월)","(화)","(수)","(목)","(금)","(토)","(일)"]
now = datetime.datetime.now()

def extract_futsal_num(html):
    area_list = []
    data = html.find("div",{"id":"photo_glist"})
    area = data.find_all("span")
    for i in area:
        i = i.get_text()
        area_list.append(i if i.find('해당동명') >= 0 else '')
    
    while '' in area_list:
        area_list.remove('')

    return area_list.index('해당동명 :신천동')

def extract_futsal_date(URL):

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    num = extract_futsal_num(soup)
    print(num)
    pagination = soup.find_all("div", {"class": "tooltip"})[num]
    date = pagination.get_text()
    date = date.split('\n')
    while '' in date:
        date.remove('')

    date = date[1:]
    get_date_format(date) #요일 덧붙이기
    return date

def get_date():

    futsal_date = []
    futsal_date.append(extract_futsal_date(URL_A))
    futsal_date.append(extract_futsal_date(URL_B))
    futsal_date.append(extract_futsal_date(URL_soccer))
    return futsal_date

def get_date_format(date):

    for i in range(0,len(date)):
        if date[i].find(str(now.year)) >= 0:
            date_temp = date[i].split('-')
            weekday = dayString[datetime.date(2020,int(date_temp[1]),int(date_temp[2])).weekday()]
            date[i] = '\n' + date[i] + weekday
