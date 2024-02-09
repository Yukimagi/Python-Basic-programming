#BeautifulSoup套件解析網頁的程式碼
#BeautifulSoup物件的建立
#pip3 install BeautifulSoup4 套件安裝

#取得網頁標題

import requests
from bs4 import BeautifulSoup   #由bs4模組內引用BeauifulSou套件
url='https://www.nuk.edu.tw/'   #國立高雄大學首頁
response=requests.get(url)
bs=BeautifulSoup(response.text, "html.parser")   #解析HTML文件的方法，傳回bs物件可解析網頁
print(bs.find('title'))                  #傳回網頁含<title>~</title>
print(bs.find('title').text)             #傳回網頁<title>標籤內的資料
print(bs.find('h1'))                     #傳回第一個符合<h1>資料
					 #若傳回None表示該網頁沒有<h1>標籤
