from libs.node import *
from libs.placement import Placement
from libs.placement_controller import PlacementController
from libs.optimizer import Optimizer

from PyQt4.QtGui import *
#from PyQt5.QtWidgets import *
from PyQt4.QtCore import *

initial_settings = {
    'num_layers' : 13,
    'max_nodes_in_layer' : 6,
    'min_node_connection' : 1,
    'max_node_connection' : 1,
}


class Canvas(QWidget):
    def __init__(self, controller, *args, **kwargs):
        super(Canvas, self).__init__(*args, **kwargs)
        self.controller = controller
        self.tx = 100
        self.ty = 100
        self.dx = 50
        self.dy = 50
        #create placement
        self.placement = Placement(**initial_settings)

        #set 
        self.controller.set_data(self.placement.get_data())
        self.nodes = self.controller.get_placement()
        print("Intersctions: {}".format(self.controller.calc_intersections()))
        print("Click on canvas to start optimization...")

        
    def keyPressEvent(self, event):
        self.placement = Placement(**initial_settings)
        self.controller.set_data(self.placement.get_data())
        self.nodes = self.controller.get_placement()
        QWidget.repaint(self)
        

    def mouseReleaseEvent(self, event):
        #optimize placement, using placement controller
        optimizer = Optimizer(self.placement,self.controller)
        
        self.nodes = self.controller.get_placement()
        #print("Count: {}".format(self.controller.calc_intersections()))
        QWidget.repaint(self)
        #self.paintEvent(event)
        #self.draw()
        #ev = QResizeEvent(QSize(1000,1000),QSize(1000,1000))
        #QMainWindow.resizeEvent(self, ev)
     
    def paintEvent(self, event):
        self.draw()
        
    #def dummy(self):
        
    def draw(self):
        i = 0
        for layer in self.nodes:
            j = 0
            for node in layer:
                #self.draw_node_and_its_connections(node)    
                #self.draw_connections(i,j,node.get_connected())
                #FIXME elimiate ghost nodes
                #if not node.get_parents() and not node.get_connected():
                #    print("")
                #else:
                self.draw_node(i,j,node)
                
                self.draw_connections(i,j,node.get_connected())
                j += 1
            i += 1
            
    def draw_connections(self,i,j,nodes):
        for node in nodes:
            self.draw_connection(i,j,node)
            
    def draw_node(self,i,j,node):
        #print("drawing {} {}".format(i,j))
        #i,j = sys.find_ij(node)
        r,g,b = node.get_color()
        color = QColor(r,g,b)
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        r = QRect(self.tx*i+self.dx,self.ty*j+self.dy,20,20)
        outer, inner = Qt.black, color        
        p.fillRect(r, QBrush(inner))
        pen = QPen(outer)
        pen.setWidth(1)
        p.setPen(pen)
        p.drawRect(r)
        
        p.drawText(self.tx*i+self.dx,self.ty*j+self.dy,node.get_name())
        
    def draw_connection(self,i,j,node):
        di,dj = self.controller.find_ij(node)
        #print("drawing connection from (){}{} to ({}){}{}".format(i,j,node.get_name(),di,dj))
        
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        #FIXME tuple
        r,g,b = node.get_color()
        color = QColor(r,g,b)
        pen = QPen(color, 3)
        p.setPen(pen)
        p.drawLine(10+self.tx*i+self.dx,10+self.ty*j+self.dy,10+self.tx*di+self.dx,10+self.ty*dj+self.dy)
        

    
class MainWindow(QMainWindow):
    def __init__(self, controller, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #nodes = sys.get_data()
        canvas = Canvas(controller)
        self.setCentralWidget(canvas)
        

class Renderer():
    #def __init__(self,p_c):        
    #    self.controller = p_c

    def __init__(self):
        i = 0
        
    def render(self):       
        #create placement controller
        self.controller  = PlacementController()
        
        #create placement
        #placement = Placement(**initial_settings)

        app = QApplication([])
        r = MainWindow(self.controller)
        r.show()
        app.exec_()
        
        
