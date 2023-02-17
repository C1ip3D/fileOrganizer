import os
import shutil

src = "" #Put the source path
dest = "" #Put the destination path


imgFiles = ['.png', '.jpg', ".jfif", ".gif", '.tiff', '.jpeg']
vidFiles = ['.mov', '.mp4', 'mp3', ]
installers = ['.exe', '.bat', '.csv','.reg']
programmingFiles = ['.java', '.js', '.py', '.html', '.css']
normal = ['.pdf', '.txt']

fileList = os.listdir(src)
for file in fileList:
    name,ext = os.path.splitext(file)
    if ext == '':
        continue
    if ext in imgFiles:
        path1 =  src+ '/'+file
        path2 = dest + '/' + "Images"
        path3 = dest + '/' + "Images" + '/'+file
        if os.path.exists(path2):
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
    elif ext in vidFiles:
        path1 = src + '/'+file
        path2 = dest + '/' + "Videos"
        path3 = dest + '/' + "Videos" + '/'+file
        if os.path.exists(path2):
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
    elif ext in installers:
        path1 = src + '/'+file
        path2 = dest + '/' + "Installers"
        path3 = dest + '/' + "Installers" + '/'+file
        if os.path.exists(path2):
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
    elif ext in programmingFiles:
        path1 = src + '/'+file
        path2 = dest + '/' + "Programing"
        path3 = dest + '/' + "Programming" + '/'+file
        if os.path.exists(path2):
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
    elif ext in normal:
        path1 = src + '/'+file
        path2 = dest + '/' + "Files"
        path3 = dest + '/' + "Files" + '/'+file
        if os.path.exists(path2):
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving "+ file + '...' )
            shutil.move(path1, path3)
    else:
        print("The remaining files shall be put in random folder")
        path1 = src + '/' + file
        path2 = dest + '/' + "Random"
        path3 = dest + '/' + "Random" + '/' + file
        if os.path.exists(path2):
            print("Moving " + file + '...')
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving " + file + '...')
            shutil.move(path1, path3)




