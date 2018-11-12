from collections import deque
from myLib import Classes, MiscFuncs
import time

#Our BFS Function
def BFS(myDict, myNode):
    startTime = time.time()
    counter = 1

    #need our queue for this to work properly
    queue = deque([])

    #and then add to the queue
    queue.append(myNode)

    currentNode = None
    goalStateReached = False
    depth = 0

    #We are going to loop until the queue is empty or we find the goal state
    while queue is not [] or goalStateReached is False:
        #remove the left most item in our list, which is acting like a queue thanks to the import deque
        try:
            currentNode = queue.popleft()
            #In some cases, there is an indexing error when the deque is empty, this handles that
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
                depth = currentNode.depth + 1
                myDict[strUpState] = counter
                upPath = currentNode.path + upState
                newNode = Classes.Node(strUpState, upState, None, upPath, depth) 
                queue.append(newNode)
        #Remaining directional moves follow the same logic
        if right:
            rightState = MiscFuncs.swapRight(currentNode.listState, zeroPosition)
            strRightState = MiscFuncs.createStringState(rightState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strRightState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strRightState] = counter
                rightPath = currentNode.path + rightState
                newNode = Classes.Node(strRightState, rightState, None, rightPath, depth) 
                queue.append(newNode)
        if down:
            downState = MiscFuncs.swapDown(currentNode.listState, zeroPosition)
            strDownState = MiscFuncs.createStringState(downState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strDownState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strDownState] = counter
                downPath = currentNode.path + downState
                newNode = Classes.Node(strDownState, downState, None, downPath, depth) 
                queue.append(newNode)
        if left:
            leftState = MiscFuncs.swapLeft(currentNode.listState, zeroPosition)
            strLeftState = MiscFuncs.createStringState(leftState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strLeftState)
            if alreadyInDict is False:
                counter += 1
                depth = currentNode.depth + 1
                myDict[strLeftState] = counter
                leftPath = currentNode.path + leftState
                newNode = Classes.Node(strLeftState, leftState, None, leftPath, depth) 
                queue.append(newNode)
    endTime = time.time()
    #Check if the goal state was reached
    if goalStateReached is False:
        print("No Solution")
        print("Depth:", currentNode.depth)
        print("Nodes Created:", counter)
        print("Elapsed Time:", endTime - startTime)
        #MiscFuncs.creatCSV_NS(currentNode, myNode.listState, counter, 1, endTime - startTime)
    else:
        #display information about last node/state
        MiscFuncs.printGoalState(currentNode, counter, 1, endTime - startTime, myNode.listState)