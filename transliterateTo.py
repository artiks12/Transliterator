import nltk
from Punctuations import *

# Function for transliterating words from IPA to specified language.
def transliterateTo(ipa,rules):
    result = "" # transliteration result

    # Go through every single word
    for x in range(len(ipa)):
        list = []
        case = 0
        if(ipa[x][-1] == 'UPPER'):
            case = 1
        elif(ipa[x][-1] == 'TITLE'):
            case = -1
        ipa[x].pop()
        
        # Add spaces to result if it is not the begining of setence.
        if(x!=0 and not(isPunctuation(ipa[x][0]) or isIncloser(ipa[x][0]))):
            if(isIncloser(ipa[x-1][0])):
                result+=""
            else:
                result+=" "
        letter = ""

        # Case when the list element is either not a word or has no pronounciation found
        first = 1
        word = ""
        for y in range(len(ipa[x])):
            letter = ipa[x][y]
            
            # Symbol is not a letter. Prevents the same result multiple times
            if(not(letter in rules)):
                if(letter == "/"):
                    if(y!=0 and y!=len(ipa[x])-1):
                        if(not(word in list)):
                            list.append(word)
                        if(case == -1):
                            first = 1
                        word = ""
                else:
                    word += letter
                
            else:
                # Checks word case and changes sounds to letters
                if(case == 1):
                    word += rules[letter][1]
                elif(case == -1):
                    word += rules[letter][first]
                    if(first == 1):
                        first = 0
                else:
                    word += rules[letter][0]
        
        # There is only one pronunciation result for the word 
        if(len(list) == 0):
            result += word
        # There are multiple pronunciation results for the word 
        else:
            if(not(word in list)):
                list.append(word)
            for x in range(len(list)):
                if(x!=0):
                    result+='/'
                result+=list[x]

    return result