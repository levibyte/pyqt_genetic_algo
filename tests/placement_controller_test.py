import pytest

from libs.placement_controller import PlacementController
from libs.node import Node, Color


@pytest.fixture
def placement_data():
    """ creates simple placement data
    Placement bellow:
    
      A    D  
       \  /   
      B-\/-E   
        /\   
       /  \   
      C    F
    
    Total there are 3 intersection within this placement.
    """

    layers = []
    layer1 = []
    layer2 = []
    
    dummy_color = Color(0,0,0)
    A = Node("A",dummy_color)
    B = Node("B",dummy_color)
    C = Node("C",dummy_color)
    D = Node("D",dummy_color)
    E = Node("E",dummy_color)
    F = Node("F",dummy_color)
    
    A.add_connection(F)
    B.add_connection(E)
    C.add_connection(D)
    

    layer1.append(A)
    layer1.append(B)
    layer1.append(C)
    
    layer2.append(D)
    layer2.append(E)
    layer2.append(F)
    
    
    layers.append(layer1)
    layers.append(layer2)
    
    return layers
    
def test_count_intersections_raw(placement_data):
    pc = PlacementController();
    pc.set_data(placement_data)
    assert 3 == pc.calc_intersections()
    
def test_count_intersections_on_swap_colmns(placement_data):
    pc = PlacementController();
    placement_data[0],placement_data[1] = placement_data[1],placement_data[0]
    pc.set_data(placement_data)
    assert 0 == pc.calc_intersections()
    
def test_count_intersections_on_swap_inside_first_column(placement_data):
    pc = PlacementController();
    placement_data[0][0],placement_data[0][2] = placement_data[0][2],placement_data[0][0]
    pc.set_data(placement_data)
    assert 0 == pc.calc_intersections()

def test_count_intersections_on_swap_inside_second_column(placement_data):
    pc = PlacementController();
    placement_data[1][0],placement_data[1][1] = placement_data[1][1],placement_data[1][0]
    pc.set_data(placement_data)
    assert 2 == pc.calc_intersections()

    
    
