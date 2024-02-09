#pip install beautifulsoup4
#抓取Yahoo奇摩科技新聞RSS網頁(XML網頁結構)

import requests
from bs4 import BeautifulSoup
yahoo_tech_news_xml = requests.get('https://tw.news.yahoo.com/rss/technology')
soup = BeautifulSoup(yahoo_tech_news_xml.text, "html.parser")  #解析XML網頁
type(soup) # 檢視網頁型別
for news in soup.findAll('item'): #抓取全部科技新聞標題的item標籤
    print(news.title.string) #抓取全部科技新聞標題的item標題


