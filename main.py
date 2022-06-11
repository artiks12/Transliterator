from pathlib import Path
from getIPA import getIPA
from getTransliteration import getTransliteration
from PrepareDictionary import *

languagesFrom = [ "british" , "american"] # Supported languages from witch text can be transliterated.
languagesTo = [ "latvian" ] # Supported languages to witch text can be transliterated.

# Gets the text after function name
def getSetence(command):
    space = False
    for x in range(len(command)):
        if(space == False and command[x] == " "):
            space = True
        if(space == True and command[x] != " "):
            return command[x:len(command)]

# Main transliteration function
def transliterate(text,languageFrom,languageTo,single):

    ipa = getIPA(text,languageFrom,single) # Gets list of word pronounciations
    
    result = getTransliteration(ipa,text,languageTo) # Gets transliteration result

    print(result) # Outputs the result
    

# Interface code
def main():
    #prepareDictionary()

    printDictionary()

    print(nltk.pos_tag)

    languageFrom = "american" # Default values for languageFrom
    languageTo = "latvian" # Default values for languageTo

    print("Welcome to interlanguage phonetical transliterator!")
    print('To see all comand, type "help" or "h".')
    command = ""
    
     # Programm works as long as we don't make it stop with "q" or "quit" command
    while command != "q" and command != "quit":
        command = input("> ")
        method = command.split()

        # Checks whether any command is typed
        if(command != ""):
            # "transliterate" command
            if(method[0] == "t" or method[0] == "transliterate"):
                if(len(method) >= 2):
                    transliterate(getSetence(command),languageFrom,languageTo,0)
                elif(len(method) == 1):
                    print("No text given.")
            
            # "parse" command
            elif(method[0] == "p" or method[0] == "parse"):
                if(len(method) == 2):
                    my_file = Path(method[1])
                    if my_file.is_file():
                        f = open(method[1],'r')
                        text = f.read()
                        print(text)
                        transliterate(text,languageFrom,languageTo,0)
                        f.close()
                    else:
                        print("File doesn't exist. Is the path or file name specified correectly?")
                elif(len(method) == 1):
                    print("No file given.")
                else:
                    print("Too many arguments given.")

            # "set" command
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
            
            # "languages" command
            elif(method[0] == "l" or method[0] == "languages"):
                if(len(method) == 1):
                    print("language from: " + languageFrom)
                    print("language to: " + languageTo)
                else:
                    print("Too many arguments given.")

            # "help" command
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
            
            # Transliterates a single word. Gets all pronounciations
            elif(method[0] == "w" or method[0] == "word"):
                if(len(method) == 2):
                    transliterate(method[1],languageFrom,languageTo,1)
                elif(len(method) == 1):
                    print("No text given.")
                else:
                    print("Too many arguments given.")

            # Check part of speach tags for every word in text.
            elif(method[0] == "pos" or method[0] == "partOfSpeach"):
                if(len(method) >= 2):
                    sentence = getSetence(command)
                    print(nltk.pos_tag(nltk.word_tokenize(sentence)))
                elif(len(method) == 1):
                    print("No text given.")
            
            # Anything that is not a proper command
            elif(method[0] != "q" and method[0] != "quit"):
                print("command " + command + " doesn't exist.")

            # Makes sure, that "quit" command doesn't take any arguments
            else:
                if(len(method) > 1):
                    print("Too many arguments given.")
                    command = ""
            

main()