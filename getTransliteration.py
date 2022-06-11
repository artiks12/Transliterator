from transliterateTo import *
from Languages.Latvian.IPAtoLatRules import IPAtoLat

# Main function for getting transliteration result
def getTransliteration(ipa,text,languageTo):
    if(languageTo == "latvian"):
        return transliterateTo(ipa,text,IPAtoLat)