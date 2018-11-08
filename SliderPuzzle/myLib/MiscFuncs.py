import random, copy

def UserMenu():
    #You don't need comments for this.
    print("\t\t\t*****************")
    print("\t\t\t* Slider Puzzle *")
    print("\t\t\t*****************\n")
    print("Enter a number corresponding to the action you wish to take")
    print("-----------------------------------------------------------------------")
    print("If you don't create your own starting state, or opt to have")
    print("one created for you, a default starting state will be used.")
    print("-----------------------------------------------------------------------")
    print("Q. Exit the program")
    print("H. Help: Redisplay the menu")
    print("1. Enter your own starting state")
    print("2. Generate a random starting state")
    print("3. Run a Breadth First Search on generated starting state")
    print("4. Run a Depth First Search on a generated starting state")
    print("5. Run an A Star-Misplaced Tiles Search on a generated starting state")
    print("-----------------------------------------------------------------------\n\n")

def getUserInput():
    #Loop infinitly until the user inputs valid data
    while True:
        userInput = str(input())
        #If userInput is not in the list here, we give a prompt and continue retrieiving input
        if userInput not in ("q", "Q", "h", "H", "1", "2", "3", "4", "5"):
            print("Select one of the listed options above.")
        else:
            break
    return userInput

def createRows(state):
    #This is used to split a single, long list into a multi-D list
    newState = [[], [], []]
    i = 0
    j = 0

    while i < 3:
        newState[i].append(state[j])
        if j == 2 or j == 5 or j == 8:
            i += 1
        j += 1

    return newState

def createUserGeneratedState():
    genState = []
    #This all makes sure the user inputs valid data for a puzzle
    print("Enter a number between 0 to 8. This includes 0 and 8. Repeated numbers are not allowed.")
    while len(genState) < 9:
        while True:
            try:
                userInput = int(input())
                if userInput not in range(0, 9):
                    print("Please enter a number between 0 to 8.")
                if userInput in genState:
                    print("You've already entered that. Enter another number.")
                else:
                    break
            #Sometimes there is a value error that occurs because int() can't convert everything into an int
            #So we tell user to enter an integer
            except ValueError:
                print("Please enter an integer")
        #once we get valid input, we add to the list
        genState.append(userInput)
    #then we split the list, or create the 3 rows for the puzzle 
    genState = createRows(genState)

    return genState

def generateRandomState():
    genState = []   
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    #I decided to have a list of ints and randomly select one of them 
    # to add into the genState. Once a number is used, it is replaced
    # with an x, so the program knows to try again. Once done, we split the list.
    while len(genState) < 9:
        postion = random.randint(0, 8)
        if nums[postion] is not "x":
            genState.append(nums[postion])
            nums[postion] = "x"
    genState = createRows(genState)

    return genState

def createStringState(state):
    stringState = ""
    i = 0
    j = 0

    #converts the list version of the State into a string and returns it
    while i < 3:
        stringState += str(state[i][j])
        if j == 2:
            i += 1
            j = 0
        else:
            j += 1
    return stringState

def findEmptyPosition(startingState):
    row = 0
    column = 0

    #Uses the list state to find the position of the zero and returns that location 
    while row < 3:
        if startingState[row][column] == 0:
            blankPosition = [row, column]
        if column == 2:
            row += 1
            column = 0
        else:
            column += 1
    return blankPosition

def calculateMisplacedTiles(state):
    goalstate = [ [1,2,3], [4,5,6], [7,8,0] ]
    tempNode = copy.deepcopy(state)
    i = 0
    j = 0
    misplaced = 0

    while i < 3:
        if tempNode[i][j] is not goalstate[i][j]:
            misplaced += 1
        if j is 2:
            i += 1
            j = 0
        else:
            j += 1
 
    return misplaced

#function that checks the value of the location up one space from our current location
def checkUp(zeroPosition):
    if zeroPosition[0] is not 0: 
        #valid move  
        return True
    else:
        #invalid move
        return False

def swapUp(state, zeroPosition):
    tempState = copy.deepcopy(state)

    #hold value above zero position
    holdMyInt = tempState[zeroPosition[0] - 1][zeroPosition[1]]

    #set the given zero postion to above position
    tempState[zeroPosition[0]][zeroPosition[1]] = holdMyInt

    #set above position to 0
    tempState[zeroPosition[0] - 1][zeroPosition[1]] = 0

    return tempState

#function that checks the value of the location down one space from our current location
def checkDown(zeroPosition):
    if zeroPosition[0] is not 2:   
        return True
    else:
        return False

def swapDown(state, zeroPosition):
    tempState = copy.deepcopy(state)

    #hold value above zero position
    holdMyInt = tempState[zeroPosition[0] + 1][zeroPosition[1]]

    #set the given zero postion to above position
    tempState[zeroPosition[0]][zeroPosition[1]] = holdMyInt

    #set above position to 0
    tempState[zeroPosition[0] + 1][zeroPosition[1]] = 0

    return tempState

#function that checks the value of the location left one space from our current location
def checkLeft(zeroPosition):
    if zeroPosition[1] is not 0:   
        return True
    else:
        return False

def swapLeft(state, zeroPosition):
    tempState = copy.deepcopy(state)

    #hold value above zero position
    holdMyInt = tempState[zeroPosition[0]][zeroPosition[1] - 1]

    #set the given zero postion to above position
    tempState[zeroPosition[0]][zeroPosition[1]] = holdMyInt

    #set above position to 0
    tempState[zeroPosition[0]][zeroPosition[1] - 1] = 0

    return tempState

#function that checks the value of the location right one space from our current location
def checkRight(zeroPosition):
    if zeroPosition[1] is not 2:   
        return True
    else:
        return False

def swapRight(state, zeroPosition):
    tempState = copy.deepcopy(state)

    #hold value above zero position
    holdMyInt = tempState[zeroPosition[0]][zeroPosition[1] + 1]

    #set the given zero postion to above position
    tempState[zeroPosition[0]][zeroPosition[1]] = holdMyInt

    #set above position to 0
    tempState[zeroPosition[0]][zeroPosition[1] + 1] = 0

    return tempState

def checkGoalState(myNode):
    stringGS = '123456780'

    if myNode.stringState == stringGS:
        return True
    else:
        return False

def checkMyDict(myDict, state):
    if state in myDict:
        return True
    else:
        return False

def printGoalState(stateNode, counter, alg, time):    
    print("Goal State Information:")
    print("---------------------------------------------------------------------")
    print("State as a List:", stateNode.listState)
    print("State as a String:", stateNode.stringState)
    
    #Only use this block when the path is actually recorded
    if alg is not 2:
        print("Path:")
        for item in range(len(stateNode.path)):
            print(stateNode.path[item])
            if (item + 1) % 3 is 0:
                print("")
    print("Elapsed Time:", time)
    print("Depth:", stateNode.depth)
    print("Nodes created:", counter)
