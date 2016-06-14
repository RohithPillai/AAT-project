#Om Namo Narayanaya
#Om Gum Ganapathaye Namo Namaha

import random
import numpy as np
import os
import cPickle
import sys

#create a file for saving using cPicle/pickle
class prog_state(object):
    """docstring for prog_state"""
    def __init__(self, filename,datalen):
        self.filename = filename
        self.datalen = datalen
        self.totseen = 0
        self.countpos = 0
        self.countneg = 0
        self.readlines = []

def exitformalities(PS):
    print "\nsaving program state..."
    pickle_out = open("saved_PS_labeldataprog","wb")
    cPickle.dump(PS,pickle_out)
    pickle_out.close()
    print "done labelling",count,"Positive & Negative examples..."
    print "here's a yoda :\n\t<{-_-}>"
    print "exiting program"
    exit()

def getrand(a,c,t):
    last = t-c
    b = np.argsort(a)
    if last < 0:
        print "Read all instances in the data file..."
        return None
    num =  b[random.randint(0,last)]
    a[num] = 1
    return num

def main(count,filen):

    data = np.loadtxt(filen,delimiter = '\t', dtype = str)

    if "raw_cleaned_labeled_data.txt" in os.listdir(os.getcwd()):
        new = raw_input("Do you want to load from last time?(y/n):")
        while new not in ['y','n']:
            new = raw_input("Sorry pls ans => Do you want to load from last time?(y/n):")

        # Load saved program state
        if new == 'y':
            #load the file
            sur = raw_input("Are you sure you want to load the prev. data? Data will be written to existing file. (y/n):")
            while sur not in ['y','n']:
                sur = raw_input("Are you sure you want to load the prev. data? Data will be written to existing file. (y/n):")
            if sur == 'y':
                print "loading saved program state..."
                fout = open("raw_cleaned_labeled_data.txt","a")
                pickle_in = open("saved_PS_labeldataprog","rb")
                PS = cPickle.load(pickle_in)
                pickle_in.close()

            else:
                print "exiting program......."
                exit()

        else: #Star over ===> RESET
            sur = raw_input("Are you sure you want to start over? Warning: all saved data will be overwriten. (y/n):")
            while sur not in ['y','n']:
                sur = raw_input("Are you sure you want to start over? Warning: all saved data will be overwriten. (y/n):")
            if sur == 'y':
                print "Setting up new program state..."
                fout = open("raw_cleaned_labeled_data.txt","w")
                PS = prog_state("raw_cleaned_labeled_data.txt",len(data))
                PS.totseen = 0
                PS.countpos, PS.countneg = 0,0
                PS.readlines = [0]*PS.datalen
            else:
                print "exiting program......."
                exit()
    else:
        print "Setting up new program state..."
        fout = open("raw_cleaned_labeled_data.txt","w")
        PS = prog_state("raw_cleaned_labeled_data.txt",len(data))
        PS.totseen = 0
        PS.countpos, PS.countneg = 0,0
        PS.readlines = [0]*PS.datalen

    lastline = PS.datalen -1
    print "How to use this program to label:"
    print "\ty - yes\n\tn - no\n\tk - skip the current example phrase\n\tc - edit the sentence. ONLY use to correct spacing errors in examples.\n\ts - save and exit the program\n"

    print "Please label the following:"

    while PS.countpos < count or PS.countneg < count  :
        print "\nState:\n Total Seen:",PS.totseen,"|| Total Labeled:",PS.countneg+PS.countpos,"|| Labeled Positive:",PS.countpos,"|| Labeled Negative:",PS.countneg
        #keep reading the file and writting

        ### Warning: This has the enourmos problem of an infinite loop if the
        ### count > no. of instances of the data!!!!!
        # line = random.randint(0,lastline)
        # while line in PS.readlines:
        #     line = random.randint(0,lastline)

        line = getrand(PS.readlines,PS.totseen,lastline)
        if line  == None:
            exitformalities(PS)

        dataline = data[line]
        if dataline[0] == '@':
            dataline = data[line+(random.choice([1,-1]))]

        print '\n'+dataline
        resp = raw_input("Enter (y/n/k and s to save and exit):")
        while resp not in ['y','n','k','s']:
            if resp == 'c':
                sure = 'n'
                while sure != 'y'and sure != 'x':
                    changedline = raw_input("Enter the changed sent (only change spacing errors!):\n")
                    sure = raw_input("Save changes? (y/n or press x to exit without changes):")
                    while sure not in ['y','n','x']:
                        sure = raw_input("Sorry pls respond as follows => Save changes? (y/n):")

                if sure == 'y':
                    dataline = changedline

            print "Try again."
            print dataline
            resp = raw_input("Enter (y/n/k and s to save and exit):")

        if resp == 's':
            exitformalities(PS)

        elif resp == 'k':
            PS.totseen += 1
            continue
        elif resp == 'y':
            ans = '1'
            PS.countpos += 1
        elif resp == 'n':
            ans = '0'
            PS.countneg += 1

        PS.totseen += 1
        fout.write(ans+'\t'+dataline+'\n')

    exitformalities(PS)

if __name__ == '__main__':

    if sys.argv[1:] == []:
        count = 2000
    else:
        count = int(sys.argv[1])
    filename = "Cleaned_Norm_VPnNPs_wikipedianewuniq_Half1st.txt"
    if raw_input("You have set count to: "+str(count) +". To continue press Enter, to cancel and exit press x now:") == 'x':
        print "exiting program"
        exit()
    else:
        main(count,filename)
