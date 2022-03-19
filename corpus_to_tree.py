
#------------------------------------------------     CONLANG GENERATOR     ------------------------------------------------#
#-----------------------------------------------------     IMPORTS     -----------------------------------------------------#
import random
#----------------------------------------------------     FUNCTIONS     ----------------------------------------------------#
def import_corpus(path,encoding,debth) :
    # Step 1 : convert file to raw_corpus
    file = open(path,"r", encoding = encoding)
    corpus = file.read().lower().splitlines()
    file.close()

    #Step 2 : preprocess each word
    for i in range(len(corpus)) :
        corpus[i] = "_" * debth + corpus[i] + "_" * debth
    
    return corpus

def alphabet_generator(corpus) :
    alphabet=[]
    for word in corpus :
        for letter in word :
            if letter not in alphabet :
                alphabet.append(letter)
    return alphabet

"""
def polygram_generator(corpus,alphabet,debth, prev = "") :
    polygram = [0]*len(alphabet)
    for w in range(100) : 
        word = corpus[w]
        for l in range(debth,len(word)) :
            if len(prev) == debth :
                if prev  == word[l-debth:l] :
                    polygram[alphabet.index(word[l])] += 1 
            else :
                smaller_polygram = polygram_generator(corpus, alphabet, debth, prev = prev + word[l])
                polygram[alphabet.index(word[l])] = smaller_polygram
                     
    return polygram  

def word_to_polygram(word,alphabet,debth,prev = "") :
    polygram = [0]*len(alphabet)
    for l in range(debth,len(word))
"""



class Polygraph() :
    class Node() :
        def __init__(self) :
            self.count = 0
            self.children = {}

    def __init__(self,corpus,alphabet) :
        self.root = self.Node()
        
        for word in corpus :
            current = self.root
            current.count += 1
            for l in range(len(word)) :
                print(word[l])
                #if non_existant node, create node
                if word[l] not in current.children :
                    current.children[word[l]] = self.Node()
                #count occurences
                current = current.children[word[l]]
                current.count += 1
                    

    def show3(self) :
        current = self.root
        tmp = ""
        while True :
            print(current.count)
            if len(list(current.children)) > 0 :
                r = random.choice(list(current.children))
                tmp += r
                current = current.children[r]
            else :
                print(tmp)
                break
    def show(self) :
        current = self.root
        print(list(current.children))

#--------------------------------------------------     MAIN  PROGRAM     --------------------------------------------------#

path = "liste_francais.txt"
encoding = "Windows-1252"
debth = 1

corpus = import_corpus(path,encoding,debth)
alphabet = alphabet_generator(corpus)
print(alphabet)

polygram = Polygraph(corpus[0],alphabet)
polygram.show()