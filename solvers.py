from cmath import cos
from pickle import TRUE
import random
import sys
from threading import local

class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far.
        self.best_state = None  



    def search(self, start_state):
        conf_matrix_new={"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
        for keys in self.conf_matrix:
            l = self.conf_matrix[keys]
            for e in l:
                conf_matrix_new[e].append(keys)

       
        print(f"cost of start state : {self.cost_fn(start_state)}")
        """
        :param start_state: str Input string with spelling errors
        """               

        k = 5
        lenn =len(start_state)
        
        beam = []
        beam.append(start_state)
    
        wordlist = [i for i in start_state.split()]
        wordlist_again= wordlist.copy()
            
      
        for m in range(0,len(wordlist)):
            random.shuffle(wordlist_again)
            word=random.choice(wordlist_again)
            w = wordlist.index(word)
            wordlist_again.remove(word)
            beam =[]
            beam.append(word)
            wlen= len(word)
            clevel=0
            list_char_random=[]

            for l in range(0, wlen):
                list_char_random.append(l)

            while(clevel<wlen):
                random.shuffle(list_char_random)
                charlevel= random.choice(list_char_random)
                list_char_random.remove(charlevel)
                store={}
                cost=[]

                for b in range (0,len(beam)):
                    beamword= beam.pop(0)
                    conf_row= conf_matrix_new[beamword[charlevel]] 
                    new_wordlist= wordlist
                    new_wordlist[w]= beamword
                    fakestr= ' '.join(new_wordlist)
                    store[self.cost_fn(fakestr)]= [beamword]
                    cost.append(self.cost_fn(fakestr))

                    for j in range(0,len(conf_row)):
                        newword = beamword[0:charlevel] + conf_row[j] + beamword[charlevel+1:]
                        new_wordlist2 = wordlist
                        new_wordlist2[w] = newword
                        fakestr2= ' '.join(new_wordlist2)
                        if self.cost_fn(fakestr2) not in cost:
                            store[self.cost_fn(fakestr2)]= [newword]
                            cost.append(self.cost_fn(fakestr2))

                cost.sort()
                beam=[]

                for best in range(0,k):
                    if(best<len(store)):
                        beam+=store[cost[best]]

                while(len(beam)>k):
                    beam.pop(len(beam)-1)

                new_wordlist3 = wordlist
                new_wordlist3[w]= beam[0]
                beststring= ' '.join(new_wordlist3)
                self.best_state= beststring
                clevel+=1

            wordlist[w]= beam[len(beam)-1]
            new_wordlist4 = wordlist
            new_wordlist4[w]= beam[0]
            self.best_state = ' '.join(new_wordlist4)
                        
        print(f"best state: {self.best_state} ")
        print(f"cost of best state: {self.cost_fn(self.best_state)} ")


        
      
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state
