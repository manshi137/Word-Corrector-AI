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

    # def transform(self):
    #     conf_matrix_new={}
    #     for keys in self.conf_matrix:
    #         l = self.conf_matrix[keys]
    #         for e in l:
    #             conf_matrix_new[e].append(keys)
    #     return conf_matrix_new
    print("hiiiiiiiiiiiiiiiiiii")

    def search(self, start_state):
        conf_matrix_new={"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
        for keys in self.conf_matrix:
            l = self.conf_matrix[keys]
            for e in l:
                conf_matrix_new[e].append(keys)

        # print(conf_matrix_new)
        # print("initial cost")
        print(self.cost_fn(start_state))
        """
        :param start_state: str Input string with spelling errors
        """               

        k = 2 
        lenn =len(start_state)
        
        beam = []
        beam.append(start_state)
        # print( start_state.split())
        wordlist = [i for i in start_state.split()]
        wordlist_again= wordlist.copy()
            
      
        for m in range(0,len(wordlist)):
            random.shuffle(wordlist_again)
            word=random.choice(wordlist_again)
            w = wordlist.index(word)
            # print(f"wordlist={wordlist}")
            # print(f"wordlist_again = {wordlist_again}")
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
                    # print(f"store ; {store}")
                    cost.append(self.cost_fn(fakestr))
                    # print(f"cost== {self.cost_fn(fakestr)}")
                    for j in range(0,len(conf_row)):
                        # print(f"beam word : {beamword}")
                        newword = beamword[0:charlevel] + conf_row[j] + beamword[charlevel+1:]
                        # print(f"new word : {newword}")
                        #store and cost
                        new_wordlist2 = wordlist
                        new_wordlist2[w] = newword
                        fakestr2= ' '.join(new_wordlist2)
                        # print("aa")
                        if self.cost_fn(fakestr2) not in cost:
                            store[self.cost_fn(fakestr2)]= [newword]
                            cost.append(self.cost_fn(fakestr2))
                        # print(f"cost2== {self.cost_fn(fakestr2)}")
                cost.sort()
                # print(store)
                # print(f"cost list: {cost}")
                beam=[]
                # self.best_state = ' '.join
                for best in range(0,k):
                    if(best<len(store)):
                        beam+=store[cost[best]]
                        # print(f"beam {beam}")
                while(len(beam)>k):
                    beam.pop(len(beam)-1)
                    # print(f"beam {beam}")

                new_wordlist3 = wordlist
                new_wordlist3[w]= beam[0]
                beststring= ' '.join(new_wordlist3)
                self.best_state= beststring
                # print(f"cost best == {self.cost_fn(self.best_state)}")
                clevel+=1
            wordlist[w]= beam[len(beam)-1]
            new_wordlist4 = wordlist
            new_wordlist4[w]= beam[0]
            print(f"best word: {beam[0]}")
            self.best_state = ' '.join(new_wordlist4)
                        

                    
            # costs.sort()
            # beam=[]
            # self.best_state = store[costs[0]][0]
            # print(f"cost of best state: {self.cost_fn(self.best_state)} ")
            # print(f"best state: {self.best_state} ")
            # for k in range(0,k):
            #     beam.append(store[costs[k]])

        print(f"cost of best state: {self.cost_fn(self.best_state)} ")
        print(f"best state: {self.best_state} ")


        
        
        
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state