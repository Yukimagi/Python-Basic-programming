#w13_課堂練習:
#個人作業
#自行找一張照片，試著將照片做以下的效果：改變亮度、扭曲、馬賽克、浮雕、輪廓處理、模糊化...
#以"課堂練習範本.doc"格式繳交至Moodle
from PIL import Image, ImageFilter, ImageEnhance

#顯示圖片(用Pillow的套件Image開檔)
print("原圖片:flower.jpg")
image=Image.open('C://Users//USER//Downloads//基礎程式設計//W13//flower.jpg')
image.show()
while(True):
    n=int(input("請問你想對圖片進行怎麼樣的處裡呢?\n改變顏色(0)\n改變亮度(1)\n扭曲(2)\n馬賽克(3)\n浮雕(4)\n輪廓處理(5)\n模糊化(6)\n對比化(7)\n旋轉與縮放化(8)\n"))
    if(n==0):
        print("互補圖:flower_bgr.jpg\n")
        #處理三原色
        #將藍色和紅色互補後再顯示圖片
        r, g, b = image.split()
        convert_image = Image.merge('RGB', (b, g, r))
        convert_image.show()#顯示互補顏色後的圖片
        convert_image.save("C://Users//USER//Downloads//基礎程式設計//W13//flower_bgr.jpg")#另存檔案
        
        print("黑白圖:logo1_blackwhite.jpg\n")
        #blackwhite黑白
        blackwhite = image.convert("1")#1 bit單位元的黑白圖片
        blackwhite.show()
        blackwhite.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_blackwhite.jpg")
        
        print("灰階圖:logo1_gray.jpg\n")
        #灰階
        gray_iamge = image.convert("L")#轉成灰階圖片
        gray_iamge.show()
        gray_iamge.save('C://Users//USER//Downloads//基礎程式設計//W13//logo1_gray.jpg')#另存檔案
    if(n==1):
        print("調整亮度圖:logo1_bright.jpg\n")
        factor=int(input('調整的亮度參數'))
        #亮度增強對象
        enhancer = ImageEnhance.Brightness(image)
        #調整亮度
        image_brightness_adjusted = enhancer.enhance(factor)
        #show & save
        image_brightness_adjusted.show()
        image_brightness_adjusted.save('C://Users//USER//Downloads//基礎程式設計//W13//logo1_bright.jpg')
    if(n==2):
        print("扭曲圖:distorted_image.jpg\n")
        #扭曲
        # 獲取圖像的寬度和高度
        w, h = image.size
        factor=int(input('調整的扭曲參數'))
        # 創建一個新圖像對象，與原始圖像相同大小
        distorted_image = Image.new('RGB', (w, h))

        # 扭曲圖像
        for y in range(h):
            for x in range(w):
                dx = int(factor * w * (y - h / 2) / h)
                dy = int(factor * h * (x - w / 2) / w)
                distorted_x = x + dx
                distorted_y = y + dy

                if 0 <= distorted_x < w and 0 <= distorted_y < h:
                    distorted_image.putpixel((x, y), image.getpixel((distorted_x, distorted_y)))
        distorted_image.show()
        # 保存生成的扭曲圖像
        distorted_image.save('C://Users//USER//Downloads//基礎程式設計//W13//distorted_image.jpg')

    if(n==3):
        print("馬賽克圖:mosaic_image.jpg\n")
        factor=int(input('馬賽克方格大小參數'))
        #馬賽克
        # 獲取圖像的寬度和高度
        w, h = image.size
        # 創建一個新圖像對象，與原始圖像相同大小
        mosaic_image = Image.new('RGB', (w, h))
        # 循環遍歷圖像的每個塊
        for y in range(0, h, factor):
            for x in range(0, w, factor):
                # 獲取當前塊的顏色
                piece = image.crop((x, y, x + factor, y + factor))
                avg_color = piece.resize((1, 1)).getpixel((0, 0))

                # 將整個塊填充為平均顏色
                mosaic_image.paste(avg_color, (x, y, x + factor, y + factor))
        mosaic_image.show()
        # 保存生成的馬賽克圖像
        mosaic_image.save('C://Users//USER//Downloads//基礎程式設計//W13//mosaic_image.jpg')
    if(n==4):
        print("浮雕圖:logo1_emboss.jpg\n")
        #emboss浮雕
        emboss = image.filter(ImageFilter.EMBOSS)
        emboss.show()
        emboss.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_emboss.jpg")
    if(n==5):
        print("輪廓處理圖:logo1_contour.jpg\n")
        #contour 輪廓處理
        contour = image.filter(ImageFilter.FIND_EDGES)
        contour.show()
        contour.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_contour.jpg")
    if(n==6):
        print("模糊化圖:logo1_filtered.jpg\n")
        #模糊化
        filtered = image.filter(ImageFilter.BLUR)
        filtered.show()
        filtered.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_filtered.jpg")
    if(n==7):
        #contrast對比增加
        print("對比圖:logo1_contrast.jpg\n")
        factor=int(input('對比大小參數'))
        enh_contrast = ImageEnhance.Contrast(image)
        contrast = enh_contrast.enhance(factor)
        contrast.show()
        contrast.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_contrast.jpg")
    if(n==8):
        print("rotate 180:logo1_rotate_180.jpg\n")
        #rotate 180
        rotate_180 = image.transpose(Image.ROTATE_180)
        rotate_180.show()
        rotate_180.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_rotate_180.jpg")
        
        print("resized縮放圖:logo1_resize.jpg\n")
        #resized縮放
        resized = image.resize((round(image.size[0] * 2), round(image.size[1] * 1.5)))
        resized.show()
        resized.save("C://Users//USER//Downloads//基礎程式設計//W13//logo1_resized.jpg")