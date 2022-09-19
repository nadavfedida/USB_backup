import os
if os.path.isdir("/Users/nadav/Desktop/Uni/Private/USB_project/Test1/"):
    print("folder entered")
    os.chdir('/Users/nadav/Desktop/Uni/Private/USB_project/Test1/')
    f=open('testingFile.txt','w+')
    f.write('this is a test doc')
    f.close()

else:
    print("current directory not found")
# /Users/nadav/Desktop/Uni/Private/USB_project/Test1