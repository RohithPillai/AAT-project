#Om Gum Ganapathaye Namo Namaha
#Om Namo  Narayanaya

import re
import wikipedia
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

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
        
        #better filter and isolation of words from special characters
        regex = re.compile('[,\;\+\-\|\:\~\`\@\#\$\%\^\&\*\(\)\'\"\{\}\!\?\=\[\]1234567890]')

        rep = {";":".",
               ",":" , ",
               " th ": "",
               "-th ": "",
               " th-": "",
               "-th-": " ",
               " st ": "",
               "-st-": " ",
               " st-": "",
               "-st ": "",
               " nd ": "",
               "-nd ": "",
               " rd ": "",
               "-rd ": "",
               " -":"",
               "- ":"",
               "°c":"",
               "°f":"",
               "'re":" are",
               "'s":"",
               "n't":" not"}
        
        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
        pattern = re.compile("|".join(rep.keys()))
        text = pattern.sub(lambda m: rep[re.escape(m.group(0))], i)
        
        (m,_) = re.subn('\[\w*\]',' ',text)
        (n,_) = re.subn(regex,'',m)
        
        f+=" "+n
    return f.lower()

def createfile(siteLists,st=0,filename = "wikipediaarts_sound.txt"):

    #defaults to overwrite!!!!!
    if st == 0:
        fout = open(filename,'w')
    else:
        fout = open(filename,'a')

    count = 0
    for site in siteLists:
        sentences = getText(site)
        fout.write(sentences.encode('utf-8')+"\n")

        count+=1
    fout.close()

#Sound, Music, Birds_in_music, Vibrato, Onomatopoeia, Auditory_hallucination, Musical_ear_syndrome,
# Motor_theory_of_speech_perception, Cocktail_party_effect, Dichotic_listening, Jingle
def main():
    createfile(["Sound", "Music","Birds_in_music","Vibrato","Onomatopoeia","Auditory_hallucination","Musical_ear_syndrome",
"Motor_theory_of_speech_perception","Cocktail_party_effect","Dichotic_listening","Jingle"])

#########################################################################

if __name__ == "__main__" :
    main()
