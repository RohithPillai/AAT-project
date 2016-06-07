#Om Namo Narayanaya
#Om Gum Ganapathaye Namo Namaha
import progressbar

# read the filterwords
fil = open("filterwords","w")

line = fil.readline()
filwrd = []
while line:
    if line[0] != '#':
        filwrd += [line]
    line = fil.readline()
fil.close()

# to get total nuber of lines in the file prior to reading line by line.
with open('Extracted_Noun_Verb_Phrases_wikipedia.txt') as f:
    lentot = sum(1 for _ in f)
f.close()

#go through the NP and NPs
fvnp = open("Extracted_Noun_Verb_Phrases_wikipedia.txt","w")

# write to new file
fout =  open("Cleaned_Norm_VPnNPs_wikipedia.txt","w")

linevnp = fvnp.readline().lower()
P = progressbar.ProgressBar(lentot)
count = 0

while linevnp:

    removebool = False
    #remove words that are: is a prefix of words from filterwords
    for i in filwrd:
        spliti = i.split()
        lengthi = len(spliti)
        if linevnp.split()[:lengthi] != spliti:
            removebool = True

    if !removebool:
        fout.write(linevnp)


    linevnp = fvnp.readline().lower()
    P.update(count)
    count +=1

fout.close()
fvnp.close()
print "done!"
