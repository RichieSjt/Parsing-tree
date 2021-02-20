class Node(object):

    '''This object stores data used to generate the parsing tree.'''
    
    def __init__(self, label, depth, leaves, parent, is_final):
        '''
        Args:
            label (str): The string that resulted from parsing
            depth (int): The depth of the node in the tree
            leaves (list): A list of references to the children nodes
            parent (Node): The parent of this node.
            is_final (boolean): If the string is accepted then a path is 
                established through the nodes that have this value as True.
        '''
        self.label = label
        self.depth = depth
        self.leaves = leaves
        self.parent = parent
        self.is_final = is_final