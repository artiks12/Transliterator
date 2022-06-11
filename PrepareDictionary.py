import nltk
import re

# Function for getting list as string
def listToString(lists): 
    
    # initialize an empty string
    str1 = "[" 
    firstList = True
    
    # traverse in the string  
    for list in lists: 
        if(firstList == True):
            firstList = False
        else:
            str1 += ','
        str1 += "["
        firstSound = True
        for sound in list:
            if(firstSound == True):
                firstSound = False
            else:
                str1 += ','
            str1 += "'" + sound + "'"
        str1 += "]"
    str1 += "]"
            
    # return string  
    return str1

# function for getting phonetics without stresses
def get_phonetics(item):
    result = []
    for phone in item:
        if(phone[-1] == "0" or phone[-1] == "1" or phone[-1] == "2"):
            result.append(phone[0:-1])
        else:
            result.append(phone)
    return result

# function that makes a dictionary where words have no stresses
def prepareDictionary():
    arpabet = nltk.corpus.cmudict.dict()
    my_dict = {}

    # goes through every entry in nltk dictionary
    for key, value in arpabet.items():
        result = []
        # goes through every pronounciation in an entry
        for item in value:
            unique = True
            phone = get_phonetics(item) # Gets phonetics with no stresses
            # Goes through result list
            for check in result:
                # the length for both phonemes is not equal, therefore it is unique
                if(len(phone) != len(check)):
                    continue
                else:
                    unique = False
                    # checks every sound in phones
                    for x in range(len(check)):
                        if(check[x] != phone[x]):
                            unique = True
                            break
                    if(unique == False):
                        break
            if(unique == True):
                result.append(phone)
        my_dict[key] = result
    return my_dict

def printDictionary():
    dict = prepareDictionary()
    # Creates a Dictionary.py file
    f = open("Dictionary.py", "w")
    f.write("Dictionary = {\n")
    for key, value in dict.items():
        if("'" in key and not("'s" in key) and not(key[-1] == "'") and not(key.startswith("o'")) and not(key.endswith("'t"))):
            if("'" in key):
                string = "    " + '"' + key + '":' + listToString(value) + ",\n"
                f.write(string)
            elif('"' in key):
                string = "    " + "'" + key + "':" + listToString(value) + ",\n"
                f.write(string)
            else:
                string = "    " + '"' + key + '":' + listToString(value) + ",\n"
                f.write(string)
            
    f.write("}")
    f.close()