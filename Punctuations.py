# Determines if given symbol is a punctuation symbol
def isPunctuation(s):
    return s == '.' or s == '!' or s == '...' or s == '?' or s == ',' or s == ':' or s == ';'

# Determines if given symbol is a inclosing symbol
def isIncloser(s):
    return s == '"' or s == '(' or s == ")" or s == '{' or s == "}" or s == '[' or s == "]"