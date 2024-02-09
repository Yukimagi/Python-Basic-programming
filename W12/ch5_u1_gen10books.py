# 將10本書的資訊寫入到一個 txt 檔案中的程式碼

books = [
    {'title': '深淵的秘密', 'price': 350, 'quantity': 10},
    {'title': '失落的文明', 'price': 450, 'quantity': 5},
    {'title': '終結者的復仇', 'price': 300, 'quantity': 8},
    {'title': '蒼穹的羽翼', 'price': 250, 'quantity': 12},
    {'title': '迷霧中的真相', 'price': 400, 'quantity': 6},
    {'title': '暴風雨前的平靜', 'price': 280, 'quantity': 15},
    {'title': '時光之盒', 'price': 500, 'quantity': 3},
    {'title': '禁忌的魔法', 'price': 380, 'quantity': 9},
    {'title': '雪山神秘事件', 'price': 420, 'quantity': 7},
    {'title': '黑暗森林的傳說', 'price': 320, 'quantity': 11}
]

with open('books.txt', 'w', encoding='utf-8') as file:
    for book in books:
        file.write(f"{book['title']}, {book['price']}, {book['quantity']}\n")
