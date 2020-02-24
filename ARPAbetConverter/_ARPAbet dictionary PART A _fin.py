import os
import os.path
import re

#WIP search up dictionary foler, count files, open files one by one.



def rawARPAbet():
    directory = "dictionares/"
    all_dic = os.listdir(directory)

    print(all_dic)

    nah = 0
    for f in all_dic:
        nah += 1

    blankTXT = ''
    kek = 0
    for f in all_dic:
        dic_list = open(str(directory + all_dic[kek]), 'r')
        blankTXT += dic_list.read()
        kek = kek + 1
        
        if kek == nah:
            ff = open('raw_ARPAbet.txt', 'w')
            ff.write(blankTXT)
            ff.close()
            dic_list.close()
            print('raw_ARPAbet.txt was successfuly created')

            
try:
    print('Do you wish to create new "raw_ARPAbet.txt"? \nY or N')
    #rawARPAbet()
    con1 = input()
    if (con1 == 'Y') or (con1 == 'y'):
        rawARPAbet()
        
    print("""PART A complete, use PART B""")

except:
    print("""raw_ARPAbet.txt do not exist or cannot be created,
          check if the folder 'dictionares' exist in same directory as
          PY file and if it contains text files""")


