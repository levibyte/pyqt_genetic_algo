from libs.node import *
import random
from random import randint
import copy

class PlacementController:
    def __init__(self):
        self.layers = []

    def get_placement(self):
        return self.layers
    
    #def set_placement(self,placement):
        #self.layers = placement.get_data()

    def set_data(self,data):
        #del self.layers
        #self.layers = []
        #self.layers = copy.deepcopy(data)
        self.layers = data
        #self.layers = copy.copy(data)
        #print(" from set data:{}".format(self.calc_intersections()))
        
    def add_change(self):
        #return 0
        import time
        random.seed(time.clock())

        x = randint(0,len(self.layers)-1)
        
        j = randint(0,len(self.layers[x])-1)
        y = randint(0,len(self.layers[x])-1)
        
        #print("SWAPPING {}{} to {}{}".format(x,j,x,y))

        #del self.layers[x]
        self.layers[x][j],self.layers[x][y] = self.layers[x][y],self.layers[x][j]

    def calc_intersections(self):
        i = 0
        res = 0
        for layer in self.layers:
            res += self.calc_intersections_beetween_to_adjcent_layers(i)
            i += 1
        
        return res
        
    def calc_intersections_beetween_to_adjcent_layers(self,i):
        if i is len(self.layers)-1:
            return 0
        
        vec = []
        for node in self.layers[i]:
            for n in node.get_connected():
                i,j = self.find_ij(n)
                vec.append(j)
            #vec.append([j for i,j in node.get_connected()])
        
        res = 0
        k = 0
        #print(vec)
        #exit(0)
        for v in vec:
            for i in range(0,k):
               if vec[i] > vec[k]:
                res += 1 
            k += 1
        return res
        
    
    def find_ij(self,mynode):
        i = 0
        found = False
        
        for layer in self.layers:
            j = 0
            for node in layer:
                if node == mynode:
                    found = True
                    break
                j += 1
                
            if found is True:
                break
            i += 1
            
        return i,j
        
    
    def merge(self,nodes1,nodes2):
        res = []
        for i in range(len(nodes1)):
            #print("////////MERGE: {} {}".format(len(nodes1),len(nodes2)))
            res.append(self.merge_columns(nodes1[i],nodes2[i]))
        
        return res
            
            
        
    def merge_columns(self,col1,col2):
        in_first = set(col1[:len(col1)])
        in_second = set(col2)
        in_second_but_not_in_first = in_second - in_first
        result = col1 + list(in_second_but_not_in_first)
        return result

            
