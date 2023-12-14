import os
import glob
from PIL import Image


FolderPath = "./datas/raw/images/"
ComicPaths = [f for f in os.listdir(FolderPath) if os.path.isdir(os.path.join(FolderPath, f))]

for xPath in ComicPaths:
    
    xEditedPath = "./datas/edited/images/" + xPath
    
    if not os.path.isdir(xEditedPath):
        os.mkdir(xEditedPath)
    
    # 見開きページの幅を取得
    xRawPath = "./datas/raw/images/" + xPath
    FirstImg = Image.open(xRawPath + '/000.jpg')
    FullWidth, FullHeight = FirstImg.size
    print(FullHeight)
    
    PageCount = 0
    for yPath in sorted(glob.glob(xRawPath + '/*.jpg')):
        xxImg = Image.open(yPath)
        aResizeImg = xxImg.crop((FullWidth // 2, 0, FullWidth, FullHeight))
        bResizeImg = xxImg.crop((0, 0, FullWidth // 2, FullHeight))
        aResizeImg.save(xEditedPath + "/" + str(PageCount).zfill(3) + '.jpg', quality=95) 
        bResizeImg.save(xEditedPath + "/" + str(PageCount + 1).zfill(3) + '.jpg', quality=95)
        
        PageCount += 2