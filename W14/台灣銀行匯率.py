#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import string
import html

result = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
result.encoding = 'UTF-8'
soup = BeautifulSoup(result.text, "html.parser")
data_name = soup.find_all('div', 'hidden-phone print_show')
data1 = soup.find_all('td', 'rate-content-cash text-right print_hide')
data2 = soup.find_all('td', 'rate-content-sight text-right print_hide')
#print(data1)
for i in range(len(data_name)):
    data_name[i] = str(data_name[i])
    #清除掉不需要的資料
    #要去除雙引號的話要輸入\"
    data_name[i] = data_name[i].replace('<div class=\"hidden-phone print_show\" style=\"text-indent:30px;\">', ''
)
    data_name[i] = data_name[i].replace('</div>', '')
    data_name[i] = html.unescape(data_name[i])
    data_name[i] = data_name[i].replace(' ', '')
    data_name[i].strip() # 移除空格
    #同理分別整理data1和data2
    data1[2*i] = str(data1[2*i])
    data1[2*i] = data1[2*i].replace('<td class=\"rate-content-cash text-right print_hide\" data-table=\"', '')
    data1[2*i] = data1[2*i].replace('</td>', '')
    data1[2*i+1] = str(data1[2*i+1])
    data1[2*i+1] = data1[2*i+1].replace('<td class=\"rate-content-cash text-right print_hide\" data-table=\"', '')
    data1[2*i+1] = data1[2*i+1].replace('</td>', '')

    data2[2*i] = str(data2[2*i])
    data2[2*i] = data2[2*i].replace('<td class=\"rate-content-sight text-right print_hide\" data-hide=\"phone\" data-table=\"', '')
    data2[2*i] = data2[2*i].replace('</td>', '')
    data2[2*i+1] = str(data2[2*i+1])
    data2[2*i+1] = data2[2*i+1].replace('<td class=\"rate-content-sight text-right print_hide\" data-hide=\"phone\" data-table=\"', '')
    data2[2*i+1] = data2[2*i+1].replace('</td>', '')
    
    print(data_name[i])
    print(data1[2*i])
    print(data1[2*i + 1])
    print(data2[2*i])
    print(data2[2*i + 1])
    


