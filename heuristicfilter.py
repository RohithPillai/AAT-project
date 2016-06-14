#Om Namo Narayanaya
#Om Gum Ganapathaye Namo Namaha
import progressbar
import string
import subprocess
import shlex

""" Code complexity Work: O(n^2) """

# read the filterwords
fil = open("filterwords","r")

line = fil.readline()
filwrd = []
while line:
    if line[0] != '#' and line[0] != '\n':
        filwrd += [line.replace("\n","")]
    line = fil.readline()
fil.close()

# to get total nuber of lines in the file prior to reading line by line.
with open('Extracted_Noun_Verb_Phrases_wikipedianew.txt') as f:
    lentot = sum(1 for _ in f)
f.close()

#go through the NP and NPs
fvnp = open("Extracted_Noun_Verb_Phrases_wikipedianew.txt","r")

# write to new file
fout =  open("Cleaned_Norm_VPnNPs_wikipedianew.txt","w")

linevnp = fvnp.readline().lower()

##P = progressbar.ProgressBar(lentot)
count = 0
printable = set(string.printable)
acceptable = set(string.printable)
acceptable.update(['the','their','his','her','such'])

while linevnp:

    #clean all the unprintable characters like the greek alphabets etc, and other chars.

    linevnp = filter(lambda x: x in printable, linevnp)

    if linevnp[0] == '@':
        #fout.write(linevnp)
        linevnp = fvnp.readline().lower()
        continue
    if len(linevnp.split()) == 0:
        linevnp = fvnp.readline().lower()
        continue
    # filter out words like 'the' and 'a' if
    #it is the very first word on the phrase

    prev =''
    curr = linevnp
    while prev != curr and len(curr) != 0:
        prev = curr
        firstword = linevnp.split()[0]
        if firstword in acceptable:
            linevnp = " ".join(linevnp.split()[1:])
        curr = linevnp


    removebool = False
    #remove words that are: is a prefix of words from filterwords
    for i in filwrd:
        spliti = i.split()
        lengthi = len(spliti)
        if linevnp.split()[:lengthi] == spliti:
            removebool = True



    if not(removebool):
        wrl = linevnp.replace("\n","").replace("=== ","").replace("== ","").replace("===","").replace("==","").replace("=","").replace(" th ","").replace(" st ","")
        if wrl != "":
            fout.write(wrl.strip()+'\n')



    linevnp = fvnp.readline().lower().replace("th-","")
##    P.update(count)
    count +=1

fout.close()
fvnp.close()

print "run this in the cmd/terminal:\nsort C:\Users\\rohit\Documents\AAT\Cleaned_Norm_VPnNPs_wikipedianew.txt | uniq > C:\Users\\rohit\Documents\AAT\Cleaned_Norm_VPnNPs_wikipedianew_uniq.txt\n "
