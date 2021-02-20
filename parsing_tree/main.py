# Authors:
# RichieSjt https://github.com/RichieSjt
# EduardoHerreraJ https://github.com/EduardoHerreraJ

from parsing_tree import generate_parsing_tree
from visual_tree import visualize_tree

file_name = input("Enter the file name: ")
word = input("Enter the string to be validated: ")
max_depth = int(input("Max depth: "))

root = generate_parsing_tree(file_name, word, max_depth)
visualize_tree(root)