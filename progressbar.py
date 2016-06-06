#Om Namo Narayanaya
#Om Gum  Ganapathaye Namo Namaha

import sys
import time

class ProgressBar  (object):

    """ProgressBar is a tool to create a text-based progess bar indicator """
    def __init__(self,total, totalwidth =50,prefix ="Progress", suffix ="Completed", character = "="):

        self.total = total
        self.totalwidth = totalwidth
        self.prefix = prefix
        self.suffix = suffix
        self.character = character

    def update (self,iteration):

        filledLength = int(round(self.totalwidth*iteration / float(self.total)))-1
        percents        = round(100.00 * (iteration / float(self.total)),2)
        bar             = self.character * filledLength + '>'+'-' * (self.totalwidth - filledLength)
        sys.stdout.write('%s: [%s] %s%s %s\r' % (self.prefix, bar, percents, '%', self.suffix)),sys.stdout.flush()
        if iteration == self.total-1:
            filledLength = self.totalwidth
            percents        = 100.00
            bar             = self.character * filledLength + '>'+'-' * (self.totalwidth - filledLength)
            sys.stdout.write('%s: [%s] %s%s %s\r' % (self.prefix, bar, percents, '%', self.suffix)),sys.stdout.flush()
            print("\n")


""" Example usage:
P = ProgressBar(100)
for i in range(100):
    time.sleep(0.01)
    P.update(i)"""
