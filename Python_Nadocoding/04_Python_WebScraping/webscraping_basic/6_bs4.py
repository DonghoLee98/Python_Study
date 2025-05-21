# PIP 모듈 설치
# pip install beautifulsoup4    # web scrapping에 사용
# pip install lxml              # scrap된 내용을 Parsing 하는 데에 사용

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

# 가져온 정보들이 lxml을 통해 파싱되고, BeautifulSoup로 객체화 되어 soup 변수에 저장된다
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.div)         # soup 객체에서 처음 발견되는 div element를 출력
# print(soup.div.attrs)   # div element의 속성 정보를 출력
# print(soup.div["id"])   # div element의 속성 '값' 정보를 출력
# 위의 내용은 해당 페이지에 대한 이해가 높을 때... 유용

# find("~1", "~2") 에서 ~1은 태그, ~2는 attribute 이다. ~1을 생략하면 attr만으로 찾는다.
# print(soup.find("div", attrs={"class":"Footer__footer--gvFec"}))
# print(soup.find(attrs={"class":"Footer__footer--gvFec"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1)

# https://www.youtube.com/watch?v=yQ20jZwDjTE&list=PLMsa_0kAjjrd8hYYCwbAuDsXZmHpqHvlV&index=6
# 1 18 30
