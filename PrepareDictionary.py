import nltk
import re

# Function to convert  
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

def get_phonetics(item):
    result = []
    for phone in item:
        if(phone[-1] == "0" or phone[-1] == "1" or phone[-1] == "2"):
            result.append(phone[0:-1])
        else:
            result.append(phone)
    return result


arpabet = nltk.corpus.cmudict.dict()
my_dict = {}
count1 = 0
count2 = 0

for key, value in arpabet.items():
    result = []
    for item in value:
        unique = True
        phone = get_phonetics(item)
        for check in result:
            if(len(phone) != len(check)):
                continue
            else:
                unique = False
                for x in range(len(check)):
                    if(check[x] != phone[x]):
                        unique = True
                        break
                if(unique == False):
                    break
        if(unique == True):
            result.append(phone)
    my_dict[key] = result

f = open("Dictionary.py", "w")
f.write("TwoOrMore = {\n")
for key, value in my_dict.items():
    string = "    " + '"' + key + '":' + listToString(value) + ",\n"
    f.write(string)
        
f.write("}")
f.close()

        

