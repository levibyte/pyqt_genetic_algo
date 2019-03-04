from libs.placement import Placement
from libs.placement_controller import PlacementController

import random

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
        #self.optimize()
        
        while self.controller.calc_intersections() is not 0:
            self.controller.add_change()
        #for i in range(1000):
            #self.controller.add_change()
            #self.controller.add_change()
            #self.controller.add_change()
        
        self.best_data = self.controller.get_placement()
        self.controller.set_data(self.best_data)
        print("END: {}".format(self.controller.calc_intersections()))
        
    def optimize(self):
        print("before optimization: {}".format(self.current_fitness))
        for i in range(100):
            self.controller.add_change()
            fitness = self.controller.calc_intersections() 
            print ("iteration: {} , fitness = {}".format(i,fitness))
            if fitness < self.current_fitness:
                self.current_fitness = fitness
                self.best_data = self.controller.get_placement()
                self.controller.set_data(self.best_data)
        
        print("after optimization: {}".format(self.current_fitness))
        self.best_data = self.controller.get_placement()
        self.controller.set_data(self.best_data)
        print("END: {}".format(self.controller.calc_intersections()))
        
    #def get_best_placement(self):
        #return self.best_data
