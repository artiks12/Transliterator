import nltk

# Function for transliterating words from IPA to specified language.
def transliterateTo(ipa,text,rules):
    words = nltk.word_tokenize(text) # get all words in their original forms for lowercase/uppercase
    result = "" # transliteration result

    # Go through every single word
    for x in range(len(ipa)):
        # Add spaces to result if it is not the begining of setence.
        if(x!=0 and words[x] != '.'):
            result+=" "
        letter = ""

        # Case when the list element is either not a word or has no pronounciation found
        if(len(ipa[x]) == 1 and ipa[x][0] == words[x]):
            result += words[x]
        else:
            first = 1 # Marks the begining of a word
            for phone in ipa[x]:
                # Removes stresses
                if(phone[-1] == "0" or phone[-1] == "1" or phone[-1] == "2"):
                    letter = phone[0:-1]
                else:
                    letter = phone
                
                # Checks word case and changes sounds to letters
                if(words[x].isupper()):
                    result += rules[letter][1]
                elif(words[x].istitle()):
                    result += rules[letter][first]
                    if(first == 1):
                        first = 0
                else:
                    result += rules[letter][0]
    
    return result