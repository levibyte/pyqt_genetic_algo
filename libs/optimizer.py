from libs.placement import Placement
from libs.placement_controller import PlacementController

import random

class Optimizer:
    def __init__(self, data, controller):
        self.data = data
        self.controller = controller
        self.generations = []
        self.best_data = data
        self.initial_fitness = self.controller.calc_intersections() 
        self.current_fitness = self.initial_fitness
        self.optimize()
        
    def optimize(self):
        print("before optimization: {}".format(self.current_fitness))
        for i in range(10000):
            self.controller.add_change()
            fitness = self.controller.calc_intersections() 
            print ("iteration: {} , fitness = {}".format(i,fitness))
            if fitness < self.current_fitness:
                self.current_fitness = fitness
                self.best_data = self.controller.get_data()
        print("after optimization: {}".format(self.current_fitness))
        
    def get_best_option(self):
        return self.best_data
