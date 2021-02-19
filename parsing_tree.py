#Authors:
#RichieSjt https://github.com/RichieSjt
#EduardoHJ https://github.com/EduardoHerreraJ

import re
from Node import Node
from cmd_tree import print_tree

def final_path(node):
    try:        
        node.is_final = True
        final_path(node.parent)
    except AttributeError:
        #Root node has None set as its paren, so when trying to
        #access its is_final property the NoneType raises an AttributeError.
        pass

def generate_parsing_tree(file_name, word, max_depth):
    '''
    The main tree processing is made in this function.

    Args:
        file_name (str): The name of the file to open, must be in the same folder.
        word (str): The word that we are going to process to determine if it's accepted or rejected by the grammar.
        max_depth (int): The maximum number of levels that should be generated, 
            the tree will keep generating all of its levels unless it finds the above word.
    
    Returns:
        root: The root of the tree with all of the corresponding leaves.
    '''
    file = open(file_name, "r")

    productions = []

    for idx, line in enumerate(file):
        #- The first line indicates the set of non terminal states separated by commas
        if idx == 0: non_terminal_symbols = line.rstrip('\n').split(",")
        #The second line indicates the terminal symbols separated by commas
        elif idx == 1: terminal_symbols = line.rstrip('\n').split(",")
        #The third line indicates the start symbol
        elif idx == 2: start_symbol = line.rstrip('\n')
        #The following lines indicate the productions of the grammar
        else: productions.append(re.split('->', line.rstrip('\n')))

    queue = []
    accepted = False

    #Creating the start symbol as a node and enqueueing it
    root = Node(start_symbol, 0, [], None, False)
    queue.append(root)

    while queue:
        #We pop the first node from the queue to analyse it as a parent
        current_node = queue.pop(0)
        current_depth = current_node.depth

        #If the depth of the children to analyse is less than the established depth we continue
        if current_depth + 1 <= max_depth:
            #Iterating over each of the characters in the node's label
            for idx, char in enumerate(current_node.label):
                #An uppercase represents a non terminal symbol
                if char.isupper():
                    for production in productions:
                        #We search for the production associated to the non terminal symbol
                        if char == production[0]:
                            #If we find it, we create a child node, add it to the queue and add it to the parent's leave list
                            new_production = current_node.label[:idx] + production[1] + current_node.label[idx+1:]
                            temp_leave = Node(new_production, current_depth+1, [], current_node, False)
                            queue.append(temp_leave)
                            current_node.leaves.append(temp_leave)

                            if new_production == word:
                                final_path(temp_leave)
                                accepted = True
                                break
                    break
        
        if accepted:
            #If the required string is found we stop
            queue.clear()
    
    #print_tree(root)
    
    print("The string is", "accepted" if accepted else "rejected")

    return root