import heapq, time
from myLib import Classes, MiscFuncs

#Our BFS Function
def misplacedTiles(myDict, myNode):
    startTime = time.time()
    counter = 1

    #need our queue for this to work properly
    priority_queue = []

    #and then add to the priority queue
    heapq.heappush(priority_queue, myNode)

    currentNode = None
    goalStateReached = False
    depth = 0

    #We are going to loop until the priority queue is empty or we find the goal state
    while priority_queue is not [] or goalStateReached is False:
        #remove the smallest item in our list, which is acting like a queue thanks to the import deque
        try:
            currentNode = heapq.heappop(priority_queue)
            #In some cases, there is an indexing error, this handles that
        except IndexError:
            break

        #check if goalState has been reached
        goalStateReached = MiscFuncs.checkGoalState(currentNode)
        if goalStateReached is True:
            break

        #Find the zero's position on the puzzle
        zeroPosition = MiscFuncs.findEmptyPosition(currentNode.listState)

        #Start off by finding out our valid moves
        up = MiscFuncs.checkUp(zeroPosition)
        down = MiscFuncs.checkDown(zeroPosition)
        left = MiscFuncs.checkLeft(zeroPosition)
        right = MiscFuncs.checkRight(zeroPosition)

        #Adjust the depth
        depth += 1

        #do a temp State swap to comapre against dictionary if state exsist or not
        if up:
            #generate our possible state, create a string version of it, and look in the dictionary if this state exist
            upState = MiscFuncs.swapUp(currentNode.listState, zeroPosition)
            strUpState = MiscFuncs.createStringState(upState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strUpState)
            if alreadyInDict is False:
                #Since it isn't in the dictionary, we can increment the counter,
                # add to state and counter to the dictionary, create a new node for the state,
                # and push node onto the queue
                counter += 1
                myDict[strUpState] = counter
                upPath = currentNode.path + upState
                heuristic = MiscFuncs.calculateMisplacedTiles(currentNode.listState)
                newNode = Classes.Node(strUpState, upState, heuristic, upPath, depth) 
                heapq.heappush(priority_queue, newNode)
        #Remaining directional moves follow the same logic
        if right:
            rightState = MiscFuncs.swapRight(currentNode.listState, zeroPosition)
            strRightState = MiscFuncs.createStringState(rightState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strRightState)
            if alreadyInDict is False:
                counter += 1
                myDict[strRightState] = counter
                rightPath = currentNode.path + rightState
                heuristic = MiscFuncs.calculateMisplacedTiles(currentNode.listState)
                newNode = Classes.Node(strRightState, rightState, heuristic, rightPath, depth) 
                heapq.heappush(priority_queue, newNode)
        if down:
            downState = MiscFuncs.swapDown(currentNode.listState, zeroPosition)
            strDownState = MiscFuncs.createStringState(downState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strDownState)
            if alreadyInDict is False:
                counter += 1
                myDict[strDownState] = counter
                downPath = currentNode.path + downState
                heuristic = MiscFuncs.calculateMisplacedTiles(currentNode.listState)
                newNode = Classes.Node(strDownState, downState, heuristic, downPath, depth) 
                heapq.heappush(priority_queue, newNode)
        if left:
            leftState = MiscFuncs.swapLeft(currentNode.listState, zeroPosition)
            strLeftState = MiscFuncs.createStringState(leftState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strLeftState)
            if alreadyInDict is False:
                counter += 1
                myDict[strLeftState] = counter
                leftPath = currentNode.path + leftState
                heuristic = MiscFuncs.calculateMisplacedTiles(currentNode.listState)
                newNode = Classes.Node(strLeftState, leftState, heuristic, leftPath, depth) 
                heapq.heappush(priority_queue, newNode)
    endTime = time.time()
    #Check if the goal state was reached
    if goalStateReached is False:
        print("No Solution")
        print("Nodes Created:", counter)
        print("Elapsed Time:", endTime - startTime)
    else:
        #display information about last node/state
        MiscFuncs.printGoalState(currentNode, counter, 3, endTime - startTime)