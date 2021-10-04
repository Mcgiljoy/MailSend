# 웹크롤링 프로젝트
# https://h-glacier.tistory.com/

import datetime

import requests as requests
from bs4 import BeautifulSoup
import urllib.request
import requests
import re

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

# 스마트스토어 목록

# webpage=requests.get('https://search.shopping.naver.com/search/all?origQuery=%EC%8A%A4%ED%86%A0%EC%96%B4&pagingIndex=1&pagingSize=40&productSet=total&query=%EC%8A%A4%ED%86%A0%EC%96%B4&sort=rel&timestamp=&viewType=list')
# soup = Soup(webpage.text, 'html.parser')
webpage = urllib.request.urlopen('https://search.shopping.naver.com/search/all?origQuery=%EC%8A%A4%ED%86%A0%EC%96%B4&pagingIndex=4&pagingSize=40&productSet=total&query=%EC%8A%A4%ED%86%A0%EC%96%B4&sort=rel&timestamp=&viewType=list').read()
print('-------------------------------------------------------')
# print(webpage)

print('-------------------------------------------------------')


soup = BeautifulSoup(webpage, 'html.parser')
print('soup 시작 -------------------------------------------------------')

# print(soup)
print('soup 끝 -------------------------------------------------------')

# aTag = soup.find_all('a')
# temps = soup.find_all('a', {'class:basicList_mall__sbVax')
# , 'href')
# temps = soup.select('a.basicList_mall__sbVax')

# re.compile ("^smartstore"))
# print('aTag 시작 -------------------------------------------------------')
# aTag = soup.find_all('a')
#
# # print(aTag)
# print('aTag 끝 -------------------------------------------------------')
#
# print('aTag Select 시작 -------------------------------------------------------')
# aTagSel = soup.select('a')
#
# print(aTagSel)
# print('aTag Select 끝 -------------------------------------------------------')
#
# temps = soup.find_all('a', 'basicList_mall__sbVax')
# # temps = soup.select('a.basicList_mall__sbVax')
# print("smartstore a Tag :", temps)
# links = soup.select('a[href]')
# print("links :", links)
#
#
# for link in links:
#     # 특정 문자열을 포함한 링크를 가져온다.
#     # if re.search('^https:\/\/s\w+', link['href']):
#     if re.search('smartstore', link['href']):
#         # if re.compile("smartstore+ "):
#             print('smartstore Link', link['href'])

scriptTag = soup.find('script', id='__NEXT_DATA__')
print('scriptTag 시작-----------------------------------')
print(scriptTag)
print('scriptTag 끝-----------------------------------')

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
print('\n')