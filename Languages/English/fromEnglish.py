import nltk
from Languages.English.region import *
from Languages.English.partOfSpeach import *
from Languages.English.Dictionary import *
from PrepareDictionary import *
from Punctuations import *


# Part of speech tags
POS = [
    "CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNS","NNP","NNPS","PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","TO","UH","VB","VBG","VBD","VBN","VBP","VBZ","WDT","WP","WRB"
]

# Gets word case
def case(text):
    if(text.isupper() and len(text) > 1):
        return 'UPPER'
    elif(text.istitle() or (text.isupper() and len(text) == 1)):
        return 'TITLE'
    else:
        return 'LOWER'

# Main function for getting english pronounciations
def fromEnglish(text,language,single):
    dict = prepareDictionary()
    region = {}

    # Sets region specific dictionary
    if(language == "british"):
        region = british
    if(language == "american"):
        region = american

    Sentence = nltk.pos_tag(nltk.word_tokenize(text)) # Gets part of speach for each word
    words = nltk.word_tokenize(text.lower()) # Gets every word of settence in lowercase

    result = [] # resulting list of pronounciations
    
    # gets pronounciations for every single word, depending on region
    count = 0
    for x in range(len(Sentence)):
        token = words[x]
        original = Sentence[x][0]
        pos = Sentence[x][1]

        # Fixes double quotes
        if(original == "''" or original == "``"):
            original = '"'
            token = '"'

        # Cases when token starts with apostrophe
        if(original.startswith("'")):
            # Cases when token is an apostrophe
            if(original == "'"):
                count-=1
                result[count].append("'")
                result[count].append(case(Sentence[x-1][0]))
                count+=1 
            # Special case "I'm"
            elif(words[x-1]+words[x] == "i'm"):
                count-=1
                result[count] = ['AY',"'",'M','/','AH',"'",'M']
                if(case(Sentence[x-1][0]) == 'UPPER'):
                    result[count].append('TITLE')
                else:
                    result[count].append('LOWER')
                count+=1
            # Checks if given token is in dictionary with words, that have apostrophe
            elif(original in apostrophes):
                result.append(apostrophes[original][0])
                result[count].append(case(Sentence[x-1][0]))
                count+=1
            # Other cases
            else:
                # Form 's
                if(pos == "POS" or pos == "VBZ"):
                    count-=1
                    result[count].pop()
                    result[count].append("'")
                    result[count].append("Z")
                    result[count].append(case(Sentence[x-1][0]))
                    forw=0
                    for y in range(len(result[count])):
                        if(result[count][y+forw] == '/'):
                            result[count].insert(y,"Z")
                            result[count].insert(y,"'")
                            forw+=2
                    count+=1
                # Forms 'll, 've, 'd and 're
                elif(pos == "MD" or pos == "VBP" or pos == "VBD"):
                    count-=1
                    token = words[x-1]+words[x]
                    original = Sentence[x-1][0]+Sentence[x][0]
                    pos = Sentence[x-1][1]
                    result[count] = pronounceRegion(original,pos,token,dict,region,single)
                    if(case(Sentence[x-1][0]) == 'UPPER'):
                        result[count].append('TITLE')
                    else:
                        result[count].append('LOWER')

                    # Form 'll
                    if(words[x] == "'ll"):
                        if(result[count][-3] == "AH"):
                            result[count].insert(-3,"'")
                        else: 
                            result[count].insert(-2,"'")
                        forw = 0
                        for y in range(len(result[count])):
                            if(result[count][y+forw] == '/'):
                                if(result[count][y+forw-2] == "AH"):
                                    result[count].insert(y-2,"'")
                                else: 
                                    result[count].insert(y-1,"'")
                                forw+=1
                    
                    # Form 've
                    elif(words[x] == "'ve"):
                        if(result[count][-3] == "AH" or result[count][-3] == "IH"):
                            result[count].insert(-3,"'")
                        else: 
                            result[count].insert(-2,"'")
                        forw = 0
                        for y in range(len(result[count])):
                            if(result[count][y+forw] == '/'):
                                if(result[count][y+forw-2] == "AH" or result[count][y+forw-2] == "IH"):
                                    result[count].insert(y-2,"'")
                                else: 
                                    result[count].insert(y-1,"'")
                                forw+=1

                    # Form 'd
                    elif(words[x] == "'d"):
                        if(result[count][-3] == "AH"):
                            result[count].insert(-3,"'")
                        else: 
                            result[count].insert(-2,"'")
                        forw = 0
                        for y in range(len(result[count])):
                            if(result[count][y+forw] == '/'):
                                if(result[count][y+forw-2] == "AH"):
                                    result[count].insert(y-2,"'")
                                else: 
                                    result[count].insert(y-1,"'")
                                forw+=1
                    
                    # Form 're
                    elif(words[x] == "'re"):
                        if(token == "if_you're"):
                            result[count].insert(2,"_") 
                            result[count].insert(-2,"'") 
                        else:
                            result[count].insert(-2,"'") 
                            forw = 0
                            for y in range(len(result[count])):
                                if(result[count][y+forw] == '/'):
                                    result[count].insert(y+forw-1,"'")
                                    forw+=1
                    count+=1
                                
                # All other cases
                else:
                    result.append(pronounceRegion(original,pos,token,dict,region,single))
                    result[count].insert(0,"'")
                    result[count].append(case(Sentence[x-1][0])) 
                    count+=1
        
        # Form 't
        elif(original.startswith("n't")):
            count-=1
            token = words[x-1]+words[x]
            original = Sentence[x-1][0]+Sentence[x][0]
            pos = Sentence[x-1][1]
            result[count] = pronounceRegion(original,pos,token,dict,region,single)
            
            # can't has different fronounciations for british and american
            if(token != "can't"):
                if(result[count][-1] == "T"):
                    result[count].insert(len(result[count])-1,"'")
                else:
                    result[count].append("'")
                forw = 0
                for y in range(len(result[count])):
                    if(result[count][y+forw] == '/'):
                        result[count].insert(y+forw-1,"'")
                        forw+=1
            result[count].append(case(Sentence[x-1][0]))
            count+=1
    
        # Checks if given token is in dictionary with words, that have apostrophe
        elif(original in apostrophes):
            result.append(apostrophes[original][0])
            result[count].append(case(Sentence[x-1][0]))
            count+=1

        # Words that have -
        elif('-' in original):
            # Split word into parts, that are divided by -
            tokenParts = token.split('-')
            originalParts = original.split('-')
            list = []
            first = 1
            c = 'LOWER'
            # Go through every single word
            for y in range(len(tokenParts)):
                r = []
                # Get pronounciations of word and add -
                temp = pronounceRegion(originalParts[y],pos,tokenParts[y],dict,region,single)
                if(first == 1):
                    first = 0
                    c = case(originalParts[y])
                else:
                    for l in list:
                        l.append('-')
                
                # Seperate pronounciations into lists, if a word has multiple pronounciations
                variant = []
                if('/' in temp):
                    for t in temp:
                        if(t == '/'):
                            r.append(variant)
                            variant = []
                        else:
                            variant.append(t)
                    r.append(variant)
                else:
                    for t in temp:
                        variant.append(t)
                    r.append(variant)
                
                # Combine the word with everything found so far
                combined = []
                if(len(list) == 0):
                    for a in r:
                        combined.append(a)
                else:
                    for l in list:
                        for a in r:
                            combined.append(l+a)
                list = combined
            
            # Combine all variants together in a single list
            first = 1
            finish = []
            for l in list:
                if(first == 1):
                    first = 0
                else:
                    finish.append('/')
                for elem in l:
                    finish.append(elem)

            finish.append(c)
            result.append(finish)
            count+=1

        # All other cases
        else:
            result.append(pronounceRegion(original,pos,token,dict,region,single))
            # For words that are longer than 1 symbol, check if the word is in a form, where first symbol is a letter and second is an apostrophe
            if(len(words[x]) > 1):
                if((words[x][1] == "'" and words[x][0] != "'") and not(token == "c'mon" or token == "m'bow")):
                    result.insert(1,"'")
                else:
                    if(token == "c'mon"):
                        result.insert(2,"'")
                    if(token == "m'bow"):
                        result.insert(1,"'")
                        result.insert(7,"'")
            result[count].append(case(original))
            count+=1
        
    return result

# gets pronounciations for a word, depending on region
def pronounceRegion(original,pos,word,dict,region,single):
    phones = dict.get(word) # Gets all pronounciations
    
    # Punctuation
    if(isPunctuation(original) or isIncloser(original)):
        return [original]

    # Paragraph
    elif(single == 0):
        # Custom word
        if(word in Dictionary):
            return getNewElement(Dictionary[word])
        
        # Custom word dependent on part of speech tag
        elif(word+pos in Dictionary):
            search = word + pos
            return getNewElement(Dictionary[search]) 

        # pronounciation of word is region specific
        elif(word in region):
            return getNewElement(region[word])
        
        # pronounciation of word is part of speach specific
        elif(word + pos in PoT):
            search = word + pos
            return getNewElement(PoT[search])
        
        # pronounciation of word is region and part of speach specific
        elif(word + pos in region):
            search = word + pos
            return getNewElement(region[search])
        
        # there is only one pronounciation for word
        elif(len(phones) == 1):
            return getNewElement(phones[0])
        
        # Default
        elif(phones != None):
            return getNewElement(getSingle(word,Dictionary,region,phones))

        # Pronounciation not found
        else:
            return ["/"+original+"/"]
    
    # One Word
    else:
        # Gets all pronounciations
        result = getNewElement(getSingle(word,Dictionary,region,phones))
        if(len(result) == 0):
            return ["/"+original+"/"]
        return result
            
        

# Gets all pronounciations of single word
def getSingle(word,Dictionary,region,phones):
    
    # pronounciation of word is in custom dictionary
    if(word in Dictionary):
        return Dictionary[word]

    # pronounciation of word is in custom dictionary and part of speech specific
    else:
        result = []
        first = 1
        for pos in Dictionary:
            if(pos.startswith(word) and pos[len(word):] in POS):
                if(first == 1):
                    first = 0
                else:
                    result.append('/')
                for item in Dictionary[pos]:
                    result.append(item)
        if(len(result) != 0):
            return result

    # pronounciation of word is region specific
    if(word in region):
        return region[word]
    
    # pronounciation of word is region and part of speech specific
    else:
        result = []
        first = 1
        for pos in region:
            if(pos.startswith(word) and pos[len(word):] in POS):
                if(first == 1):
                    first = 0
                else:
                    result.append('/')
                for item in region[pos]:
                    result.append(item)
        if(len(result) != 0):
            return result
    
    # default search
    result = []
    first = 1
    for phone in phones:
        if(first == 1):
            first = 0
        else:
            result.append('/')
        for item in phone:
            result.append(item)
    return result

def getNewElement(phones):
    result = []
    for p in phones:
        result.append(p)
    return result