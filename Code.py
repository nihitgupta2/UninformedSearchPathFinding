# Nihit Gupta 
# Id 20759430
import random

def breathFirstSearch(maze,startPosition,endPositions,breakingScheme):
    #open queue list is a fifo list
    openQueue = [startPosition]
    closedQueue = []
    currentPosition = None
    nodeCounter = 0
    finalEndNode = None
    allPositions = []
    traversalDict = {}
    while openQueue!=[]: 
        currentPosition = openQueue.pop(0)
        allPositions.append(currentPosition)
        nodeCounter+=1
        if currentPosition in endPositions:
            finalEndNode = currentPosition
            print(f"Goal Node Reached {finalEndNode}")
            print(f"Total Nodes Expanded = {nodeCounter}")
            break
            # goal node found so break
        else:
            childNodes = findAllChildNodes(maze,currentPosition,breakingScheme)
            childNodesNoRep = [i for i in childNodes if i not in closedQueue and i not in openQueue]
            openQueue.extend(childNodesNoRep)
            #print(openQueue)
            closedQueue.append(currentPosition)
            traversalDict[tuple(currentPosition)]=childNodesNoRep
    
    route = pathFinder(traversalDict,finalEndNode)
    print(route)
    print(f"The total cost for BFS with breaking scheme {breakingScheme} is {len(route)}")
    print("-------------------------------------------------------------")
    print(allPositions)
    return route



def depthFirstSearch(maze,startPosition,endPositions,breakingScheme):
    # open queue list is a lifo list
    openQueue = [startPosition]
    closedQueue = []
    currentPosition = None
    nodeCounter = 0
    finalEndNode = None
    allPositions = None
    traversalDict = {}
    while openQueue!=[]: 
        currentPosition = openQueue.pop()
        #print(currentPosition)
        nodeCounter+=1
        if currentPosition in endPositions:
            finalEndNode = currentPosition
            print(f"Goal Node Reached {finalEndNode}")
            print(f"Total Nodes Expanded = {nodeCounter}")
            break
            # goal node found so break
        else:
            childNodes = findAllChildNodes(maze,currentPosition,breakingScheme)
            childNodes.reverse()
            childNodesNoRep = [i for i in childNodes if i not in closedQueue]
            openQueue.extend(childNodesNoRep)
            closedQueue.append(currentPosition)
            traversalDict[tuple(currentPosition)]=childNodesNoRep
    
    route = pathFinder(traversalDict,finalEndNode)
    print(route)
    print(f"The total cost for DFS with breaking scheme {breakingScheme} is {len(route)}")
    return route
 


def pathFinder(pathDict,goalNode):
    # this function finds the actual path taken by the agent
    totalPath = [goalNode]
    #this function takes a goal node and check in the dictionary to find the parent node
    #using recusrsion we find all parent nodes and thus get the actual path
    def recursiveFinding(pathDict,goalNode):
        if goalNode == [2,11]:
            return 0
        else:
            iterNode = goalNode
            for key,val in pathDict.items():
                if iterNode in val:
                    totalPath.append(list(key))
                    iterNode = list(key)
                    recursiveFinding(pathDict,iterNode)

    recursiveFinding(pathDict,goalNode)
    totalPath.reverse()
    return totalPath



def findAllChildNodes(maze,currentPosition,breakingScheme):
    upPosition = None
    downPosition = None
    leftPosition = None
    rightPosition = None
    childNodes = None
    finalChildren = None
    # checking non is out of boud or blocked and then considering them as a child node
    if (currentPosition[1]+1)<25 and (currentPosition[1]+1)>=0 and maze[currentPosition[1]+1][currentPosition[0]]!=1:
        upPosition = [currentPosition[0],currentPosition[1]+1]

    if (currentPosition[1]-1)<25 and (currentPosition[1]-1)>=0 and maze[currentPosition[1]-1][currentPosition[0]]!=1:
        downPosition = [currentPosition[0],currentPosition[1]-1]
    
    if (currentPosition[0]+1)<25 and (currentPosition[0]+1)>=0 and maze[currentPosition[1]][currentPosition[0]+1]!=1:
        rightPosition = [currentPosition[0]+1,currentPosition[1]]
    
    if (currentPosition[0]-1)<25 and (currentPosition[0]-1)>=0 and maze[currentPosition[1]][currentPosition[0]-1]!=1:
        leftPosition = [currentPosition[0]-1,currentPosition[1]]
    
    if breakingScheme == "LURD":
        childNodes = [leftPosition,upPosition,rightPosition,downPosition]
        finalChildren = [i for i in childNodes if i is not None]
    elif (breakingScheme) == "RULD":
        childNodes = [rightPosition,upPosition,leftPosition,downPosition]
        finalChildren = [i for i in childNodes if i is not None]
    else:
        print("Please Enter the correct Breaking Ties Scheme")
    
    return finalChildren



def generateGraph(maze,actualPath):
    # maze_copy = maze
    
    # "_" means blocks that can used i.e. positions where agent can go
    # "#" means blocks that are blocked and the agent 
    # "*" represents the blocks agent took in the actual path

    for i in range(24,-1,-1):
        mazeLine = ""
        for j in range(25):
            if [j,i] in actualPath:
                if i==11 and j==2:      # Start never changes
                    mazeLine+=" S "
                elif i==21 and j==2:    # E2 never changes
                    mazeLine+=" E "
                elif i==19 and j==23:   # E1 never changes
                    mazeLine+=" E "
                else:
                    mazeLine+=" * "
            elif maze[i][j] == 0:
                mazeLine+=" _ "
            elif maze[i][j] == 1:
                mazeLine+=" X "
            else:
                mazeLine+=" * "
        print(mazeLine)



def main ():
    totalspots = [25,25]
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]
    # I have assumed that in the given map on Learn the 0,0 is the bottom left square and the square 
    # on its right is 1,0 and the square above 0,0 is 0,1 and so on 
    # However in the above 2D arrays every sublist is a row and first sublist is the bottom most row
    # so in order to access 9,11 graph value I use 11,9 in 2D Array.
    # The coordinate values in output corresponds to the GRAPH. 
    S = [2,11]      #start position
    E1 = [23,19]    #Exit position 1 
    E2 = [2,21]     #Exit position 2
    endPositions = [E1,E2]
    breakingScheme1 = "LURD"
    breakingScheme2 = "RULD"
    print(f"------------------BFS with {breakingScheme1} Breaking ties scheme------------------")
    pathRouteBFS1 = breathFirstSearch(maze,S,endPositions,breakingScheme1)
    generateGraph(maze,pathRouteBFS1)

    print(f"------------------BFS with {breakingScheme2} Breaking ties scheme------------------")
    pathRouteBFS2 = breathFirstSearch(maze,S,endPositions,breakingScheme2)
    generateGraph(maze,pathRouteBFS2)

    print(f"------------------DFS with {breakingScheme1} Breaking ties scheme------------------")
    pathRouteDFS1 = depthFirstSearch(maze,S,endPositions,breakingScheme1)
    generateGraph(maze,pathRouteDFS1)

    print(f"------------------DFS with {breakingScheme2} Breaking ties scheme------------------")
    pathRouteDFS2 = depthFirstSearch(maze,S,endPositions,breakingScheme2)
    generateGraph(maze,pathRouteDFS2)
    



if __name__ == '__main__':
    main()