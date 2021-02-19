# Parsing-tree
Integrative project made during the computational maths course.


## Functionality
**A program that reads from a file the elements that define a context-free grammar and apply the top-down 
parsing process for strings given by the user.**

The grammar must be defined in a txt file. The file shall be defined as follows:
- The first line indicates the set of non-terminal symbols separated by commas, only one uppercase character.
- The second line indicates the set of terminal symbols separated by commas, only one
lowercase character.
- The third line indicates the start symbol.
- The following lines indicate the productions of the grammar in the following format:
nonTerminalSymbol -> chain terminals or non-terminal symbol

Lambda cannot appear as body of any production. The top-down parsing process
receives a string and an integer. The integer indicates the maximum depth of the parsing
tree. If this depth is exceeded, the process stops indicating that no solution was
found for the string.

The outcome of this process is a png image of the parsing tree.


###### Important
> This program doesn't validate the values in the input file, it assumes that they were built correctly.

## Built with
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![Graphviz Badge](https://img.shields.io/badge/Graphviz-969696?style=flat-square&logoColor=white)
![Dot files Badge](https://img.shields.io/badge/Dot_files-006C66?style=flat-square&logoColor=white)
