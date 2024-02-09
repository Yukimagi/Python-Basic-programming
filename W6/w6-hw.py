import math
#工作量、體重(字典定義)
#將key改為tuple(m(中度),l(輕度),h(重度))
#體重(l),工作(l)
ll=('體重過輕者','輕度工作')
ml=('體重正常者','輕度工作')
hl=('體重過重者','輕度工作')

lm=('體重過輕者','中度工作')
mm=('體重正常者','中度工作')
hm=('體重過重者','中度工作')

lh=('體重過輕者','重度工作')
mh=('體重正常者','重度工作')
hh=('體重過重者','重度工作')

dict_kcal={ll:35,
           ml:30,
           hl:25,
           
           lm:40,
           mm:35,
           hm:30,
           
           lh:45,
           mh:40,
           hh:35}

#每日熱量
print('每日熱量建議')
#字典輸出
#體重過輕者
print('-----------------')
print('體重過輕者所需熱量:')
print('輕度工作: '+str(dict_kcal[ll])+' kcal')
print('中度工作: '+str(dict_kcal[lm])+' kcal')
print('重度工作: '+str(dict_kcal[lh])+' kcal')
#體重正常者
print('-----------------')
print('體重正常者所需熱量:')
print('輕度工作: '+str(dict_kcal[ml])+' kcal')
print('中度工作: '+str(dict_kcal[mm])+' kcal')
print('重度工作: '+str(dict_kcal[mh])+' kcal')
#體重過重者
print('-----------------')
print('體重過重者所需熱量:')
print('輕度工作: '+str(dict_kcal[hl])+' kcal')
print('中度工作: '+str(dict_kcal[hm])+' kcal')
print('重度工作: '+str(dict_kcal[hh])+' kcal')
print('-----------------')
#顯示我的熱量計算
print('我的體重:49kg')
w=49
print('我的身高:158cm')
h=158
print('我的工作量:正常')
print('我的bmi:正常')
print('我所需的熱量:'+str(dict_kcal[mm]*w))
print('-----------------')
#顯示我的每日飲食建議量
print('請參考以下\n每日飲食建議量')
#使用變數，可幫助之後有其他大卡的數據可以直接修正
a=3
b=5
c=1.5
d=3
e=2
f=5
print('由於我是1715大卡\n(因此我大約需要1800大卡):')
print('全榖雜糧類:'+str(a)+'份')
print('豆魚蛋肉類:'+str(b)+'份')
print('乳品類    :'+str(c)+'份')
print('蔬菜類    :'+str(d)+'份')
print('水果類    :'+str(e)+'份')
print('油脂類    :'+str(f)+'份')
print('total     :'+str(a+b+c+d+e+f)+'份')
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
#食物組合與熱量(使用字典與list)
#list(名稱,份,大卡)
全榖雜糧類1=['飯',3,840]
全榖雜糧類2=['飯',2,560]

豆魚蛋肉類1=['肉',4,160]
豆魚蛋肉類2=['肉',5,200]

乳品類1=['牛奶',1.5,225]
乳品類2=['牛奶',2,300]

蔬菜類1=['菜',1,25]
蔬菜類2=['菜',3,75]

水果類1=['水果',1,60]
水果類2=['水果',2,120]

油脂類1=['油',4,240]
油脂類2=['油',5,300]

food_set1={'全榖雜糧類':全榖雜糧類1,'豆魚蛋肉類':豆魚蛋肉類2,'乳品類':乳品類1,
           '蔬菜類':蔬菜類2,'水果類':水果類2,'油脂類':油脂類1}
food_set2={'全榖雜糧類':全榖雜糧類2,'豆魚蛋肉類':豆魚蛋肉類1,'乳品類':乳品類2,
           '蔬菜類':蔬菜類1,'水果類':水果類1,'油脂類':油脂類2}
#印出結果並自行比較與選擇
print('食物組合1\n(名稱、份數、熱量(大卡))')
print(food_set1.values())
print('總熱量:'+str(food_set1['全榖雜糧類'][2]+food_set1['豆魚蛋肉類'][2]+
                food_set1['蔬菜類'][2]+food_set1['乳品類'][2]+
                food_set1['水果類'][2]+food_set1['油脂類'][2])+'kcal')

print('食物組合2\n(名稱、份數、熱量(大卡))')
print(food_set2.values())
print('總熱量:'+str(food_set2['全榖雜糧類'][2]+food_set2['豆魚蛋肉類'][2]+
                food_set2['蔬菜類'][2]+food_set2['乳品類'][2]+
                food_set2['水果類'][2]+food_set2['油脂類'][2])+'kcal')
print('-----------------')
print('3餐食物隨機組合:')
#list與set的使用(並同時做早餐的重新排序)
list_rice=['白飯','麵線']
set_rice=set(list_rice)
#測試update
set_rice.update(['白飯'])
set_rice.update(['紫米飯'])
set_rice.update(['五穀雜糧飯'])
list_rice=list(set_rice)
#print(list_rice) #測試是否隨機產生(是)

list_meat=['炒豬肉絲','煎魚','雞肉丁','丁香魚','肉丸','扁食']
set_meat=set(list_meat)
list_meat=list(set_meat)

list_milk=['牛奶','羊奶','起司','優格','乳酪蛋糕']
set_milk=set(list_milk)
list_milk=list(set_milk)

list_veg=['炒高麗菜','燙地瓜葉','苦瓜鹹蛋','炒A菜','炒筍子']
set_veg=set(list_veg)
list_veg=list(set_veg)

list_fruit=['蘋果','西瓜','奇異果','香蕉','蓮霧','水蜜桃']
set_fruit=set(list_fruit)
list_fruit=list(set_fruit)

list_oil=['酪梨','堅果','橄欖油','玄米油']
set_oil=set(list_oil)
list_oil=list(set_oil)


tuple_breakfast=('早餐','400卡')
tuple_lunch=('中餐','400卡')
tuple_dinner=('晚餐','400卡')

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
