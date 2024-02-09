#w12_課堂練習：
#個人作業
#寫三個小故事，或是延續期中專題，分別用with open語法寫入三個不同檔案，再分別讀出來。
#利用seek()分別讀出三個檔案裡的某句，並顯示出來。
#以"課堂練習範本"word檔格式繳交至Moodle
#A1105505 林彧頎
#問題定義
Question={"Question1":"有三種動物分別是\n'猴子' '鳥' '蛇'\n你要從家裡帶祂們出門請問你要怎麼帶祂們去呢?\n",
        "Question2":"有四樣東西\nKEY 你 橋跟兔子\n請編個小故事\n這四樣東西全都要出現在故事裡面中\n",
        "Question3":"從飯廳開始你打算看看整個房子，你看到地上有杯子，杯子是什麼材質？\n你拿起杯子後會做什麼？\n"}
#答案存放            
Story_Ans={"A1":"","A2":"","A3":""}
#解讀定義           
meaning={"1":"猴子=另一半 鳥=孩子 蛇=錢財\n",
         "2":"key=錢 橋=自己的人生 兔子=另一半\n",
         "3":"你看見的杯子材質堅硬程度，是你與在樹林裡一起散步的人關係強度。\n你對杯子的處理方式顯示出你會對這個人做的事。\n"}
#使程式碼可不斷操作
while(True):
    #詢問
    print('心理診療系統\n請問您是使用者還是心理師?\n')
    test=input("使用者(1)心理師(2)")
    #使用者
    if(int(test)==1):
        a=int(input("故事心理測驗嗎(1)查看專家建議(2)"))
        #故事心理測驗
        if(a==1):            
            print('以下將有3個心理測驗\n請依照心理測驗的問題\n依照您的想法，寫出對應的故事\n此文件將給予心理師為您解答\n或是您可以參考回答後的參考答案自行解讀。\n')
            i=1
            #with open寫檔(故事內容)
            for k in Question.keys():
                print(k+Question[k])
                Story_Ans["A"+str(i)]=input("請輸入您的心理測驗故事。\n")
                print(Story_Ans["A"+str(i)])
                with open(f'C:\\Users\\USER\\Downloads\\基礎程式設計\\W12\\Story_test_{i}.txt', 'w') as file_object:
                    file_object.write(k+"\n"+Question[k]+"\n\nANS:\n"+Story_Ans["A"+str(i)])
                print('參考解讀:\n'+meaning[str(i)])
                i=i+1
         #查看專家建議       
        if(a==2):
            i=1
            for k in Question.keys():
                #例外處理
                try:
                    #讀檔並查看專家建議
                    with open(f'C:\\Users\\USER\\Downloads\\基礎程式設計\\W12\\Story_test_{i}.txt', 'r') as file_object:
                        print(file_object.read()+"\n\n")
                    i=i+1
                except Exception:#錯誤處裡
                    print("錯誤!")
                    pass
    #心理學家           
    elif(int(test)==2):
        print("請問您想查看哪一則的答案?")
        ans=input("Story_1:(1)/Story_2:(2)/Story_3:(3)")
        #依照要求給予建議
        if(int(ans)==1 or int(ans)==2 or int(ans)==3):
            line_number=7
            i=int(ans)
            #例外處理
            try:
                #讀答案檔
                with open(f'C:\\Users\\USER\\Downloads\\基礎程式設計\\W12\\Story_test_{i}.txt', 'r') as file_object:
                    print('第'+str(i)+'問題之答案:\n')
                    
                    # 移到第六行起始位置
                    for _ in range(line_number - 1):
                        file_object.readline()
                        
                    # 目前pointer位址
                    sixth_line_start = file_object.tell()
                    # seek移動指標位置
                    file_object.seek(sixth_line_start)
                    print(file_object.read())
                #用a的方法在檔案後續繼續寫檔(建議)        
                with open(f'C:\\Users\\USER\\Downloads\\基礎程式設計\\W12\\Story_test_{i}.txt', 'a') as file_object:
                    recommand=input("請問你想輸入的分析建議?:\n")
                    file_object.write("\n\n專家分析:\n"+recommand)
            #例外處理
            except Exception:
                print("錯誤!")
                pass