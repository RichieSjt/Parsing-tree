from subprocess import check_call

f = open("tree.dot", "w")
#Writing into the file using the .dot format
f.write("digraph tree{")
#Creating a global node_id for the construction of the nodes in the dot file
node_id = 0

def visualize_tree(root):

    '''
    Generates a dot file that is then interpreted by Graphviz to generate a png file.
    
    Args:
        root (Node): The main root of the tree.
    '''
    global node_id

    #The global node_id must be reset in order to match the correct edges in the dot file
    node_id = 0
    build_nodes(root)

    node_id = 0
    build_edges(root)

    #The node's id will match when building the edges since we are traversing the tree in the same
    #way we did when we created the nodes

    f.write("\n}")
    f.close()

    #Using the subprocess module from python to run the following command in windows cmd and generate the .png file
    check_call(['dot','-Tpng','tree.dot','-o','tree_image.png'])

def build_nodes(root):
    
    '''
    Recursive function to traverse the tree and add each of the nodes in the dot file.
    
    Args:
        root (Node): The main root of the tree.
    '''
    global node_id

    node_string = "\n\t" + "node_"+str(node_id) + ' [label = "' + str(root.label) + '"];'
    f.write(node_string)
    for children in root.leaves:
        node_id += 1
        build_nodes(children)

def build_edges(root):

    '''
    Recursive function to to traverse the tree and add each of the edges relations from the nodes in the dot file.
    
    Args:
        root (Node): The main root of the tree.
    '''
    global node_id
    
    parent_id = node_id

    for children in root.leaves:
        node_id += 1
        if children.is_final:
            #If the children is final, the edge connecting to it's parent changes its color to red
            edge_string = "\n\t" + "node_" + str(parent_id) + " -> " + "node_" + str(node_id) +' [color="red"];'
            f.write(edge_string)
        else:
            #If the children is not final, there is no need to change it's color
            edge_string = "\n\t" + "node_" + str(parent_id) + " -> "+ "node_" + str(node_id) +";"
            f.write(edge_string)
        build_edges(children)