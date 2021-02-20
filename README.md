# Parsing-tree
Integrative project carried out for the computational mathematics course.


## Functionality
**A program that reads from a file the elements that define a context-free grammar and applies the top-down 
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

## Dependencies
The functionality of this project relies on the graphviz visualization software to compile the generated dot file into a png image file.

To install graphviz on windows follow the instructions here: [Graphviz windows installation](https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224).

Remember to add the bin folder path from the Graphviz installation ```(C:\Program Files\Graphviz 2.44.1\bin)``` to the 
system environment variables and restart your pc.


#### Important notes
> This program is built to work on Windows OS.
> 
> This program doesn't validate the values in the input file, it assumes that they were built correctly.

## Built with
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![Graphviz Badge](https://img.shields.io/badge/Graphviz-969696?style=flat-square&logoColor=white)
![DOT graph description language Badge](https://img.shields.io/badge/DOT_graph_files-006C66?style=flat-square&logoColor=white)
