import requests
res = requests.get("http://naver.com")
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
# print("응답코드 : ", res.status_code)   # 200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
# 
# res.raise_for_status()
# print("웹 스크래핑을 진행합니다.")
#
# 위의 두 뭉텅이 코드는 서로 같은 역할을 한다.

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)
    # 위 코드 실행으로 google의 HTML을 따와 .html의 파일로 만든다
