from queue import Queue

#######################################################################################################
#											   Functions											  #
#######################################################################################################

def check(start) :    # checking start input
	if start == "A" or start == "B" or start == "C" or start == "D" or start == "E" or start == "F" or start == "G" or start == "H" :
		return "true"
	else :
		return "false" 
def check2(end) :     # checking end input
	if end == "A" or end == "B" or end == "C" or end == "D" or end == "E" or end == "F" or end == "G" or end == "H" :
		return "true"
	else :
		return "false"
	
def getKeys(dictOfElements, valueToFind): # return the keys of specific value
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys


def bfs(start,end,flag) : 	# the BFS Algorithm Function
	
	BFS = [] 	       		    # used to register BFS total output 
	BFS2 = [] 	       		    # used to register BFS output 
	explored = [] 			    # used to register already visited points				
	temp = Queue() 	 			# used for Temp Register				
	level = {} 		  			# used for Levels register
	if flag == "p" :
		points_w = points_p
	elif flag == "n" :
		points_w = points_n
	
	level[start] = 0
	explored.append(start)
	temp.put(start)
	
	while not temp.empty() :
		
		x = temp.get()  		# get start point from Temp Queue and remove it from Temp
		BFS.append(x)   		# Register in BFS output

		for i in points_w[x] :
			if i not in explored :
				level[i] = level[x]+1	# Level of current point 
				explored.append(i) 		# Registered to explored list (to prevent infinite looping)
				temp.put(i)		   		# put i in Temp Queue
	
	for k in BFS : 						# Register the Path of Algorithm Until end Point only
		if k == end :
			BFS2.append(k)
			break 
		BFS2.append(k)
		

	var = getKeys(level, level[end])	# get all other points had the same level of end point
	for l in var :
		if l != end and l not in BFS2 :
			BFS2.append(l)
	
	print("\nBFS Traversal Output Path is : ",BFS)
	print("BFS Path until End Point Level : ",BFS2)
	print("The Level of Each Point : ",level)
	print("\n")

#######################################################################################################
#											   Dictionaries  		    							  #
#######################################################################################################

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

#######################################################################################################
#												  Main												  #
#######################################################################################################

print("\n\t B \u2500 C   E \u2500 G")
print("\t |   | \u2571 | ")
print("\t A   D \u2500 F \u2500 H\n")

start = input("Select Start Point From Algorithm : ") 
end = input("Select Start Point From Algorithm : ")

end = end.upper()     	# used for users case senstive errors
start = start.upper() 	# used for users case senistive errors

if check(start) == "true" and check2(end) == "true" :
	 check = "true"
else : 
	print("\nInvalid Inputs")
	print("Program Quit ...\n")	
	exit()

if start < end : 		# direction is positive 
	flag = "p"

elif start > end : 		# direction is negative
	flag = "n"
else : 				 	# start point and end point are same
	print("The BFS Output Path is : ",start)
	exit()
		
bfs (start,end,flag)