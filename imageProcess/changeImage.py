from PIL import Image, ImageDraw, ImageFont
import pygame

def createTransparentText(fileOut, text, /, width=150, height=30, *, color=(255, 255, 255, 0), mode='RGBA'):
    img = Image.new(mode=mode, size=(width, height), color=color)
    painter = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 25) 
    painter.text((0,0), text, fill=(255,0,0), font=font)
    img.save(fileOut)
    print("Successful")

def createBullet(fileOut, /, width, height, *, color=(255, 255, 255, 0), mode='RGBA'):
    img = Image.new(mode=mode, size=(width, height), color=color)
    painter = ImageDraw.Draw(img)
    xy = [(0,0), (5,0), (5,10),(0,10)]
    painter.polygon(xy, (255,0,0))
    xy = [(5,0), (15,0), (20,5),(15,10),(5,10)]
    painter.polygon(xy, (242,185,50))

    img.save(fileOut)
    print("Successful")

def changeSize(fileIn, fileOut, width1, height1, scale=None):
    img = Image.open(fileIn)
    width, height = img.size
    if scale is not None:
        newWidth = int(width * scale)
        newHeight = int(height * scale)
        img = img.resize((newWidth, newHeight))
    else:
        img = img.resize((width1, height1))

    img.save(fileOut)
    print("Successful")

def makeTransparent(fileIn, fileOut):
    r,g,b=245,245,245
    img = Image.open(fileIn)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []

    # for item in datas:
    #     print(item[0],item[1],item[2],item[3])
    #     break
    for item in datas:
        if item[0] == r and item[1]==g and item[2]==b:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(fileOut, "PNG")
    print("Successful")

def rotate(fileIn, fileOut, angle):
    img = Image.open(fileIn)
    img = img.rotate(angle)
    img.save(fileOut)
    print("Successful")

if __name__ == '__main__':
    # changeSize("head.png", "head1.png", 40, 40)
    # changeSize("fighter.png", "fighter1.png", 400, 400)
    # rotate("fighter1.png", "fighter2.png", -90)
    # makeTransparent("fighter.png", "fighter5.png")
    # changeSize("fighter3.png", "fighter4.png", 60, 50)
    # changeSize("fighterjet.png", "fighterjet1.png", 70, 60)
    # changeSize("forest.jpg", "forest1.jpg", 640, 480)
    # makeTransparent("apple.png", "apple1.png")
    # changeSize("background.jpg", "background1.jpg", 400, 300)
    # makeTransparent("pythonprogramming.png", "pythonprogramming1.png")
    # makeTransparent("win.png", "win1.png")
    # changeSize("win1.png", "win2.png", 200, 160)
    # makeTransparent("apple1.jpg", "apple2.jpg")
    # changeSize("apple2.png", "apple3.png", 40, 40)
    # changeSize("gameover.jpg", "gameover1.jpg", 250, 200)
    # changeSize("imageProcess/grassfield.jpg", "imageProcess/grassfield1.jpg", 640, 480)
    # createBullet("bullet.png", 20, 20)
    # rotate("bullet.png", "bullet2.png", 90)
    createTransparentText("gameover.png", "Game Over!!!")
