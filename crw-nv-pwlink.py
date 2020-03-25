import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus

# 타겟 URL을 읽어서 HTML를 받아온다:
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

searchkeywords = input("키워드를 입력하세요: ")
url = f"https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={quote_plus(searchkeywords)}"

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

plName = soup.select("#power_link_body > ul > li.lst > div > a")
plDescription = soup.select("#power_link_body > ul > li.lst > div > div.ad_dsc > p")

for item in zip(plName, plDescription):
    result = {"제목": [item[0].text.strip()], "문안": [item[1].text.strip()]}

db = pd.DataFrame(result)
db.to_csv('excel_test.csv', mode='w', encoding='euc-kr')
