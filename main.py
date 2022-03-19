"""                           Conlang generator                            """
"""----------- Settings -----------"""
  
path = "liste_francais.txt"
debth = 1


"""----------- Import librairy -----------"""
import random

"""----------- Functions -----------"""
def import_corpus(path,debth) :       
    file = open(path,"r")
    raw_corpus = file.read().lower().splitlines()
    corpus=""
    for i in raw_corpus :
        corpus += " "*debth
        corpus += i.lower()
        corpus += " "*debth
    file.close()
    return corpus

def alphabet_generator(corpus) :
    alphabet=[]
    for letter in corpus :
        if letter not in alphabet :
            alphabet.append(letter)
    return alphabet

def polygram_generator(corpus,alphabet,debth, prev = "") :
    polygram = [0]*len(alphabet)
    for l in range(debth,len(corpus)) :
        if len(prev) == debth :
            if prev in ("",corpus[l-debth:l]) :
                polygram[alphabet.index(corpus[l])] += 1    
        else :
            nextprev = prev + corpus[l]
            recursion = polygram_generator(corpus,alphabet,debth,prev=nextprev) 
            polygram[alphabet.index(corpus[l])] = recursion                         
    return polygram   
    
def branch_sum(array) :
    total = 0
    if type(array) is list :
        for item in array :
            total += branch_sum(item)
    else :
        total += array
    return total

def letter_generator(polygram,prev) :
    
    if type(polygram[0]) is list :
        small = polygram[prev[0]]
        return letter_generator(small,prev[1:]) 
    else :
        dice = random.randint(0,branch_sum(polygram)-1)
        total = 0
        for i in range(len(polygram)) :
            total += polygram[i]
            if total > dice :
                return i
    
def word_generator(alphabet,polygram,word = None ) :
    if word is None :
        word = [0]*debth
    if word == [0]*debth or word[-1] !=0 :
        prev = word[-debth:]
        letter = letter_generator(polygram,prev)
        if not (word == [0]*debth and letter == 0) :
            word.append(letter)
        return word_generator(alphabet,polygram,word )
    else :
        string_word = ""
        for i in word :
            if i != 0 :
                string_word += alphabet[i]
        return string_word
"""----------- Main -----------"""


corpus = import_corpus(path,debth)
alphabet = alphabet_generator(corpus)
polygram = polygram_generator(corpus,alphabet,debth)


print(polygram)


print("==============")
for i in range(10) :
    print(word_generator(alphabet,polygram))
