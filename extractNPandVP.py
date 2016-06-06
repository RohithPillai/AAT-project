#Om Gum Ganapathaye Namo Namaha
#Om Namo  Narayanaya

from nltk.parse.stanford import StanfordParser
import urllib2
import html2text
import re
from bs4 import BeautifulSoup
import os
import wikipedia
import codecs
import progressbar

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

################# Functions ############################################

""" parseThisSent (str Sentence) => str[] Phrases
    REQUIRES: Sentence is unicode
    ENSURES: Phrases are the list of NPs or VPs from Sentence
"""
def parseThisSent (sentences):
    parser=StanfordParser(path_to_models_jar=my_path_to_models_jar3, path_to_jar=my_path_to_jar3)
    c = list(parser.raw_parse(sentences))
    B = c[0].copy()
    #get all  NPs and VPs
    phrasesList = []
    for s in B.subtrees(lambda B: B.label() == 'NP' or B.label() == 'VP'): phrasesList += [(" ".join(s.leaves()))]
    return phrasesList

""" parseThisSents (str[] Sentences) => str[] Phrases
    REQUIRES: Sentences are unicode
    ENSURES: Phrases are the list of NPs or VPs from Sentences
"""
def parseThisSents (sentences):
    sen10ses = []
    for i in sentences: sen10ses+= [i.split()]

    parser=StanfordParser(path_to_models_jar=my_path_to_models_jar3, path_to_jar=my_path_to_jar3)
    # c = list(parser.parse_sents(sentences))
    c = parser.parse_sents(sen10ses)
    A = list(c)
    phrasesList = []
    for i in range(len(A)):
        for B in A[i]:
##            print B
            for s in B.subtrees(lambda B: B.label() == 'NP' or B.label() == 'VP'):phrasesList += [(" ".join(s.leaves()))]
    return phrasesList



""" getsite (str site) => html doc
    REQUIRES: site is a topic and not an entire URL so that it can be
                looked up in Wikipedia
    ENSURES:
        - html doc returned is of URL "http://en.wikipedia.org/wiki/site
        - html doc is of type <Unicode>
"""
def getText(site):
    txt = wikipedia.page(site).content
    v = txt.split("\n")
    f = ""
    for i in v:
        if "{" in i or "*" in i:
            continue
        (m,g) = re.subn('\[\w*\]',' ',i)
        f+=" "+m
    return f.split(".")



""" createfile( str[] sitelists,
                int st: 0(default),
                str filename:"Extracted_Noun_Verb_Phrases.txt"(default)
                                                )  => None
    REQUIRES: The sitelists contain only existing topics
    ENSURES: All NPs and VPs from all the sites in
                sitelist is written to filename
"""

def createfile(siteLists,st=0,filename = "Extracted_Noun_Verb_Phrases_wikipedia.txt"):

    #defaults to overwrite!!!!!
    if st == 0:
        fout = open(filename,'w')
    else:
        fout = open(filename,'a')
    P = progressbar.ProgressBar(len(siteLists))
    count = 0
    for site in siteLists:
        fout.write("@source: "+site+"\n")
        sentences = getText(site)
        phrases = parseThisSents (sentences)
        for NVphrase in phrases:
            fout.write(NVphrase.encode('utf-8')+"\n")
        P.update(count)
        count+=1
    fout.close()

#Sound, Music, Birds_in_music, Vibrato, Onomatopoeia, Auditory_hallucination, Musical_ear_syndrome,
# Motor_theory_of_speech_perception, Cocktail_party_effect, Dichotic_listening, Jingle
def main():
    createfile(["Sound", "Music", "Birds_in_music","Vibrato","Onomatopoeia","Auditory_hallucination","Musical_ear_syndrome",
"Motor_theory_of_speech_perception","Cocktail_party_effect","Dichotic_listening","Jingle"])

#########################################################################

if __name__ == "__main__" :
    main()
