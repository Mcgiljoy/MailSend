# 웹크롤링 프로젝트
# https://h-glacier.tistory.com/

import datetime

import requests as requests
from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import json


# now = datetime.datetime.now()
# nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

# print("\n       ※ Python Webcrawling Project 1 ※ \n ")
# print('   환영합니다, ' + nowDate)
# print('      오늘의 주요 정보를 요약해 드리겠습니다.\n')
#
# # 오늘의 날씨
# print('  ○>> #오늘의 #날씨 #요약 \n')
# webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
# soup = BeautifulSoup(webpage, 'html.parser')
#
# temps = soup.find('div', "temperature_text")
# print("temps", temps.get_text())
# cast = soup.find('p', "celsius")
# print('--> 서울 날씨 : ', temps.get_text(), '℃', cast.get_text())
# print('--> 서울 날씨 : ', temps.get_text())

# 파일로 저장하기
f = open("smartstore.csv", 'w')
f.write("상호" + "," + "E-Mail" + "\n")

# 스마트스토어 목록

# webpage=requests.get('https://search.shopping.naver.com/search/all?origQuery=%EC%8A%A4%ED%86%A0%EC%96%B4&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%8A%A4%ED%86%A0%EC%96%B4&sort=rel&timestamp=&viewType=list')
# soup = Soup(webpage.text, 'html.parser')
for i in range(1, 100):
    webpage = urllib.request.urlopen('https://search.shopping.naver.com/search/all?origQuery=%EC%8A%A4%ED%86%A0%EC%96%B4&pagingIndex=' + str(i) + '&pagingSize=40&productSet=total&query=%EC%8A%A4%ED%86%A0%EC%96%B4&sort=rel&timestamp=&viewType=list').read()
    # print('-------------------------------------------------------')
    # print(webpage)

    # print('-------------------------------------------------------')


    soup = BeautifulSoup(webpage, 'html.parser')
    # print('soup 시작 -------------------------------------------------------')


    # Json 형태의 정보 가져오기
    scriptTag = soup.find('script', id='__NEXT_DATA__').get_text()
    # print('scriptTag 시작-----------------------------------')
    # print(scriptTag)
    # print('scriptTag 끝-----------------------------------')

    # Json 파싱
    # jsonMall = json.dumps(scriptTag, indent=4, sort_keys=True)
    # print('jsonMall 시작-----------------------------------')
    # print(jsonMall)
    # jsonObject로 담음
    jsonObject = json.loads(scriptTag)
    # print(jsonObject)
    # Product List를 가져온다.
    # props = jsonObject.get("props")
    # print("props : ", props)
    # pageProps = props.get("pageProps")
    # print("pageProps : ", pageProps)
    prodList = jsonObject.get("props").get("pageProps").get("initialState").get("products").get("list")
    # print("prodList : ", prodList)



    for prod in prodList:
        item = prod.get("item")
        mallProductUrl = str(item.get("mallProductUrl"))
        # print("mallProductUrl : ", mallProductUrl)
        # smartstore 인 경우 상세 주소로 이동한다.
        if(mallProductUrl.find("smartstore") > 0) :
            smartStorePage = urllib.request.urlopen(mallProductUrl)
            smartStoreSoup = BeautifulSoup(smartStorePage, 'html.parser')
            # print("smartStoreSoup : ", smartStoreSoup)
            scriptTags = smartStoreSoup.find_all('script')
            # id='_10PxysFyMd')
            for scriptTag in scriptTags:
                strScript = scriptTag.getText()
                if(strScript.find("chrgrEmail") > 0):
                    print("/////////////////////////////////////////////")
                    print("strScript : ", strScript)
                    # print("Index : ", strScript.find("="))
                    # print("Length : ", len(strScript))
                    # 상호 가져오기
                    strChrgr = strScript[strScript.find("representName") - 1: len(strScript)]
                    # print("strChrgr : ", strChrgr)
                    strRepresentName = strChrgr[strChrgr.find(":") + 2: strChrgr.find(",")-1]
                    print("representName : ", strRepresentName)


                    # Email 주소 가져오기
                    strChrgr = strScript[strScript.find("chrgrEmail") - 1: len(strScript)]
                    # print("strChrgr : ", strChrgr)
                    strEmail = strChrgr[strChrgr.find(":") + 2: strChrgr.find(",")-1]
                    print("strEmail : ", strEmail)

                    #파일에 쓴다
                    f.write(strRepresentName + "," + strEmail + "\n")
                    print("/////////////////////////////////////////////")
            # print("eMailTag : ", eMailTag)
            # break
        # strTest = 'https://m.smartstore.naver.com/main/products/5245895677'
        # print(strTest.find("smartstore"))

#파일 닫기
f.close()

# print("list : ", list)
# print('jsonMall 끝-----------------------------------')
# smartstore 정보 추리기


# webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8')
# soup = BeautifulSoup(webpage, 'html.parser')
# temps = soup.find('span',"todaytemp")
# cast = soup.find('p',"cast_txt")
# print('--> 대구 날씨 : ' , temps.get_text() , '℃' , cast.get_text())
#
# webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&tqi=UrZy%2Bsp0YidssAyki54ssssssKC-251380')
# soup = BeautifulSoup(webpage, 'html.parser')
# temps = soup.find('span',"todaytemp")
# cast = soup.find('p',"cast_txt")
# print('--> 부산 날씨 : ' , temps.get_text() , '℃' , cast.get_text())
# print('\n')