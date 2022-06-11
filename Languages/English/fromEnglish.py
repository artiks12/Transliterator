import nltk
from Languages.English.region import *
from Languages.English.partOfSpeach import *
from PrepareDictionary import *
from Languages.English.Dictionary import *

# Main function for getting english pronounciations
def fromEnglish(text,language):
    arpabet = nltk.corpus.cmudict.dict() # Gets the dictionary

    Sentence = nltk.pos_tag(nltk.word_tokenize(text)) # Gets part of speach for each word
    words = nltk.word_tokenize(text.lower()) # Gets every word of settence in lowercase

    result = [] # resulting list of pronounciations
    
    # gets pronounciations for every single word, depending on region
    for x in range(len(Sentence)):
        if(language == "british"):
            result.append(pronounceRegion(Sentence[x],words[x],arpabet,british))
        if(language == "american"):
            result.append(pronounceRegion(Sentence[x],words[x],arpabet,american))
        
    return result

# gets pronounciations for a word, depending on region
def pronounceRegion(original,word,dict,region):
    try:
        phones = dict.get(word) # Gets all pronounciations
        # Pronounciation not found or the given word is not a word
        if(len(phones) == 0):
            # given word is not a word
            if(original[0] == original[1]):
                return [original[0]]
            # Pronounciation not found
            else:
                return ["/"+original[0]+"/"]
        else:
            # pronounciation of word is region specific
            if(word in region):
                return region[word]
            # pronounciation of word is part of speach specific
            elif(word + original[1] in PoT):
                search = word + original[1]
                return PoT[search]
            elif(word in Dictionary):
                return Dictionary[word]
            # Default
            else:
                return phones[0]
    except Exception as e:
        return word