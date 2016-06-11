#Om Gum Ganapathaye Namo Namaha
#Om Namo Narayana

from nltk.parse.stanford import StanfordParser
import os
from gensim.models import word2vec
import numpy as np
import logging

##model = gensim.models.Word2Vec()

##model =  models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
##model = word2vec.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

""" These following line will setup the Stanford Parser to be used
    with NLTK.

    Make sure that the files are in the same directory as the python file
"""
path = os.getcwd()
# print path
java_path = "C:/Program Files/Java/jdk1.8.0_91/bin/java.exe"
os.environ['JAVAHOME'] = java_path

stanford_parser_dir = path+'/stanford-parser-full-2015-12-09/stanford-parser-full-2015-12-09/'

my_path_to_models_jar3 = stanford_parser_dir  + "stanford-parser-3.6.0-models.jar"
my_path_to_jar3 = stanford_parser_dir  + "stanford-parser.jar"

#######

def parseThisSentsandWrite (target,sentences,fhand, model_fname='brown_model'):
    model = word2vec.Word2Vec.load(model_fname)

    sen10ses = []
    for i in sentences: sen10ses+= [i.split()]

    parser=StanfordParser(path_to_models_jar=my_path_to_models_jar3, path_to_jar=my_path_to_jar3)
    # c = list(parser.parse_sents(sentences))
    c = parser.parse_sents(sen10ses)
    A = list(c)
    phrasesList = []
    for i in range(len(A)):
        try:
            for B in A[i]:
    ##            print B

                #init. the sum vectors
                Post = B.pos()
                J = np.zeros(300)
                N = np.zeros(300)
                V = np.zeros(300)
                for (word, tag) in Post:
                    GenPos = tag[0]
                    if GenPos == 'J':
                        J  = np.add(np.array(model[word.replace(",","").replace(";","")]),J)
                    elif GenPos == 'N':
                        N  = np.add(np.array(model[word.replace(",","").replace(";","")]),N)
                    elif GenPos == 'V':
                        V = np.add(np.array(model[word.replace(",","").replace(";","")]),V)

                vect = np.concatenate((N,J,V),axis=0)

                #generate an array with strings
                vect_arrstr = np.char.mod('%f', vect)
                #combine to a string
                vect_str = ",".join(vect_arrstr)
    ##            print type(target),type(vect_str)
                fhand.write(target[i]+","+vect_str+"\n")
        except:
            continue


def getVec (filename):#, model):

    logging.basicConfig(filename='example.log', filemode = 'w',
                        format='%(asctime)s ::%(levelname)s:%(message)s',
                        level=logging.DEBUG,  datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('Starting vectorize.py...')

    target_data = np.loadtxt("raw_cleaned_labeled_data.txt",
                             usecols=[0],delimiter="\t",dtype = str)

    sent_data = np.loadtxt("raw_cleaned_labeled_data.txt",
                           usecols=[1],delimiter="\t",dtype = str)

    fout = open (filename,"w")

    logging.info('Number of vectors to make: '+str(len(target_data)))

    parseThisSentsandWrite (target_data, sent_data,fout)#,model)

    logging.info('done: making vectors')

    fout.close()
    print "done"

if __name__ == '__main__':
    getVec("labeled_vecData.txt")
