import os
import glob
from PIL import Image
import pathlib
## -------------- CONFIG HERE ---------------------
DIR = "./DrowningDetectionDataset/swimming/"
ALLOW_IMAGE_TYPE = ['webp']
## ------------------------------------------------
CONVERT_TO = "png"

filenames = []
imagenames = []
for IMAGE_TYPE in ALLOW_IMAGE_TYPE:
    filenames.append(glob.glob(DIR+"*."+IMAGE_TYPE))
    print(f"{IMAGE_TYPE} has {len(filenames[len(filenames)-1])}.")
for names in filenames :
    for name in names:
        imagenames.append(name) 
imagenames.sort()
if(len(imagenames)>0):
    imgpath = os.path.split(imagenames[0])[0]
    split_path=imgpath.split('/')
    if(len(split_path)==1):
        split_path=imgpath.split('\\')
    if(len(split_path)==1):
        split_path=imgpath.split("//")
    folderName = split_path[len(split_path)-1]
    print(f"Rename to -> {folderName}")
    print(f"Examples of renamed files : ")
    for count,imagename in enumerate(imagenames):
        imgpath = os.path.split(imagename)[0]
        imgname = os.path.split(imagename)[1]
        name = pathlib.Path(imagename).stem
        file_extension = os.path.splitext(imgname)[1]
        newname = name + '.' + CONVERT_TO
        print(imgpath+"/"+newname)
        if count == 4:
            break
    # Confirmation
    all_images_count = len(imagenames)
    print(f"ALL Image = {all_images_count}")
    confFlag = input("Confirm to rename? (y/n) ")
    if(confFlag=='y' or confFlag=='Y'):
        for count,imagename in enumerate(imagenames):
            imgpath = os.path.split(imagename)[0]
            imgname = os.path.split(imagename)[1]
            name = pathlib.Path(imagename).stem
            file_extension = os.path.splitext(imgname)[1]
            newname = name + '.' + CONVERT_TO
            imgPIL = Image.open(imagename).convert("RGB")
            imgPIL.save(imgpath+"/"+newname)
            print(f"-> {imgpath}/{newname} converted!")
        print("Done!")
else:
    print(f"no image type {ALLOW_IMAGE_TYPE} in {DIR}")
