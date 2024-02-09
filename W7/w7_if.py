#1.  if 條件分支：思考電影售票流程
#2.  for迴圈：應用、List type的for迴圈、Dictionary type的for迴圈
#3.  while迴圈：利用變數離開迴圈(Break)

# if----
age = 19
if (18 <= age):
    print('賣出電影票')

# if else----
age = 15
if (18 <= age):
    print('賣出電影票')
else:
    print('無法賣出電影票')

# if elif else-----
age = 70
if (60 <= age):
    print('票價為 1000 元')
elif (18 <= age):
    print('票價為 1800 元')
else:
    print('無法賣出電影票')

print('歡迎下次光臨')

# 更嚴謹的思考
age = 70
if (18 <= age <= 59):
    print('票價為 1800 元')
elif (60 <= age):
    print('票價為 1000 元')
else:
    print('無法賣出電影票')

print('歡迎下次光臨')

# 更多的條件-------
age = 65
pointcard = True   #有集點卡
count = 5  #集點5次優待
if (pointcard == True):
    if (count == 5):
        print('感謝您的長久惠顧，此次為1000元優惠價')

# 更多的條件，寫成1個if-------
age = 65
pointcard = True   #有集點卡
count = 5  #集點5次優待
if ((pointcard == True) and (count == 5)):
    print('感謝您的長久惠顧，此次為1000元優惠價')

# review all condictions...
# 18歲以下不賣票
# 18歲以上、59歲以下1800
# 60歲以上1000
if (age < 18):
    print('無法賣出電影票')
elif ((60 <= age) or ((pointcard == True) and (count == 5))):
    print('票價為 1000 元')
else:
    print('票價為 1800 元')

print('歡迎下次光臨')
