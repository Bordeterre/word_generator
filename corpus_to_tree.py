
#------------------------------------------------     CORPUS  GENERATOR     ------------------------------------------------#
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
        corpus[i] = "_" * debth + corpus[i] + "_"
    
    return corpus

class Polygraph() :
    class Node() :
        def __init__(self) :
            self.count = 0
            self.children = {}

    def __init__(self,corpus,debth) :
        self.root = self.Node()
        for word in corpus :
            #print(word)
            for l in range(len(word)-debth) :
                #For each letter, we associate the 
                current = self.root
                for d in range(debth+1) :
                    #if non_existant node, create node
                    if  not word[l+d] in current.children :
                        current.children[word[l+d]] = self.Node()
                    #count occurences
                    current = current.children[word[l+d]]
                    current.count += 1

    def show(self,debth) :
        decision_root = self.root #From where 
        word = "_"*debth
        r = ""
        while r != "_" :
            # Chose the correct determination table to use
            current = decision_root
            i = len(word)-debth
            for d in range(debth) :
                current = current.children[word[i]]
                i+=1

            # Chose a weigthed random letter 
            letters = list(current.children)
            weigths = []
            for l in letters :
                weigths.append(current.children[l].count)
            r = random.choices(letters,weigths)[0]
            word += r
            
        #cleanup :
        word = word.replace("_", "") 
        return word


#--------------------------------------------------     MAIN  PROGRAM     --------------------------------------------------#

path = "liste_francais.txt"
encoding = "Windows-1252"
debth = 3

corpus = import_corpus(path,encoding,debth)

polygram = Polygraph(corpus,debth)

for i in range(10) :
    print(polygram.show(debth))