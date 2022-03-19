#------------------------------------------------     CORPUS  GENERATOR     ------------------------------------------------#
"""
The example datasets are :
    -liste_francais.txt, from : http://www.3zsoftware.com/fr/listes.php (gutenberg.txt)
    -liste_anglais.txt, from : https://github.com/dwyl/english-words/blob/master/words.txt
    -frankenstein.txt, from : https://www.gutenberg.org/files/84/84-0.txt
"""
#---------------------------------------------------     PARAMETERS     ----------------------------------------------------#
path = "liste_francais.txt"
encoding = "utf-8"
mode = "word" # word / sentence
debth = 3
amount = 10
noise = 1

#-----------------------------------------------------     IMPORTS     -----------------------------------------------------#
import sys 
import corpus_to_tree as ctt
#----------------------------------------------------     FUNCTIONS     ----------------------------------------------------#

#--------------------------------------------------     MAIN  PROGRAM     --------------------------------------------------#

corpus = ctt.import_corpus(path,encoding,debth,mode)
polygram = ctt.Polygraph(corpus,debth,noise)

for i in range(amount):
    if mode == "sentence" :
        print("============================================")
        sentence = " ".join(polygram.show(debth,noise).split("\n"))+"."
        print(sentence)
    elif mode == "word" :
        print(polygram.show(debth,noise))
