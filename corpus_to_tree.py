
#------------------------------------------------     CORPUS  GENERATOR     ------------------------------------------------#
#-----------------------------------------------------     IMPORTS     -----------------------------------------------------#
import random
import os
#----------------------------------------------------     FUNCTIONS     ----------------------------------------------------#
def import_corpus(path,encoding,debth,mode) :
    # Step 1 : convert file to raw_corpus
    file = open(path,"r", encoding = encoding)
    if mode == "sentence" :
        corpus = file.read().lower().split(".")
    elif mode == "word" :
        corpus = file.read().lower().split("\n")      
    
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

    def __init__(self,corpus,debth,noise) :
        self.root = self.Node()
        i = 0
        p = 0
        for word in corpus :
            #Progress bar
            i+=1
            if( p != int(i/len(corpus)*60)) :
                os.system("clear")
                print("Building corpus tree : %.2f %%" %(i/len(corpus)*100))
                p = int(i/len(corpus)*60)
                print("o"*p + "."*(60-p))
            #Calculations
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

        print()
        print("Done !")

    def generate(self,debth,noise) :
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
                weigths.append(current.children[l].count*(1 + random.random()*noise - 0.5*noise ))
            r = random.choices(letters,weigths)[0]
            word += r
            
        #cleanup :
        word = word.replace("_", "") 
        return word


