#擷取網頁圖片
#pip3 install requests

import requests
#抓指定圖片網址
img_url='http://www.gotop.com.tw/Waweb2004/WawebImages/BookXL/AEL022200.jpg'
response= requests.get(img_url) 
f=open('C:\\Users\\user\\Downloads\\AEL022200.jpg','wb') #指定存放路徑
# 將response.content二進位內容寫入為D磁碟的bootstrap.jpg
f.write(response.content)  			
print('下載完畢')
f.close()
