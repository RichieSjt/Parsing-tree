
def print_tree(root):

    '''Method to recursively print the tree in the console, only used for debugging purposes.'''
    
    #Printing the root and then all of its children
    print("-------", root.label, "childrens:")
    for children in root.leaves:
        print(children.label, "depth:", children.depth)

    #Repeating the above process for every children
    for children in root.leaves:
        if children.leaves:
            print_tree(children)