import math
#建一個使用者的dic
user={}

#建tuple關於個人資料建立(name,birthday,date)
print('請輸入姓名、生日')
n=input('姓名')
b=input('生日:yyyy/mm/dd(請依照此格式)')
key_t=(n,b)

#詢問使用者各項身體數值
print('請輸入您的年紀、身高、體重、工作狀況')
age=input('您的年紀是:')
height=float(input('您的身高(cm)是:'))
weight=float(input('您的體重(kg)是:'))
work=input('您的工作量是(輕度工作(0)/中度工作(1)/重度工作(2)):')
bmi=(weight)/(((height)/100)**2)

#將數據儲存到list
value=['年紀',age,'身高',height,'體重',weight,'工作狀況',work,'bmi',bmi]

#儲存到user{}
user[key_t]=value

#計算蛋白攝取量
if(int(age) < 18):
    protein=(weight *1.3)
elif(int(age) >= 18 and int(age) <= 70):
    protein=(weight *1.1)
elif(int(age) > 70):
    protein=(weight *1.2)

#計算熱量攝取量
if(bmi <= 18.5 and int(work) == 0):
      kcal=(weight *35)
elif(bmi <= 18.5 and int(work)==1):
        kcal=(weight *40)
elif(bmi <= 18.5 and int(work)==2):
        kcal=(weight *45)
elif(bmi >= 18.5 and bmi < 24.0 and int(work)==0):
        kcal=(weight *30)
elif(bmi >=18.5 and bmi <24.0 and int(work)==1):
        kcal=(weight *35)
elif(bmi >= 18.5 and bmi < 24.0 and int(work)==2):
        kcal=(weight *40)
elif(bmi >= 24.0 and int(work)==0):
      kcal=(weight *22.5)
elif(bmi >= 24.0 and int(work)==1):
      kcal=(weight *30)
elif(bmi >= 24.0 and int(work)==2):
    kcal=(weight *35)

#顯示使用者的每日蛋白質和熱量攝取量
print('建議您每日應攝取'+str(protein)+'公克的蛋白質，以及'+str(kcal)+'大卡的熱量哦')
print('------------------')
#顯示我的每日飲食建議量
print('請參考以下\n每日飲食建議量')
#使用變數，可幫助之後有其他大卡的數據可以直接修正
Kcal_1200=[1.5,3,1.5,3,2,4]
Kcal_1500=[2.5,4,1.5,3,2,4]
Kcal_1800=[3,5,1.5,3,2,5]
Kcal_2000=[3,6,1.5,4,3.5,6]
Kcal_2200=[3.5,6,1.5,4,3.5,6]
Kcal_2500=[4,7,1.5,5,4,7]
Kcal_2700=[4,8,2,5,4,8]
diet_tips={1200:Kcal_1200,1500:Kcal_1200,1800:Kcal_1800
           ,2000:Kcal_2000,2200:Kcal_2200,2500:Kcal_2500,2700:Kcal_2700}
if(kcal<=1200):
    i=1200
elif(kcal>1200 and kcal<=1500):
    i=1500
elif(kcal>1500 and kcal<=1800):
    i=1800
elif(kcal>1800 and kcal<=2000):
    i=2000
elif(kcal>2000 and kcal<=2200):
    i=2200
elif(kcal>2200 and kcal<=2500):
    i=2500
elif(kcal>2500 and kcal<=2700):
    i=2700
print(f'由於我是{kcal}大卡\n(因此我大約需要1800大卡):')
print('全榖雜糧類:'+diet_tips[i][0]+'份')
print('豆魚蛋肉類:'+diet_tips[i][1]+'份')
print('乳品類    :'+diet_tips[i][2]+'份')
print('蔬菜類    :'+diet_tips[i][3]+'份')
print('水果類    :'+diet_tips[i][4]+'份')
print('油脂類    :'+diet_tips[i][5]+'份')

print('-----------------')
print('以下為每日餐盤建議')
print('每天早晚一杯奶\n')
print('每餐水果拳頭大\n')
print('菜比水果多一點\n')
print('飯跟蔬菜一樣多\n')
print('豆魚蛋肉一掌心\n')
print('堅果種子一茶匙\n')
print('-----------------')
print('以下為我的食物組合:')
print('請選擇最適合的~')

print('3餐食物隨機組合:')
#list與set的使用(並同時做早餐的重新排序)
list_rice=['鍋貼(餐廳)','水餃(餐廳)']
set_rice=set(list_rice)
#測試update
set_rice.update(['白飯'])
set_rice.update(['紫米飯'])
set_rice.update(['五穀雜糧飯'])
list_rice=list(set_rice)
#print(list_rice) #測試是否隨機產生(是)

list_meat=['炒豬肉絲','煎魚','雞肉丁','丁香魚','肉丸','扁食','豆漿(餐廳)']
set_meat=set(list_meat)
list_meat=list(set_meat)

list_milk=['牛奶','羊奶','起司','優格','乳酪蛋糕']
set_milk=set(list_milk)
list_milk=list(set_milk)

list_veg=['炒高麗菜','燙地瓜葉','苦瓜鹹蛋','炒A菜','炒筍子','菜頭湯(餐廳)']
set_veg=set(list_veg)
list_veg=list(set_veg)

list_fruit=['蘋果','西瓜','奇異果','香蕉','蓮霧','水蜜桃']
set_fruit=set(list_fruit)
list_fruit=list(set_fruit)

list_oil=['酪梨','堅果','橄欖油','玄米油']
set_oil=set(list_oil)
list_oil=list(set_oil)

kcal_avg=kcal/3

tuple_breakfast=('早餐',f'{kcal_avg}卡')
tuple_lunch=('中餐',f'{kcal_avg}卡')
tuple_dinner=('晚餐',f'{kcal_avg}卡')

dict_meals={}

dict_meals[tuple_breakfast]=(list_rice[0],list_meat[1],list_milk[2],list_veg[0],list_fruit[1],list_oil[2])
print('早餐:'+str(dict_meals[tuple_breakfast]))
setb={list_rice[0],list_meat[1],list_milk[2],list_veg[0],list_fruit[1],list_oil[2]}

#再次重新排序(中餐)
set_rice=set(list_rice)
list_rice=list(set_rice)

set_meat=set(list_meat)
list_meat=list(set_meat)

set_milk=set(list_milk)
list_milk=list(set_milk)

set_veg=set(list_veg)
list_veg=list(set_veg)

set_fruit=set(list_fruit)
list_fruit=list(set_fruit)

set_oil=set(list_oil)
list_oil=list(set_oil)

dict_meals[tuple_lunch]=(list_rice[1],list_meat[2],list_milk[0],list_veg[1],list_fruit[2],list_oil[0])
print('中餐:'+str(dict_meals[tuple_lunch]))
setl={list_rice[1],list_meat[2],list_milk[0],list_veg[1],list_fruit[2],list_oil[0]}

#再次重新排序(晚餐)
set_rice=set(list_rice)
list_rice=list(set_rice)

set_meat=set(list_meat)
list_meat=list(set_meat)

set_milk=set(list_milk)
list_milk=list(set_milk)

set_veg=set(list_veg)
list_veg=list(set_veg)

set_fruit=set(list_fruit)
list_fruit=list(set_fruit)

set_oil=set(list_oil)
list_oil=list(set_oil)

dict_meals[tuple_dinner]=(list_rice[2],list_meat[1],list_milk[0],list_veg[2],list_fruit[1],list_oil[0])
setd={list_rice[2],list_meat[1],list_milk[0],list_veg[2],list_fruit[1],list_oil[0]}

print('晚餐:'+str(dict_meals[tuple_dinner]))
print('早餐與中餐有重複嗎?',setb>=setl)
print('中餐與晚餐有重複嗎?',setd>=setl)
print('早餐與晚餐有重複嗎?',setb>=setd)
