
#------------------------------------------------     CORPUS  GENERATOR     ------------------------------------------------#
#-----------------------------------------------------     IMPORTS     -----------------------------------------------------#
import random
import os
#----------------------------------------------------     FUNCTIONS     ----------------------------------------------------#
def import_corpus(path,encoding) :
    file = open(path,"r", encoding = encoding)
    corpus = file.read().lower().split("\n")
    file.close()
    
    i=0
    while(i < len(corpus)) :
        if corpus[i] == "" or  corpus[i][0] == "#" :
            corpus.pop(i)
        else :
            i+=1

    """
    for i in range(len(corpus)) :
        corpus += corpus[i].split(" ")
    corpus = corpus[i:]
    """
    #corpus = list(dict.fromkeys(corpus))
    
    return corpus

class Polygraph() :
    class Node() :
        def __init__(self) :
            self.count = 0
            self.children = {}

    def __init__(self,debth) :
        """Takes in a debth (int), or how far the tree looks to infer the context of a character"""
        self.root = self.Node()
        self.debth = debth

    def process_corpus(self,corpus) :
        """Takes in an array of strings, and builds a polygraph tree """
        
        # Initializes the loading bar
        i = 0
        progress = 0
        width = os.get_terminal_size().columns-1

        for word in corpus :
            # Loading bar calculations and display
            i+=1
            if( progress != int(i/len(corpus)*width)) :
                os.system("clear")
                print("Building corpus tree : %.2f %%" %(i/len(corpus)*100))
                progress = int(i/len(corpus)*width)
                print("o"*progress + "."*(width-progress))

            # The actual processing
            self.process_word(word)

        print()
        print("Done !")
  
    def process_word(self,word) :
        """Takes in a string, and integrate it into the polygraph tree """      
        
        # Preprocess the word. The "_" at the beggining allow to predict the beggining of words
        word = "_" * self.debth + word + "_"

        #For each character, records the *debth* previous characters
        for l in range(len(word)-self.debth) :
            current = self.root
            # Walk down the polygraph tree
            for d in range(self.debth+1) :
                # If the branch does not exist, create it
                if  not word[l+d] in current.children :
                    current.children[word[l+d]] = self.Node()
                #Updates the current node and increases its weigth
                current = current.children[word[l+d]]
                current.count += 1

    def generate_word(self) :
        """use the polygraph tree to generate a plausible word"""

        # Initializes the word 
        word = "_"*self.debth 
        char = ""

        # While the word hasn't ended
        while char != "_" :
            # Align the word's last *debth* letter with the polygraph tree
            current = self.root
            for i in range(len(word)-self.debth, len(word)) :
                current = current.children[word[i]]
            
            # Chose a letter to add to the word, using the node's count as weigths.
            letters = list(current.children)
            weigths = []
            for l in letters :
                weigths.append(current.children[l].count)
            char = random.choices(letters,weigths)[0]
            word += char
            
        #cleanup the word :
        word = word.replace("_", "")
        if len(word) == 1 :
            word = word[0].upper()
        if len(word) > 1 :
            word = word[0].upper() + word[1:]
        return word


