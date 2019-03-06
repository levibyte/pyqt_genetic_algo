from libs.placement import Placement
from libs.placement_controller import PlacementController

import random
import copy

class Optimizer:
    def __init__(self, placement, controller):
        self.data = placement.get_data()
        self.controller = controller
        self.controller.set_data(self.data)
        #self.controller.set_placement(placement)
        #self.generations = []
        self.best_data = []
        self.initial_fitness = self.controller.calc_intersections() 
        self.current_fitness = self.initial_fitness
        print("BEGIN: {}".format(self.controller.calc_intersections()))
        self.optimize2()
        
        #while self.controller.calc_intersections() is not 0:
            #self.controller.add_change()
        #for i in range(1000):
            #self.controller.add_change()
            #self.controller.add_change()
            #self.controller.add_change()
        
        #self.best_data = self.controller.get_placement()
        #self.controller.set_data(self.best_data)
        #print("END: {}".format(self.controller.calc_intersections()))

    def optimize(self):
        #print("before optimization: {}".format(self.current_fitness))
        for i in range(30000):
            self.controller.add_change()
            #fitness = self.controller.calc_intersections() 
            #print ("iteration: {} , fitness = {}".format(i,fitness))
            if self.controller.calc_intersections() is 3:
            #if fitness < self.current_fitness:
                #fitness = self.current_fitness
                self.best_data = copy.deepcopy(self.controller.get_placement())
                
                self.controller.set_data(copy.deepcopy(self.best_data))
                break
        
        #print("after optimization: {}".format(self.current_fitness))
        #self.best_data = self.controller.get_placement()
        #self.controller.set_data(self.best_data)
        print("END: {}".format(self.controller.calc_intersections()))
        
    def optimize2(self):
        gens_max=10
        survivors_factor=3
        max_iterations=1000
        
        gens = {self.initial_fitness:self.data}
        
        #first generation
        for i in range(gens_max):
            fitness = self.controller.calc_intersections()
            gen = copy.deepcopy(self.controller.get_placement()) 
            gens[fitness] = gen
            self.controller.add_change()
           
        
        #each new generation
        for gen_num in range(max_iterations):
            print("**********GENERATION {}************ (inital is: {} )".format(gen_num,self.initial_fitness))
            #selection
            winners=[]
            k=0
            max_winners=gens_max//survivors_factor
            for f in sorted(gens.keys()):
                if k < max_winners:
                    print("-----winner {} fintess={}".format(k,f))
                    if f < self.current_fitness: 
                        self.current_fitness = f
                    winners.append(gens[f])
                else:
                    del gens[f]
                    #break
                k+=1
                
            if self.current_fitness is 0:
                break
            #crossover
            x = gens_max-max_winners
            for g in range(x):
                import time
                random.seed(time.clock())
                a = random.randint(0,len(winners)-1)
                random.seed(time.clock())
                b = random.randint(0,len(winners)-1)
                #print("-----crossover winner{} winner{}".format(a,b))
                #gen1 = winners[a]
                #gen2 = winners[b]
                #gen = self.controller.merge(gen1,gen2)
                gen = winners[random.randint(0,len(winners)-1)]
                self.controller.set_data(copy.deepcopy(gen))
                self.controller.add_change()
                fitness = self.controller.calc_intersections()
                gens[fitness] = copy.deepcopy(self.controller.get_placement())
                #print("-->crossover {} {}".format(g,fitness))
            
            #mutation
            #for v in gens.values():
                #self.controller.set_data(copy.deepcopy(v))
                #self.controller.add_change()
                #fitness = self.controller.calc_intersections()
                #del v
                #gens[fitness] = gen
                #print("-->crossover {} {}".format(g,fitness))
            
            print()
        print("end.")
        
        #self.best_data = winners[0]
        self.best_data = copy.deepcopy(winners[0])
        self.controller.set_data(copy.deepcopy(self.best_data))
        
    #def get_best_placement(self):
        #return self.best_data
