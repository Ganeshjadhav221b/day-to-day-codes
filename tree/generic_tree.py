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
            if(self.root is not None):
                self.nodes.peek().children.append(node)
            else:
                self.root = node
            self.nodes.add(node)
        
    def view(self, node):
        if node is not None:
            print(node, len(node.children))
        for child in node.children:
            self.view(child)

    #no. of nodes
    def size(self, node, count = 0):
        #To understand why we must store the count in variable (in for loop):  count = self.size(child, count)
        #Refer pass by reference: https://realpython.com/python-pass-by-reference/ & https://stackoverflow.com/a/25670170/7467083
        if node is not None:
            count += 1
            for child in node.children:
                count = self.size(child, count)
        return count

    #TODO: finish this
    def size2(self, node, count = 0):
        if node is not None:
            # print('Here:',node, len(node.children), count)
            for child in node.children:
                count = self.size2(child, count + len(node.children))
        return count 

    def maximum(self, node, maximum = -999):
        if node is not None:
            #print('Here:',node.data, len(node.children), maximum)
            data = node.data
            for child in node.children:
                maximum = max(maximum, self.maximum(child, data))
        #print('returning: ', maximum, node.data, max(maximum, node.data))
        return max(maximum, node.data) 

    def height(self, node):
        height = -1
        if node is not None:
            for child in node.children:
                height = max(height,self.height(child))
            height += 1
        return height

    def level_order_traversal(self, node):
        queue = list()
        queue.append(node)

        while len(queue)>0:
            node = queue.pop(0)
            print(node.data, end = ' ')

            for child in node.children:
                queue.append(child)
        print()
    
    #leaf nodes in original example- 3,6,9
    def leaf_nodes(self, node):
        if node is not None and len(node.children) == 0:
            print(node.data, end = ' ')
        for child in node.children:
            self.leaf_nodes(child)

    #    10                    a
    #   |   \                 |   \  
    #   3    5                b    c
    #       |  \              | \
    #       6   9             d   e
    #   above 2 diagrams are mirror(not to consider data, but only the pattern)
    def is_mirror(self, node1 , node2):
        is_mirror = True
        # print('Here: ',node1.children,'ppp',node2.children[::-1], len(node1.children) ,len(node2.children))
        if len(node1.children) != len(node2.children):
            return False
        for child1, child2 in zip(node1.children,node2.children[::-1]):
            is_mirror = self.is_mirror(child1, child2)
        return is_mirror and True

    #    10                    a
    #   |   \                 |   \  
    #   3    5                b    c
    #       |  \                   | \
    #       6   9                  d   e
    #   above 2 diagrams are symmetric(not to consider data, but only the pattern)
    def is_symmetric(self, node1 , node2):
        is_symmetric = True
        if len(node1.children) != len(node2.children):
            return False
        for child1, child2 in zip(node1.children,node2.children):
            is_symmetric = self.is_symmetric(child1, child2)
        return is_symmetric and True

    #example- given 9, 10->5->9
    def node_to_root_path(self, currentNode, targetNode):
        path = list()
        if currentNode.data == targetNode.data:
            path.append(currentNode.data)
            return path
        for child in currentNode.children:
            path = self.node_to_root_path(child, targetNode)
            if len(path) > 0:
                path.append(currentNode.data)
                return path
        return path
    #in case of original, 3 and 6's ancesstor is 10

    #    10                    
    #   |   \                   
    #   3    5                    
    #       |  \              
    #       6    9
    #       | \ 
    #       7  8        
    #In above case, LCA for 7 & 9 is 5   
    def lowest_common_ancesstor(self):
        pass

    #    10                    
    #   |   \                   
    #   3    5                    
    #       |  \              
    #       6    9
    #       | \ 
    #       7  8        
    #In above case, distance between 7 & 9 is 3(7->6, 6->5, 5->9)  
    def distance_between_nodes(self):
        pass

    def maximum_subtree_sum(self):
        pass

    def diameter(self):
        pass


def test_generic_tree():
    inpList = [10,3,-1,5,6,-1,9]
    inpList = [10,3,-1,5,6,7,-1,8,-1,-1,19]
    
    tree = GenericTree()
    for inp in inpList:
        tree.insert(inp)

    tree.view(tree.root)
    print('Number of nodes : ',tree.size(tree.root))
    #We've to add 1 as root wont be counted initially
    # print('Number of nodes (without pass by ref): ',tree.size2(tree.root) + 1)

    print("max in tree: ", tree.maximum(tree.root))

    print("height of tree: ", tree.height(tree.root))
    print('level order traversal: ')
    tree.level_order_traversal(tree.root)
    print('leaf nodes: ')
    tree.leaf_nodes(tree.root)
    print()

    mirroredList = [10,3,5,-1,6,-1,-1,9]

    tree2= GenericTree()
    for inp in mirroredList:
        tree2.insert(inp)
    print('is mirror: ', tree.is_mirror(tree.root, tree2.root))

    print('is symmetric: ', tree.is_symmetric(tree.root, tree2.root))
    print('node to root path: ', tree.node_to_root_path(tree.root, GenericTreeNode(7)))
test_generic_tree()
