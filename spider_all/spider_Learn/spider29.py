import pytesseract
from PIL import Image

img = Image.open('code2.jpg')  # 先创建image对象
img = img.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
img = img.point(table, '1')
img.show()
text = pytesseract.image_to_string(img)  # 直接转化成string，更多参数可以查看文档
print(text)  # "OFXo"
