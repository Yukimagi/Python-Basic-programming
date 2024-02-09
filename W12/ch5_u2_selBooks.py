'''
可以讀入所產生的books.txt
可以進行選書並計算總價
並將結果輸出為yourOrder.txt
'''
# 讀入書籍資訊
with open('books.txt', 'r', encoding='utf-8') as file:
    books = [line.strip().split(',') for line in file]

# 列印書籍清單及庫存
print("書籍清單：")
for i, book in enumerate(books):
    print(f"{i+1}. {book[0]} {book[1]}元，庫存量{book[2]}本")

# 初始化購物車
cart = []

# 讀入用戶選擇的書籍編號，並加入購物車
while True:
    choice = input("請選擇欲訂購的書籍編號（按 Enter 結束訂購）：")
    if not choice:
        break
    try:
        choice = int(choice)
        if 1 <= choice <= len(books):
            book = books[choice-1]
            if int(book[2]) > 0:
                cart.append(book)
                print(f"已加入{book[0]}")
                book[2] = str(int(book[2]) - 1)  # 更新庫存
            else:
                print(f"{book[0]}庫存不足，無法加入購物車")
        else:
            print(f"沒有編號為{choice}的書籍")
    except ValueError:
        print(f"請輸入正確的書籍編號")

# 計算總價
total = sum([float(book[1]) for book in cart])

# 列印購物清單及庫存
print("\n購物清單：")
for i, book in enumerate(cart):
    print(f"{i+1}. {book[0]} {book[1]}元")
print(f"總價：{total}元")

# 寫入 yourOrder.txt 檔案
with open('yourOrder.txt', 'w', encoding='utf-8') as file:
    file.write("您的購物清單：\n")
    for i, book in enumerate(cart):
        file.write(f"{i+1}. {book[0]} {book[1]}元\n")
    file.write(f"總價：{total}元\n")

# 列印庫存清單
print("\n庫存清單：")
for i, book in enumerate(books):
    print(f"{i+1}. {book[0]} {book[2]}本")
