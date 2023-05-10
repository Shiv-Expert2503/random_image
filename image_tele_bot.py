import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import os
import cv2
import random
from PIL import Image

#Save Directory
querry=input().replace(" ","")
save_dir='images/{}'.format(querry)
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

response=requests.get("https://www.google.com/search?q={}&sxsrf=APwXEdejlp9E7WqnOtfUAeqVq7j5FKId4g:1683019846012&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiN6cjAqdb-AhXm7TgGHdPdCZsQ_AUoAXoECAEQAw&biw=1536&bih=810&dpr=1.25".format(querry))


all_html=bs(response.content,"html.parser")
all_imgs=all_html.find_all('img')[1:]

data={}
for i in all_imgs:
    img_url=i['src']
    img_data=requests.get(img_url).content
    # print(img_data)
    with open(os.path.join(save_dir,f"{querry}_{all_imgs.index(i)}.jpg"),"wb") as f:
        f.write(img_data)

    data['{}'.format(f"{querry}_{all_imgs.index(i)}.jpg")]=img_data
    
# all_imges=[]
# for i in os.listdir("images/{}".format(querry)):
#     all_imges.append(i)

# images=random.choice(all_imges)
# images
img_=os.listdir('images/{}/'.format(querry))

print(img_)
images=random.choices(img_)
print((images))

##To resize
# for i in img_:
#     i__=Image.open(f'images/LordHari/{i}')
#     new_image=i__.resize((600,600))
#     new_image.save(f'images/LordHari/{i}_resized.jpg')
#     os.remove(f'images/LordHari/{i}')





img=cv2.imread(f"IMAGES/{querry}/{querry}_"+str(random.randint(0,20))+".jpg")
# img=cv2.imread("images/LordHari/LordHari_0_resized.jpg")
# bigger = cv2.resize(img, (1050, 1610),interpolation = cv2.INTER_LINEAR)
# img=cv2.imread(bigger)
while True:
    cv2.imshow(f"{querry}",img)
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed ==ord('q'):
        break
cv2.destroyAllWindows()
for i in img_:
    os.remove(f'images/{querry}/{i}')
os.rmdir(f'images/{querry}')
os.rmdir('images')

