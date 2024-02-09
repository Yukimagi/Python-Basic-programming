# 自訂函式寫在主程式前面
def WM():
    print('注水')
    print('清洗')
    print('洗淨洗劑')
    print('脫水')
    print('烘乾')

# 主程式呼叫函式，主程式寫在自訂函式後面
WM()
print('星期一洗衣')
WM()
print('星期二洗衣')

#在函式中撰寫條件分支
def WM(mode):
    print('注水')
    if (mode == 'soft'):
        print('輕柔清洗')
    elif (mode == 'hard'):
        print('強力清洗')
    else:
        print('一般清洗')

#呼叫函式的同時傳遞參數
WM('soft')
print('第一次是柔洗')
WM('hard')
print('第二次是強洗')

#計算圓形面積的函式
def area(radius):
    result = radius * radius * 3.14
    return result

x = area(5)
print(x)

# 計算字串字數
print(len('thunderbolt'))

# 元素數量
animal = ['cat', 'dog', 'duck']
print(len(animal))

