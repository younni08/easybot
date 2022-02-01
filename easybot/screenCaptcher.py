from re import A
from PIL import ImageGrab,Image
from time import sleep

a = 91
# max = 983

print('processing image {0}'.format(a))
area = (290,120,1650,900)

while True:
    img=ImageGrab.grab()
    # img.crop(area).save('./maple_image_bank/0.png', 'png')
    img.crop(area).save('./easybot/image/{0}.png'.format(a), 'png')
    sleep(1)
    a = a + 1
    if a > 3000:
        break