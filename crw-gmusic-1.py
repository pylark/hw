import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아온다:
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

url = "https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309"
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
data = requests.get(url,headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

singers = soup.select("#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis")
titles = soup.select("#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis")
ranks = soup.select("#body-content > div.newest-list > div > table > tbody > tr > td.number")

for item in zip(ranks, titles, singers) :
    print(item[0].text.strip().split('\n')[0], item[1].text.strip(), item[2].text.strip())
