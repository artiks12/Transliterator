from Languages.English.fromEnglish import fromEnglish

# Main function for getting pronounciations
def getIPA(text,languageFrom):
    if(languageFrom == "british" or languageFrom == "american"):
        return fromEnglish(text,languageFrom)