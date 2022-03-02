



def searchSuggestions(repository,customerQuery):
  
  ##The function is expected to return a 2D_STRING_ARRAY.
  # The function accepts following parameters:
  # STRING_ARRAY repository 
  # 2. STRING customerQuery 
  
def compareWords(input, word):
    equal = 0
    i = 0
    for char in input:
        if char == word[i]:
            equal += 1
        i += 1
    return equal
            

def searchSuggestions(repository, customerQuery):
    wordList = []
    for word in repository:
        equalLevel = compareWords(customerQuery, word)
    if wordList.length() == 0:
        wordList.append(word)
    else:
        for item in wordList:
            if equalLevel > compareWords(customerQuery, item):
                wordList.append(word)
            elif equalLevel == compareWords(customerQuery, item):
                if word < item:
                    wordList.pop(wordList.pop(item))
                    wordList.append(word)
                    
                    
   if __name__ == '__main__': --                 
