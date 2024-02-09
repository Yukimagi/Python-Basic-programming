#1.  if 條件分支：思考電影售票流程
#2.  for迴圈：應用、List type的for迴圈、Dictionary type的for迴圈
#3.  while迴圈：利用變數離開迴圈(Break)

# for in range
for c in range(5):
    print('重複執行')

word = '國立高雄大學'
for c in word:
    print(c)

# for in 資料集....String, List, Dict, Tuple, Set....
music_list = ['DEATH METAL', 'ROCK', 'ANIME', 'POP', 'AA', 'BB']
for music in music_list:
    print('now playing...' + music)

# for in Dict
menu = {'拉麵':500, '炒飯':430, '煎餃':210}
total = 0
for order in menu:
    print(order)
    print(menu[order] * 1.08)
    total = total + menu[order] * 1.08

print('總價為...', total)


# while (條件式):
# 重複執行的動作
counter = 0
while (counter < 5):
    print(counter)
    counter = counter + 1

# 無窮迴圈
counter = 0
while (counter < 5):
    print(counter)
	
# 無窮迴圈
while (True):
    print('Please press Ctrl-C to stop')

#利用break離開迴圈
while(True):
    print('揮拳')
    print('腳踢')
    break   #強迫離開迴圈
    print('必殺奧義')

#利用變數離開迴圈
power = 5
while(True):
    print('揮拳')
    print('腳踢')
    print('必殺奧義')
    power = power - 1
    if (power == 0):
        break

#利用List結束離開迴圈
#利用continue回到迴圈條件式判斷
family = ['ryu-ko', 'mako', 'satsuki']
for kid in family:
    print('早安!' + kid)
    print('起床')
    print('吃早餐')
    continue   #繼續重複迴圈，continue後的動作不執行
    print('出門上學')
