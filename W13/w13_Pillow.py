from PIL import Image, ImageFilter, ImageEnhance
image = Image.open("D:\\個人資料夾\\Downloads/flower.jpg")

#處理三原色
r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))

convert_image.show()

convert_image.save("D:\\個人資料夾\\Downloads/flower_bgr.jpg")

#rotate 180
rotate_180 = image.transpose(Image.ROTATE_180)
rotate_180.show()
rotate_180.save("D:\\個人資料夾\\Downloads/logo1_rotate_180.jpg")

#contour 輪廓處理
contour = image.filter(ImageFilter.FIND_EDGES)
contour.show()
contour.save("D:\\個人資料夾\\Downloads/logo1_contour.jpg")

#contrast對比增加
enh_contrast = ImageEnhance.Contrast(image)
contrast = enh_contrast.enhance(20)
contrast.show()
contrast.save("D:\\個人資料夾\\Downloads/logo1_contrast.jpg")

#emboss浮雕
emboss = image.filter(ImageFilter.EMBOSS)
emboss.show()
emboss.save("D:\\個人資料夾\\Downloads/logo1_emboss.jpg")

#blackwhite黑白
blackwhite = image.convert("1")
blackwhite.show()
blackwhite.save("D:\\個人資料夾\\Downloads/logo1_blackwhite.jpg")

#灰階
gray_iamge = image.convert("L")
gray_iamge.show()
gray_iamge.save('D:\\個人資料夾\\Downloads/logo1_gray.jpg')

#resized縮放
resized = image.resize((round(image.size[0] * 2), round(image.size[1] * 1.5)))
resized.show()
resized.save("D:\\個人資料夾\\Downloads/logo1_resized.jpg")

#模糊化
filtered = image.filter(ImageFilter.BLUR)
filtered.show()
filtered.save("D:\\個人資料夾\\Downloads/logo1_filtered.jpg")

