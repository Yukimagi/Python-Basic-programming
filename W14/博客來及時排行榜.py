#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import string

result = requests.get('https://www.books.com.tw/web/sys_hourstop/home?loc=act_menu_0_001')
print(result)
result.encoding = 'UTF-8'
soup = BeautifulSoup(result.text, "html.parser")
#find no.1 game'name
book_list = soup.find(class_='mod_no clearfix').find_all('img')
print(book_list)

print('========================================================')
for i in range(10):
    #print(book_list[i])
    #再接著做一些處理，例如 再轉list方便使用
    #split處理(用空格切成list) https://www.runoob.com/python/att-string-split.html
    book_list[i] = str(book_list[i])
    book_list[i] = book_list[i].split('\"')
    
print('========================================================')
for i in range(10):
    print(i+1, ':\n\t', end='')
    print(book_list[i][1], book_list[i][5])

#善用type檢查型態'''




