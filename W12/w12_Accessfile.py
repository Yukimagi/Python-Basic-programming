file_object = open('C:\\Users\\user\\Downloads\\python3.txt', 'r+')
#file_object = open('C:\\Users\\USER\\Downloads\\python3.txt', 'w')
#file_object = open('C:\\Users\\USER\\Downloads\\python3.txt', 'a')

print(file_object.read())

file_object.write('5.this is sample of python\n')
# 將起始位置移至檔案開頭
file_object.seek(0)
print(file_object.read())
#file_object.flush()
#file_object.write('2.this is sample of python\n')
#file_object.write('3.this is sample of python777777\n')
with open('with.txt', 'w') as file_object:
    file_object.write('using with')

# C:\\Users\\USER\\Downloads
#print(file_object.read())
file_object.close()
