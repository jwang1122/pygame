from PIL import Image

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
    print("Successfule")

def makeTransparent(fileIn, fileOut):
    img = Image.open(fileIn)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 247 and item[1]==247 and item[2]==247:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(fileOut, "PNG")
    print("Successfule")

def rotate(fileIn, fileOut, angle):
    img = Image.open(fileIn)
    img = img.rotate(angle)
    img.save(fileOut)
    print("Successfule")

if __name__ == '__main__':
    # changeSize("head.png", "head1.png", 40, 40)
    # changeSize("fighter.png", "fighter1.png", 400, 400)
    # rotate("fighter1.png", "fighter2.png", -90)
    # makeTransparent("fighter2.png", "fighter3.png")
    # changeSize("fighter3.png", "fighter4.png", 60, 50)
    # changeSize("fighterjet.png", "fighterjet1.png", 70, 60)
    changeSize("forest.jpg", "forest1.jpg", 640, 480)
