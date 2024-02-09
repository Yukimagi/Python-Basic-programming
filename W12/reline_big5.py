# 這是一個簡單的Python程式，它可以一次讀取一行文本文件，並在讀取完畢後輸出結果：

with open('file.txt', 'r', encoding='big5') as file:
    for line in file:
        print(line.strip())

