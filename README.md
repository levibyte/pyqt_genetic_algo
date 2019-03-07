# PyQt Genetic Algo
Simple implementation and visualisation of genetic algorithm in work using Python & Qt. 

### Backround
Genetic algorithm is special technique for solving optimization problems,
specialy in places where there are a lot of combinations and finding optimal solotion by simply brute-forcing is impossible.

### The task to solve
The Aim of this project is to demonstrate optimized cell placement to complete efficient routing
Optimization should meet following criterias.
* Each node when moved should preserve it's connectivity ( parent & child connections )
* Cell position can be adjusted within same colum ( cell can be only poped/pushed vertically, horizontal moves not allowed)
* Intersections/crossings beetween  should be minimal.

### Implementation
I've used MVC pattern to abstract the data from renderer.
Theortically should be possible to add any view that can will use get_data function returning 2D array of nodes used and renderer them.


### Examples 
*Left:* Initial placmenet  &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Right:* optimized placement

<img src="https://i.ibb.co/C2gyWWf/bef.png" width="400" height="500">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img src="https://i.ibb.co/0ttqnFY/aft.png" width="400" height="500">



### More complicated cases

Placement before ( 51 crossings )
<img src="https://i.ibb.co/YDR5PKS/1.png">


Optimized ( 1 crossing )
<img src="https://i.ibb.co/2dmL5sC/2.png">


