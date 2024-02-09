#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import string

result = requests.get('https://okgo.tw/buty/kaohsiung.html')
print(result)
result.encoding = 'UTF-8'
soup = BeautifulSoup(result.text, "html.parser")
#print(soup)
#find no.1 game'name
place_list = soup.find(class_='nav_other box').find_all(class_='pic')
print('========================================================')
for i in range(len(place_list)):
    print(place_list[i])
    #再接著做一些處理，例如 再轉list方便使用
    #split處理(用空格切成list) https://www.runoob.com/python/att-string-split.html
    place_list[i] = str(place_list[i])
    place_list[i] = place_list[i].split('\"')
    
print('========================================================')
for place in place_list:
    print(place[3], place[7])

#善用type檢查型態




