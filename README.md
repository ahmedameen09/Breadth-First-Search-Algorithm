# Breadth-First-Search-Algorithm
this Breadth First Search Algorithm implemented by python for algorithms & Data-structure students 
the BFS is an algorithmic method from the searching algorithms

#####################################################################################################

computers can't understand the graphical algorithms and it's shape without computer vision
so all we do in this project is converting the drawn graph to some points used in a dictionary

points_p = { 
	"A" : [ "B" ],
	"B" : [ "C" , "A" ],
	"C" : [ "D" , "B" ],
	"D" : [ "E" , "F" , "C" ],
	"E" : [ "F" , "G" , "D" ],
	"F" : [ "H" , "E" , "D" ],
	"G" : [ "E" ],
	"H" : [ "F" ]
} # points we have in algorithm contain it's adjacent points (Positive direction)
		
points_n = { 
	"A" : [ "B" ],
	"B" : [ "A" , "C" ],
	"C" : [ "B" , "D" ],
	"D" : [ "C" , "F" , "E" ],
	"E" : [ "D" , "G" , "F" ],
	"F" : [ "D" , "E" , "H" ],
	"G" : [ "E" ],
	"H" : [ "F" ]
} # points we have in algorithm contain it's adjacent points (Negative direction)

any algorithm start searching from the left points to the right so we must consider that points - 
from the end of graph has left position diffrent from the start of the graph
so we considered that we have 2 directions +ve and -ve direction

#######################################################################################################

each direction contains the point from left to right from its position 

the +ve direction detected in the algorithm from the start and end point we take from user

if start < end : 		# direction is positive 

elif start > end : 		# direction is negative

then we have start point , end point and flag with the direction we sent them to the bfs function

the bfs function uses queue from the Data-sturctures to temp storing and deleting the points in the begining of algorithm

- the queue start with start point and store it then getting it in variable and deleting it from queue
- the point stored in explored list as we prevent the infinty looping 
- the for loop take the adjacent points to tha main point and start to give it higher level and check if it the end poind we want or not
- the points stored in queue as new points level we must search in thier branches
- after for looping the the second points stored in queue started to getting in variable and had the same last operation
- after the queue is empty the algorithmic bfs path had been detected from the start point
- then we detect the end point and all the points we have in the same level of the end point to stored in the BFS2 list 
- finally we printing the BFS full path - the BFS path from start to end point level - the levels of all points
