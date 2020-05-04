import os, os.path
from shutil import copyfile

camera1 = sorted(os.listdir("/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 1/"))
camera2 = sorted(os.listdir("/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 2/"))
camera3 = sorted(os.listdir("/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 3/"))
camera4 = sorted(os.listdir("/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 4/"))
camera5 = sorted(os.listdir("/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 5/"))
camera6 = sorted(os.listdir("/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 6/"))
cameras = [camera1, camera2, camera3, camera4, camera5, camera6]
trues = [False, False, False, False, False]

for x in range (5): 
    if (len(cameras[x]) == len(cameras[x+1])):
        trues[x] = True
    print (x+1, "=", x+2, trues[x])

if trues[0] and trues[1] and trues[2] and trues[3] and trues[4]:
    print ("Good to go")
    
else:
    print ("Not good to go")
    
filename = input("What's the filename? ") #GOPR0284.JPG
wgname = input ("What do you want to call this wigglegram? ")
folderpath = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname)

if filename in camera1:
    picindex = camera1.index(filename)
    
pic1src = "/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 1/" + camera1[picindex]
pic1dst = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname) + "/1.JPG"
pic2src = "/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 2/" + camera2[picindex]
pic2dst = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname) + "/2.JPG"
pic3src = "/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 3/" + camera3[picindex]
pic3dst = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname) + "/3.JPG"
pic4src = "/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 4/" + camera4[picindex]
pic4dst = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname) + "/4.JPG"
pic5src = "/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 5/" + camera5[picindex]
pic5dst = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname) + "/5.JPG"
pic6src = "/Users/ethanjohnsong/Pictures/GoPro/1969-12-31/HERO3+ Silver Edition 6/" + camera6[picindex]
pic6dst = "/Users/ethanjohnsong/Desktop/WG Suite/" + str(wgname) + "/6.JPG"

os.mkdir(folderpath)

copyfile(pic1src, pic1dst)
copyfile(pic2src, pic2dst)
copyfile(pic3src, pic3dst)
copyfile(pic4src, pic4dst)
copyfile(pic5src, pic5dst)
copyfile(pic6src, pic6dst)