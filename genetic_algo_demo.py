#from libs.renderer import Renderer
#from libs.system import System
from PyQt4.QtGui import *
#from PyQt5.QtWidgets import *
from PyQt4.QtCore import *
from random import randint

class Node:
    def __init__(self, name):
        self.name = name
        self.connected_nodes = []
        
    def add_connection(self,Node):
        self.connected_nodes.append(Node)
        
    def get_connected(self):
        return self.connected_nodes
    
    
class Canvas(QWidget):
    def __init__(self, nodes, *args, **kwargs):
        super(Canvas, self).__init__(*args, **kwargs)
        self.nodes = nodes
        self.tx = 100
        self.ty = 100
        self.dx = 50
        self.dy = 50
        

    def paintEvent(self, event):
        self.draw()
        
    def draw(self):
        #for nodes
        i = 0
        for layer in self.nodes:
            j = 0
            for node in layer:
                #self.draw_node_and_its_connections(node)    
                self.draw_node(i,j)
                self.draw_connection(node)
                j += 1
            i += 1
            
        
    #def draw_node_and_its_connections(self,Node):
        #self.draw_node(Node)
        #self.draw_connections(Node)
        
    def draw_node(self,i,j):
        print("drawing {} {}".format(i,j))
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        r = QRect(self.tx*i+self.dx,self.ty*j+self.dy,20,20)
        outer, inner = Qt.gray, Qt.lightGray        
        p.fillRect(r, QBrush(inner))
        pen = QPen(outer)
        pen.setWidth(1)
        p.setPen(pen)
        p.drawRect(r)
        
    def draw_connections(self,nodes):
        for node in nodes:
            self.draw_connection(node)
    
    def draw_connection(self,node):
        return 0
        

    
class Renderer(QMainWindow):
    def __init__(self,nodes,*args, **kwargs):
        super(Renderer, self).__init__(*args, **kwargs)
        canvas = Canvas(nodes)
        self.setCentralWidget(canvas)


class System:
    def __init__(self,**kwargs): 
        self.layers_max = kwargs['num_layers']
        self.nodes_max = kwargs['max_nodes_in_layer']
        self.connection_max = kwargs['max_node_connection']
        self.create_random_placement()
  
    def create_random_placement(self):
        self.create_layers()
        self.create_connections()
        
    def create_layers(self):
        self.layers = [ [ Node("Node{}{}".format(i,j)) for j in range(randint(1,self.nodes_max)) ] for i in range(self.layers_max) ]
        
    def create_connections(self):
        i = 0
        for layer in self.layers:
            j = 0
            for node in layer:
                print("Connecting {} {}".format(i,j))
                #if i is not self.layers_max-1:
                    #n = self.layers[i+1][randint(0,len(self.layers[i+1]))]
                    #node.add_connection(n)
                j+=1
            i+=1

    def get_data(self):
        return self.layers
    
initial_data = {
    'num_layers' : 5,
    'max_nodes_in_layer' : 3,
    'max_node_connection' : 2,
}

if __name__ == '__main__':
    sys = System(**initial_data)
    nodes = sys.get_data()
    app = QApplication([])
    r = Renderer(nodes)
    r.show()
    app.exec_()
