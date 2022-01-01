#Input of the tree would be in euler Path
#10 is root, has 2 children -> 3,5
#5 has 2 children 6,9
#    10
#   |   \
#   3    5
#       |  \
#       6   9
#
#input example 10,3,-1,5,6,-1,9
#Here -1 indicates that next data belongs to level up/parent's node

#idea here is to maintain stack, create node & push until we see -1.
#on -1, pop, and then continue pushing

#root: [10]
#first level : 10->3,10->5 -----10:[3,5]
#second level : 5->6, 5->9 -----5:[6,9]

class GenericTreeNode:
    def __init__(self, data):
        self.children = list()
        self.data = data
        
    def __repr__(self):
        return str(self.data)+"->"+''.join([str(elem) for elem in str(self.children)])

class Stack:
    def __init__(self):
      self.stack = list()

    def add(self, data):
         self.stack.append(data)

    def pop(self):
        self.stack.pop()
        
    def peek(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)

    def __str__(self):
        return ''.join([str(elem) for elem in str(self.stack)])
    
	
class GenericTree:
    def __init__(self):
        self.nodes = Stack()
        self.root = None
        
    def insert(self, data):
        node = None
        if data == -1:
            self.nodes.pop()
        else:
            node = GenericTreeNode(data)
            if(self.nodes.length() > 0):
                self.nodes.peek().children.append(node)
            else:
                self.root = node
            self.nodes.add(node)
        print('debug: ',data, self.nodes)
        
    def view(self, node):
        if node is not None:
            print(node)
        for child in node.children:
            self.view(child)
        

def test_generic_tree():
    inpList = [10,3,-1,5,6,-1,9]
    tree = GenericTree()
    for inp in inpList:
        tree.insert(inp)
    print('Here:', tree.root)
    tree.view(tree.root)

test_generic_tree()
