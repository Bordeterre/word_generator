#------------------------------------------------     CORPUS  GENERATOR     ------------------------------------------------#
"""
The example datasets are :
    -liste_francais.txt, from : http://www.3zsoftware.com/fr/listes.php (gutenberg.txt)
    -liste_anglais.txt, from : https://github.com/dwyl/english-words/blob/master/words.txt
    -frankenstein.txt, from : https://www.gutenberg.org/files/84/84-0.txt
"""
#---------------------------------------------------     PARAMETERS     ----------------------------------------------------#
mode = "word" # word / sentence
noise = 0

#-----------------------------------------------------     IMPORTS     -----------------------------------------------------#
import os
import sys
import corpus_to_tree as ctt
#----------------------------------------------------     FUNCTIONS     ----------------------------------------------------#
def parameters() :
    path = input("Path to the source file : ")
    while not os.path.isfile(path) and not path == "" :
        path = input("%s does not exist ! " %(path))
    encoding = input("encoding (utf-8 by default) : ")
    debth = input("Debth (3 by default): ")
    while not (debth.isdigit() and int(debth) >=0) and not path == "" :
        debth = input("Debth must be an integer ! ")

    if path == "" :
        path = "liste_francais.txt"
    if encoding == "" :
        encoding = "utf-8"
    if debth == "" :
        debth = "3"
    debth = int(debth)

    return path, encoding, debth

#--------------------------------------------------     MAIN  PROGRAM     --------------------------------------------------#

path, encoding, debth = parameters()

corpus = ctt.import_corpus(path,encoding,debth,mode)
polygram = ctt.Polygraph(corpus,debth,noise)

print()
while(True) :
    
    for i in range(10) :
        if mode == "sentence" :
            print("============================================")
            sentence = " ".join(polygram.generate(debth,noise).split("\n"))+"."
            print("  -  " + sentence)
        elif mode == "word" :
            word = polygram.generate(debth,noise)
            print("  -  " + word)
    
    print()
    print("Press enter to generate 10 new words,")
    choice = input("or type \" quit \" to quit the program : ")
    os.system("clear")
    if choice == "quit" :
        sys.exit()
    print()
    print()
    print()
    print("Here are some new words : ")
    print()
