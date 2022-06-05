import nltk
import Languages.English.MultipleRules as MultipleRules
import re
from Languages.Latvian import IPAtoLatRules
from Languages.English import MultipleRules

# Metode, kas pārveido IPA formu uz latviešu rakstību
def toLatvian(phones,uppercase):
    result = ""
    first = uppercase
    for phone in phones:
        letter = ""
        if(phone[-1] == "0" or phone[-1] == "1" or phone[-1] == "2"):
            letter = phone[0:-1]
        else:
            letter = phone
        result += IPAtoLatRules.IPAtoLat[letter][first]
        first = 0
    return result

    

def pronounce(original,word,dict,space):
    try:
        phones = dict.get(word) # Iegūstam vārda izrunas.
        case = 0 
        if(original[0].istitle()):# Noskaidrojam, vai vārds sākas ar lielo burtu.
            case = 1
        result = toLatvian(phones[0],case) # Iegūstam latviešu rakstību.
        return space + result # Pievienojam vaļu klāt rezultātam.
    except Exception as e:
        return word

# Galvenā metode
def main():
    arpabet = nltk.corpus.cmudict.dict() # Iegūstam vārdnīcu

    languageFrom = "English" # Valoda no kuras transliterēt
    languageTo = "Latvian" # Valoda uz kuru transliterēt

    string = "I run with my friends. You run with your friends." # Teikums, kuru jātransliterē

    Sentence = nltk.pos_tag(nltk.word_tokenize(string)) # Iegūstam katrai teikuma daļai vārdšķiru
    Words = nltk.word_tokenize(string.lower()) # Sadalam katru teikuma daļu pa vārdiem/pieturzīmem

    print(Sentence)
    print(Words)

    result = "" # Transliterēšanas rezultāts
    # Ejam cauri katrai teikuma daļai
    for x in range(len(Sentence)):
        if(x == 0 or Words[x] == "."):
            result += pronounce(Sentence[x],Words[x],arpabet,"")
        else:
            result += pronounce(Sentence[x],Words[x],arpabet," ")
        
    print(result)

main()