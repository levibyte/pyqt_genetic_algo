from libs.node import *
from random import randint

class Placement:
    def __init__(self,**kwargs): 
        self.layers_max = kwargs['num_layers']
        self.nodes_max = kwargs['max_nodes_in_layer']
        self.connection_max = kwargs['max_node_connection']
        self.connection_min = kwargs['min_node_connection']
        
        self.create_random_placement()
        #self.layers = []
  
    def create_random_placement(self):
        self.create_layers()
        self.create_connections()
        
    def create_rand_color(self):
        return Color(randint(0,255),randint(0,255),randint(0,255))
    
    def create_layers(self):
        self.layers = [ [ Node("Node{}{}".format(i,j),self.create_rand_color()) for j in range(randint(2,self.nodes_max)) ] for i in range(self.layers_max) ]
        
    def create_connections(self):
        i = 0
        for layer in self.layers:
            j = 0
            for node in layer:
                print("Node {} {}".format(i,j))
                if i is not self.layers_max-1:
                    for k in range(randint(self.connection_min,self.connection_max)):
                        x = len(self.layers[i+1])-1
                        d = randint(0,x)
                        print(" --> connecting to {} {}".format(i+1,d))
                        n = self.layers[i+1][d]
                        node.add_connection(n)
                        n.add_parent(node)
                        node.colorize()
                        #col = node.get_color()
                        #n.set_color(col)
                        
                j+=1
            i+=1

    def get_data(self):
        return self.layers
