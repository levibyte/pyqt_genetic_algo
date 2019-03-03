class Color:
    def __init__(self,r,g,b):
        self.red = r
        self.green = g
        self.blue = b
        
    def get(self):
        return self.red,self.green,self.blue

class Node:
    def __init__(self, name, color):
        self.name = name
        self.connected_nodes = []
        self.color = color
        
    def add_connection(self,Node):
        self.connected_nodes.append(Node)
        
    def get_connected(self):
        return self.connected_nodes
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color.get()
    
    def set_color(self,color):
        self.color = color
