from libs.placement import Placement
from libs.placement_controller import PlacementController
from libs.optimizer import Optimizer
from libs.renderer import Renderer
            
initial_settings = {
    'num_layers' : 4,
    'max_nodes_in_layer' : 6,
    'max_node_connection' : 1,
}

if __name__ == '__main__':
    #create placement controller
    placement_controller = PlacementController()
    
    #create placement
    placement = Placement(**initial_settings)
    
    #optimize placement, using placement controller
    #optimizer = Optimizer(placement,placement_controller)
    
    placement_controller.set_placement(placement)
    #placement_controller.set_data(optimizer.get_best_option())
    
    #draw 
    renderer = Renderer(placement_controller)
    renderer.draw()
    
