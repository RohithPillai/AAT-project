import gensim
import logging
import numpy as np

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = open("wikipediaarts_sound.txt","r")
sents= f.read(600000000).split(".")
sentences =[]
for sent in sents:
    sentences += [sent.split()]

sentences = np.array(sentences)
###################696358000
f.close()
print"hi"
model = gensim.models.Word2Vec(sentences, min_count=1, size = 300, workers = 2)
model.save('wikipedia_modelshort')
