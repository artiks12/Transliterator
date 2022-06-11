import nltk
from regex import W
import Languages.English.MultipleRules as MultipleRules
import re
from Languages.Latvian import IPAtoLatRules
from Languages.English import MultipleRules
import Transliterator
from pathlib import Path

languageFrom = "american"
languageTo = "latvian"

languagesFrom = [ "british" , "american"]
languagesTo = [ "latvian" ] 

# Galvenā metode
def transliterate(text):
    arpabet = nltk.corpus.cmudict.dict() # Iegūstam vārdnīcu

    string = text # Teikums, kuru jātransliterē

    Sentence = nltk.pos_tag(nltk.word_tokenize(string)) # Iegūstam katrai teikuma daļai vārdšķiru
    Words = nltk.word_tokenize(string.lower()) # Sadalam katru teikuma daļu pa vārdiem/pieturzīmem

    print(Sentence)
    print(Words)

    result = "" # Transliterēšanas rezultāts
    # Ejam cauri katrai teikuma daļai
    for x in range(len(Sentence)):
        if(x == 0 or Words[x] == "."):
            result += Transliterator.pronounce(Sentence[x],Words[x],arpabet,"")
        else:
            result += Transliterator.pronounce(Sentence[x],Words[x],arpabet," ")
        
    print(result)

def main():
    print("Welcome to interlanguage phonetical transliterator!")
    print('To see all comand, type "help" or "h".')
    command = ""
    while command != "q" and command != "quit":
        command = input("> ")
        method = command.split()

        if(command != ""):
            if(method[0] == "t" or method[0] == "transliterate"):
                if(len(method) == 2):
                    transliterate(method[1])
                elif(len(method) == 1):
                    print("No text given.")
                else:
                    print("Too many arguments given.")
            
            elif(method[0] == "p" or method[0] == "parse"):
                if(len(method) == 2):
                    my_file = Path(method[1])
                    if my_file.is_file():
                        f = open(method[1],'r')
                        text = f.read()
                        print(text)
                        transliterate(text)
                        f.close()
                    else:
                        print("File doesn't exist. Is the path or file name specified correectly?")
                elif(len(method) == 1):
                    print("No file given.")
                else:
                    print("Too many arguments given.")

            elif(method[0] == "s" or method[0] == "set"):
                if(len(method) == 3):
                    if(method[1] in languagesFrom and method[2] in languagesTo):
                        languageFrom = method[1]
                        languageTo = method[2]
                    else:
                        if(not(method[1] in languagesFrom)):
                            print(method[1] + ' is either not given in lowercase or is not supported as a value for "languageFrom"')
                        if(not(method[2] in languagesTo)):
                            print(method[2] + ' is either not given in lowercase or is not supported as a value for "languageTo"')
                elif(len(method) == 2):
                    print('Missing argument "languageTo"')
                elif(len(method) == 1):
                    print('Missing arguments "languageFrom" and "languageTo"')
                else:
                    print("Too many arguments given.")
            

            elif(method[0] == "l" or method[0] == "languages"):
                if(len(method) == 1):
                    print("language from: " + languageFrom)
                    print("language to: " + languageTo)
                else:
                    print("Too many arguments given.")

            elif(method[0] == "h" or method[0] == "help"):
                if(len(method) == 1):
                    print("--help or h:             shows commands. No arguments.")
                    print("--languages or l:        shows set languages. No arguments.")
                    print("--parse or p:            get text from file and transliterates it. Takes file path as argument.")
                    print("--quit or q:             stops program. No arguments.")
                    print("--set or s:              sets languages. Takes two strings as argument: language from and language to.")
                    print("--transliterate or t:    shows commands. Takes a text as argument.")
                else:
                    print("Too many arguments given.")
            
            elif(method[0] != "q" and method[0] != "quit"):
                print("command " + command + " doesn't exist.")

            else:
                if(len(method) > 1):
                    print("Too many arguments given.")
                    command = ""
                


main()