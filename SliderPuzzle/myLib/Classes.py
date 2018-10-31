class Node:
    #this is the constructor for the class Node
    #as you can see, it has default values if none are provided
    def __init__(self, stringState = "", listState = [], h = None, p = [], d = None):
        self.stringState = stringState
        self.listState = listState
        self.heuristicVal = h
        self.path = p
        self.depth = d