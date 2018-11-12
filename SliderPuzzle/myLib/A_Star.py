import heapq, time
from myLib import Classes, MiscFuncs

#Our BFS Function
def misplacedTiles(myDict, myNode):
    startTime = time.time()
    counter = 1

    #need our queue for this to work properly
    priority_queue = []

    #and then add to the priority queue
    heapq.heappush(priority_queue, (myNode.heuristicVal, myNode.listState, myNode))

    currentNode = None
    goalStateReached = False
    depth = 0

    #We are going to loop until the priority queue is empty or we find the goal state
    while priority_queue is not [] or goalStateReached is False:
        try:
            tempTuple = heapq.heappop(priority_queue)
            currentNode = tempTuple[2]
        except IndexError:
            break

        goalStateReached = MiscFuncs.checkGoalState(currentNode)
        if goalStateReached is True:
            break

        zeroPosition = MiscFuncs.findEmptyPosition(currentNode.listState)

        up = MiscFuncs.checkUp(zeroPosition)
        down = MiscFuncs.checkDown(zeroPosition)
        left = MiscFuncs.checkLeft(zeroPosition)
        right = MiscFuncs.checkRight(zeroPosition)

        if up:
            upState = MiscFuncs.swapUp(currentNode.listState, zeroPosition)
            strUpState = MiscFuncs.createStringState(upState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strUpState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strUpState] = counter
                upPath = currentNode.path + upState
                heuristic = MiscFuncs.calculateMisplacedTiles(upState, depth)
                newNode = Classes.Node(strUpState, upState, heuristic, upPath, depth) 
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
        if right:
            rightState = MiscFuncs.swapRight(currentNode.listState, zeroPosition)
            strRightState = MiscFuncs.createStringState(rightState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strRightState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strRightState] = counter
                rightPath = currentNode.path + rightState
                heuristic = MiscFuncs.calculateMisplacedTiles(rightState, depth)
                newNode = Classes.Node(strRightState, rightState, heuristic, rightPath, depth) 
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
        if down:
            downState = MiscFuncs.swapDown(currentNode.listState, zeroPosition)
            strDownState = MiscFuncs.createStringState(downState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strDownState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strDownState] = counter
                downPath = currentNode.path + downState
                heuristic = MiscFuncs.calculateMisplacedTiles(downState, depth)
                newNode = Classes.Node(strDownState, downState, heuristic, downPath, depth) 
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
        if left:
            leftState = MiscFuncs.swapLeft(currentNode.listState, zeroPosition)
            strLeftState = MiscFuncs.createStringState(leftState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strLeftState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strLeftState] = counter
                leftPath = currentNode.path + leftState
                heuristic = MiscFuncs.calculateMisplacedTiles(leftState, depth)
                newNode = Classes.Node(strLeftState, leftState, heuristic, leftPath, depth)
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
    
    endTime = time.time()
    if goalStateReached is False:
        print("No Solution")
        print("Depth:", currentNode.depth)
        print("Nodes Created:", counter)
        print("Elapsed Time:", endTime - startTime)
        #MiscFuncs.creatCSV_NS(currentNode, myNode.listState, counter, 3, endTime - startTime)
    else:
        MiscFuncs.printGoalState(currentNode, counter, 3, endTime - startTime, myNode.listState)

def manhattanDistance(myDict, myNode):
    startTime = time.time()
    counter = 1

    #need our queue for this to work properly
    priority_queue = []

    #and then add to the priority queue
    heapq.heappush(priority_queue, (myNode.heuristicVal, myNode.listState, myNode))

    currentNode = None
    goalStateReached = False
    depth = 0

    #We are going to loop until the priority queue is empty or we find the goal state
    while priority_queue is not [] or goalStateReached is False:
        try:
            tempTuple = heapq.heappop(priority_queue)
            currentNode = tempTuple[2]
        except IndexError:
            break

        goalStateReached = MiscFuncs.checkGoalState(currentNode)
        if goalStateReached is True:
            break

        zeroPosition = MiscFuncs.findEmptyPosition(currentNode.listState)

        up = MiscFuncs.checkUp(zeroPosition)
        down = MiscFuncs.checkDown(zeroPosition)
        left = MiscFuncs.checkLeft(zeroPosition)
        right = MiscFuncs.checkRight(zeroPosition)

        if up:
            upState = MiscFuncs.swapUp(currentNode.listState, zeroPosition)
            strUpState = MiscFuncs.createStringState(upState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strUpState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strUpState] = counter
                upPath = currentNode.path + upState
                heuristic = MiscFuncs.calculateManhattanDistance(upState, depth)
                newNode = Classes.Node(strUpState, upState, heuristic, upPath, depth) 
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
        if right:
            rightState = MiscFuncs.swapRight(currentNode.listState, zeroPosition)
            strRightState = MiscFuncs.createStringState(rightState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strRightState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strRightState] = counter
                rightPath = currentNode.path + rightState
                heuristic = MiscFuncs.calculateManhattanDistance(rightState, depth)
                newNode = Classes.Node(strRightState, rightState, heuristic, rightPath, depth) 
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
        if down:
            downState = MiscFuncs.swapDown(currentNode.listState, zeroPosition)
            strDownState = MiscFuncs.createStringState(downState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strDownState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strDownState] = counter
                downPath = currentNode.path + downState
                heuristic = MiscFuncs.calculateManhattanDistance(downState, depth)
                newNode = Classes.Node(strDownState, downState, heuristic, downPath, depth) 
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
        if left:
            leftState = MiscFuncs.swapLeft(currentNode.listState, zeroPosition)
            strLeftState = MiscFuncs.createStringState(leftState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strLeftState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strLeftState] = counter
                leftPath = currentNode.path + leftState
                heuristic = MiscFuncs.calculateManhattanDistance(leftState, depth)
                newNode = Classes.Node(strLeftState, leftState, heuristic, leftPath, depth)
                heapq.heappush(priority_queue, (newNode.heuristicVal, currentNode.listState, newNode))
    
    endTime = time.time()
    if goalStateReached is False:
        print("No Solution")
        print("Depth:", currentNode.depth)
        print("Nodes Created:", counter)
        print("Elapsed Time:", endTime - startTime)
        #MiscFuncs.creatCSV_NS(currentNode, myNode.listState, counter, 4, endTime - startTime)
    else:
        MiscFuncs.printGoalState(currentNode, counter, 4, endTime - startTime, myNode.listState)