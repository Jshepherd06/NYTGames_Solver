# Class for solving Spelling Bee game

class SpellingBee:
    def __init__(self):
    
    """
    * Function for finding words that fit the requirements:
    *   - Must only contain letters in char array 'letters'
    *   - Must contain at least one instance of char 'key'
    *   - Must be 4 or more characters long
    * Takes in char array letters and char key ^ look above for use
    * Returns an string array containing all valid words
    """
    def FindWords(self, letters, key):
        
        words = []
        with open("words_alpha.txt", "r") as f:
            #iterate through each line in words_alpha.txt
            for line in f:
                #if the word is less than 4 chars, go next
                if len(line.strip()) < 4:
                    continue
                #otherwise, iterate through each char in line
                else:
                    hasKey = 0
                    for char in line.strip():
                        #if a char in the word is not in letters, go next line
                        if char not in letters:
                            hasKey == 0
                            break

                        #if current char is key, change hasKey to 1
                        if char == key:
                            hasKey = 1
                    
                    #is word has key letter and no invalid letters, add to word list
                    if hasKey == 1:
                        words.append(line.strip())
        
        return words

