import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
# headers, from https://www.whatismybrowser.com/detect/what-is-my-user-agent/

res = requests.get(url, headers=headers)

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)