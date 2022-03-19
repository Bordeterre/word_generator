#------------------------------------------------     CORPUS  GENERATOR     ------------------------------------------------#
#-----------------------------------------------------     IMPORTS     -----------------------------------------------------#
import sys 
import corpus_to_tree as ctt
#----------------------------------------------------     FUNCTIONS     ----------------------------------------------------#

#--------------------------------------------------     MAIN  PROGRAM     --------------------------------------------------#



path = "liste_francais.txt"
encoding = "Windows-1252"
debth = 3
words = 10

print("")


corpus = ctt.import_corpus(path,encoding,debth)
polygram = ctt.Polygraph(corpus,debth)

for i in range(words):
    print(polygram.show(debth))