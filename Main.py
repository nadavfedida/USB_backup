import os, shutil
from os.path import isfile, join

source_dir = '/Users/nadav/Desktop/Uni/Private/USB_project/Test1/'
dest_dir = '/Users/nadav/Desktop/Uni/Private/USB_project/Test2/'

if len(os.listdir(source_dir)) != 0:
    print("folder 1 entered")
    os.chdir(source_dir)
    # f=open('testingFile1.txt','w+')
    # f.write('this is a test doc 1')
    
    onlyfiles = [f for f in os.listdir(source_dir) if isfile(join(source_dir, f))]
    print(onlyfiles)


    if os.path.isdir(dest_dir):
        shutil.move(os.path.join(source_dir, 'testingFile.txt'), dest_dir)
    # f.close()
elif len(os.listdir(dest_dir) ) != 0:
    print("folder 2 entered")
    os.chdir(dest_dir)


    # f=open('testingFile.txt','w+')
    # f.write('this is a test doc')
    if os.path.isdir(source_dir):
        shutil.move(os.path.join(dest_dir, 'testingFile.txt'), source_dir)
    # f.close()

else:
    print("current directory not found")



# for position, file in enumerate(destFile):
#     if not os.path.exists(file):
#         file_sr = srcFile[position]
#         if not os.path.exists(file): 
#             shutil.copy(file_sr, 'C:\destFile')
