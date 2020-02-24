import os
import os.path
import re


testSentence = "hello mister DEGOOD, how are you.wav|hello mister DEGOOD, how are you?;"

justTextTest = """

"DEGER" : "{D IY1 G ER0}", 
        "DEGIACOMO" : "{D IY1 JH AH0 K OW0 M OW0}", 
        "DEGIDIO" : "{D IH0 JH IY1 D IY0 OW0}", 
        "DEGIROLAMO" : "{D IH0 JH IH0 R OW0 L AA1 M OW0}", 
        "DEGLER" : "{D EH1 G L ER0}", 
        "DEGNAN" : "{D EH1 G N AH0 N}", 
        "DEGNER" : "{D EH1 G N ER0}", 
        "DEGOOD" : "{D EH1 G UH0 D}", 
        "DEGRAAF" : "{D EH1 G R AA0 F}", 

"""
def wordSwap(sentence, dictionary):
    sentence = sentence.upper() #convert all letters to upper for dictionary
    sentence = sentence.replace(',', ' -comma- ') #remove comma
    sentence = sentence.replace('.', ' -dot- ')
    sentence = sentence.replace(':', ' -colon- ') 
    sentence = sentence.replace('!', ' -exclamation- ')
    sentence = sentence.replace('?', ' -question- ')
    sentence = " ".join([dictionary.get(w,w) for w in sentence.split()]) #normal words to ARPAbet words
    sentence = sentence.replace(' -comma- ', ',') #get comma (and all other junk) back 
    sentence = sentence.replace(' -colon- ', ':')
    sentence = sentence.replace(' -exclamation- ', '!')
    sentence = sentence.replace(' -question- ', '?')
    sentence = sentence.replace(' -dot- ', '.')
    sentence = sentence.replace('-comma-', ',')
    sentence = sentence.replace('-colon-', ':') 
    sentence = sentence.replace('-exclamation-', '!')
    sentence = sentence.replace('-question-', '?')
    sentence = sentence.replace('-dot- ', '. ')
    sentence = sentence.replace(' -dot-', ' .')
    return sentence 


file = open('raw_ARPAbet.txt', 'r')

dictionaryARPAbet={}


happy=0
try:
    
    for line in file:
        if not line.strip(): continue
        
        y = re.sub(r'(^.*?)( )(.*?$)', r'\g<1>,\g<3>', line)
        x = y.split(',')
        happy += 1
        a=x[0]
        b=x[1]
        c=len(b)-1
        b=b[0:c]
        b= """{""" + b.strip() + """}"""
        dictionaryARPAbet[a]=b

        
    print("""paste directory here (example: C:\Folder\Val_text.txt) """)
    
    getFile = open(input(), "r") 
    smallWords = getFile.read()


    bigWords = getFile.read().upper()

    getSplit = re.split(r'(?<=\|)(.*?)(?=\;)', smallWords)

    #dictionaryARPAbet
    y = 1
    for lines in getSplit:
        y = y+1

    textPrint = ""
    x=1
    for lines in getSplit:
        if not x % 2:
            lines = lines.upper()
            lines = wordSwap(lines, dictionaryARPAbet)
            textPrint = textPrint + lines
            #print(lines)
        ###print(lines, x)
        if x % 2:
            textPrint = textPrint + lines
        x = x+1
        
        #print(textPrint)
        if x == y:
            print(textPrint)
            f = open("OUTPUT_ARPAbet.txt", "w")
            f.write(textPrint)
            f.close()


    smallWords.close()
    file.close()
##############################################################   
except:
    print("""some error happen, check if you have following files in same folder- 
            PART A.py, PART B.py, raw_ARPAbet.txt, _ARPAbet.txt""")

    print(str(happy) + "<-- check this line in complied ARPAbet text file, if its same as last line than its just falsepositive")
    print("or there is some techical error in orginal dialogue text files")
    print("however if its not than it could be an empty line in that file, open it with notepad++ and use below Regex to find and remove them all")
    print("""^(?:[\\t ]*(?:\\r?\\n|\\r))+""")
###################################################################################


def finalRun():
    print("""paste directory here (example: C:\Folder\Val_text.txt) """)
    
    getFile = open(input(), "r") 
    smallWords = getFile.read()


    bigWords = getFile.read().upper()

    getSplit = re.split(r'(?<=\|)(.*?)(?=\;)', smallWords)

    #dictionaryARPAbet
    y = 1
    for lines in getSplit:
        y = y+1

    textPrint = ""
    x=1
    for lines in getSplit:
        
        if not x % 2:
            lines = lines.upper()
            lines = wordSwap(lines, dictionaryARPAbet)
            textPrint = textPrint + lines
            #print(lines)
        ###print(lines, x)
        if x % 2:
            textPrint = textPrint + lines
        x = x+1
        
        #print(textPrint)
        if x == y:
            print(textPrint)
            f = open("OUTPUT_ARPAbet.txt", "w")
            f.write(textPrint)
            f.close()


    smallWords.close()

    
