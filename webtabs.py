import subprocess
import os
import sys
import webbrowser

#Path to URLS.txt file on your local machine
#Example C:\Tools\webtaburls.txt
path = ""
urls = os.path.exists(path)

if urls == True:
    print("File looks good..")
    fhand = open(path, "r")
    counter = 0
    myList = []
    for line in fhand:
        line = line.strip()
        myList.append(line)
        counter = counter + 1
        
    for url in myList:
        webbrowser.open(url, new=1)
    
else:
    print("testing")
    sys.exit()







