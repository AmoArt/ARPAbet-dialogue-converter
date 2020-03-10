import os
import os.path
import re

def rawARPAbet():
    directory = "dictionaries/"
    all_dic = os.listdir(directory)

    print(all_dic)

    nah = 0
    for f in all_dic:
        nah += 1

    blankTXT = ''
    kek = 0
    for f in all_dic:
        dic_list = open(str(directory + all_dic[kek]), 'r', encoding='utf-8') #utf-16-le #utf-8
        for line in dic_list:
            if not line.strip(): continue
			
            y = re.sub(r'(^.*?)( )(.*)', r'\g<1>,  \g<3>', line)
            x = y.split(',')
            a=x[0]
            
            b=x[1]
            a=a.upper()
            
            c=a+b
           # print(c)
           # c=re.sub(',', '   ')
            blankTXT += c
        blankTXT += "\n"        
        print(all_dic[kek])
        kek += 1
     #   print(c)
    print(dic_list)
    ff = open('raw_ARPAbet.txt', 'w', encoding='utf-8') #latin-1 #utf-8
	
    ff.write(blankTXT)
    ff.close()
    dic_list.close()
    print('raw_ARPAbet.txt was successfuly created')
    
try:
    print('Do you wish to create new "raw_ARPAbet.txt"? \nY or N')
    ######rawARPAbet()
    con1 = input()
    if (con1 == 'Y') or (con1 == 'y'):
        print('creating raw_ARPAbet.txt, please wait ~30 seconds for code to complete')
        rawARPAbet()
        
    print("PART A complete, use PART B")

except:
    print("""raw_ARPAbet.txt do not exist or cannot be created,
          check if the folder 'dictionariesIPA' exist in same directory as
          PY file and if it contains text files (encode UTF-8)""")
    print(kek)
