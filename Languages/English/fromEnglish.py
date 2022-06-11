from asyncio.windows_events import NULL
from re import L
import nltk
from Languages.English.region import *
from Languages.English.partOfSpeach import *
from PrepareDictionary import *

POS = [
    "CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNS","NNP","NNPS","PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","TO","UH","VB","VBG","VBD","VBN","VBP","VBZ","WDT","WP","WRB"
]

def isPunctuation(s):
    return s == '.' or s == '!' or s == '...' or s == '?' or s == ',' or s == ':' or s == ';' or s == '-'

# Main function for getting english pronounciations
def fromEnglish(text,language,single):
    dict = prepareDictionary()
    region = {}

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
        
        if(Sentence[x][0].startswith("'")):
            if(Sentence[x][0] == "'"):
                result[count-1].append("'") 
            else:
                if(Sentence[x][1] == "POS" or Sentence[x][1] == "VBZ"):
                    result[count-1].append("'")
                    result[count-1].append("Z")
                elif(not(Sentence[x][1] == "MD")):
                    result.append(pronounceRegion(Sentence[x],words[x],dict,region,single))
                    result[count].insert(0,"'")
                    count+=1
                else:
                    result[count-1] = pronounceRegion(Sentence[x-1]+Sentence[x],words[x-1]+words[x],dict,region,single)
        
        elif(Sentence[x][0].startswith("n't")):
            result[count-1] = pronounceRegion(Sentence[x-1]+Sentence[x],words[x-1]+words[x],dict,region,single)
            print(words[x-1]+words[x])
            if(words[x-1]+words[x] != "can't"):
                if(result[count-1][-1] == "T"):
                    result[count-1].insert(len(result[count-1])-1,"'")
                else:
                    result[count-1].append("'")
                forw = 0
                for x in range(len(result[count-1])):
                    if(result[count-1][x+forw] == '/'):
                        result[count-1].insert(x-1,"'")
                        forw+=1
            
            print(result[count-1])
        
        else:
            result.append(pronounceRegion(Sentence[x],words[x],dict,region,single))
            if(words[x].startswith("o'")):
                result[count].insert(1,"'")
            count+=1
            
        
    return result

# gets pronounciations for a word, depending on region
def pronounceRegion(original,word,dict,region,single):
    try:
        phones = dict.get(word) # Gets all pronounciations
        # Pronounciation not found or the given word is not a word
        if(phones == None):
            # given word is not a word
            if(isPunctuation(original[0])):
                return [original[0]]
            # Pronounciation not found
            else:
                return ["/"+original[0]+"/"]
        elif(single == 1):
            return getSingle(word,region,phones)
        else:
            # pronounciation of word is region specific
            if(word in region):
                return region[word]
            # pronounciation of word is part of speach specific
            elif(word + original[1] in PoT):
                search = word + original[1]
                return PoT[search]
            # pronounciation of word is region and part of speach specific
            elif(word + original[1] in region):
                search = word + original[1]
                return region[search]
            # there is only one pronounciation for word
            elif(len(phones) == 1):

                return phones[0]
            # Default
            else:
                return getSingle(word,region,phones)
                
    except Exception as e:
        return word

def getSingle(word,region,phones):
    # pronounciation of word is region specific
    if(word in region):
        return region[word]
    
    # pronounciation of word is region and part of speach specific
    else:
        result = []
        first = 1
        for pos in region:
            if(pos.startswith(word) and pos[len(word):] in POS):
                print(pos)
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