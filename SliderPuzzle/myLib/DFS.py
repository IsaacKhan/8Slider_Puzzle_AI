from myLib import Classes, MiscFuncs

#Our BFS Function
def DFS(myDict, myNode, counter):
    #need our stack for this to work properly
    stack = []

    #and then add to the stack
    stack.append(myNode)

    currentNode = None
    goalStateReached = False
    depth = 0

    #We are going to loop until the stack is empty or we find the goal state
    while stack or goalStateReached is False:
        #remove item from stack and load into holder node
        currentNode = stack.pop()

        goalStateReached = MiscFuncs.checkGoalState(currentNode)
        if goalStateReached is True:
            break

        zeroPosition = MiscFuncs.findEmptyPosition(currentNode.listState)

        #Start off by finding out our valid moves
        up = MiscFuncs.checkUp(zeroPosition)
        down = MiscFuncs.checkDown(zeroPosition)
        left = MiscFuncs.checkLeft(zeroPosition)
        right = MiscFuncs.checkRight(zeroPosition)

        depth += 1

        #Follows same logic as BFS, just using a stack/list as opposed to a queue/deque
        if up:
            upState = MiscFuncs.swapUp(currentNode.listState, zeroPosition)
            strUpState = MiscFuncs.createStringState(upState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strUpState)
            if alreadyInDict is False:
                counter += 1
                myDict[strUpState] = counter
                newNode = Classes.Node(strUpState, upState, None, [], depth) 
                stack.append(newNode)
        if right:
            rightState = MiscFuncs.swapRight(currentNode.listState, zeroPosition)
            strRightState = MiscFuncs.createStringState(rightState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strRightState)
            if alreadyInDict is False:
                counter += 1
                myDict[strRightState] = counter
                newNode = Classes.Node(strRightState, rightState, None, [], depth) 
                stack.append(newNode)
        if down:
            downState = MiscFuncs.swapDown(currentNode.listState, zeroPosition)
            strDownState = MiscFuncs.createStringState(downState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strDownState)
            if alreadyInDict is False:
                counter += 1
                myDict[strDownState] = counter
                newNode = Classes.Node(strDownState, downState, None, [], depth) 
                stack.append(newNode)
        if left:
            leftState = MiscFuncs.swapLeft(currentNode.listState, zeroPosition)
            strLeftState = MiscFuncs.createStringState(leftState)
            alreadyInDict = MiscFuncs.checkMyDict(myDict, strLeftState)
            if alreadyInDict is False:
                counter += 1
                myDict[strLeftState] = counter
                newNode = Classes.Node(strLeftState, leftState, None, [], depth) 
                stack.append(newNode)

    if goalStateReached is False:
        print("No Solution")
    else:
        MiscFuncs.printGoalState(currentNode)