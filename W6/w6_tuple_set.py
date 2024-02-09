#1. 序對型別 ( Tuple Type )
#2. Tuple 與 List 之不同處
#3. 集合型別 ( Set Type )
#4. Set( )函數
#5. 使用set函式建立集合型別資料

#Tuple語法 => (元素1, 元素2, 元素3, ....)
#Tuple接受不同型態元素 (與List相同)
#Tuple宣告後不能再變更存放的資料 (與List不同)
#Tuple意思：多個元素組成一個群組；元素彼此有關係

tuple_smaple = ('apple', 3, 90.4)    #什麼意思?
print(tuple_smaple)

flavor_list = ['薄荷', ' 巧克力', '草莓', '香草']   #List型別，存放四個字串
flavor_list[0] = '蘭姆葡萄乾'
flavor_list[3] = '香蕉'
print(flavor_list)

flavor_tuple = ('薄荷', ' 巧克力', '草莓', '香草')
flavor_tuple[0] = '蘭姆葡萄乾'  #TypeError
flavor_tuple[2] = '香蕉'   #TypeError
print(flavor_tuple)


#Tuple可以用來當Dictionary的Key, List不行, 因Tuple的值不能再被異動
#Key by Tuple

#設計一個體重紀錄App
diary =  {}                # 先宣告一個空Dict
key = ('kamata', '08-01')  # 多個元素當Key想到Tuple
diary[key] = 70
key = ('kamata', '08-03')
diary[key] = 72
key = ('nakata', '08-04')
diary[key] = 58
print(diary)
print(diary[('kamata', '08-03')])
print(str(diary[('kamata', '08-03')] + diary[('kamata', '08-01')])+'kg')
#數值無法與字串串接，利用str將數值轉為字串

#Set Type
#一樣可存多項資料
#語法 => {元素1, 元素2, 元素3, ....}

candy = {'delicious', 'fantastic'}   #set型別，存放兩個字串
print(candy)#會打亂順序

#set()函式
#將string拆解並不留相同資料
candy = set('delicious')
print(candy)
words = set('國立高雄大學')
print(words)
words = set('國立', '高雄',  '大學')  #TypeError

#技巧1: set()可以用將List中的重複項刪除
flavor = ['apple', 'peach', 'soda', 'soda']   #List型別
print(flavor)
candy = set(flavor)
print(candy)

words = ['國立', '高雄',  '大學', '國立', '大學']
name = set(words)
print(name)

#技巧1: 轉成set後可以使用update()來新增集合元素
candy.update(['grape']) 
print(candy)

#技巧1:再用list()函式轉回List
flavor = ['apple', 'peach', 'soda', 'chocolate', 'soda', 'grape', 'grape']  
flavor_set = set(flavor)   #利用set()刪去重複元素  
print(flavor_set)  
flavor = list(flavor_set)  #再用list()函式轉回List 
print(flavor)


#技巧2: Set可以輕易用來"比較"元素內容，List不容易做到
#e.g.,比較最近兩週境外移入確診的國家別
#透過集合比較算子
A = {'a', 'b', 'c'}  
B = {'e', 'f', 'c'}
print("A <= B:", A<=B)  #B是否包含A的所有
print("A >= B:", A>=B)  #A是否包含B的所有
print("A | B:", A|B)  #聯集
print("A & B:", A&B)  #交集
print("A - B:", A-B)  #差集:A有B沒有
print("A ^ B:", A^B)  #互次:A和B共同之外的
