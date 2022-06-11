import nltk

# Function for transliterating words from IPA to specified language.
def transliterateTo(ipa,text,rules):
    sentence = nltk.pos_tag(nltk.word_tokenize(text)) # Gets part of speach for each word
    words = nltk.word_tokenize(text) # get all words in their original forms for lowercase/uppercase
    result = "" # transliteration result

    count = 0
    # Go through every single word
    for x in range(len(ipa)):
        if(words[count].startswith("'") and (sentence[count] == 'MD' or sentence[count] == "POS" or sentence[count] == "VBZ" or sentence[count] == 'RB')):
            count+=1
        # Add spaces to result if it is not the begining of setence.
        if(x!=0 and words[count] != '.'):
            result+=" "
        letter = ""

        # Case when the list element is either not a word or has no pronounciation found
        if(len(ipa[x]) == 1 and ipa[x][0] == None):
            result += words[count]
        else:
            first = 1 # Marks the begining of a word
            for phone in ipa[x]:
                letter = phone
                
                # Checks if the symbol is a letter
                if(not(letter in rules)):
                    result += letter
                else:
                    # Checks word case and changes sounds to letters
                    if(words[count].isupper()):
                        result += rules[letter][1]
                    elif(words[count].istitle()):
                        result += rules[letter][first]
                        if(first == 1):
                            first = 0
                    else:
                        result += rules[letter][0]
        count+=1

    return result