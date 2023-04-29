## Trees
> A tree `data structure` is a structure of nodes.  p72  
Nodes are `connected` by other nodes by edges.  

> Nodes contain `data`.  
Edges represent a `relationship` with another nodes.  

> The starting node of a tree is called a `root`.  
Trees always have exactly `one root`.  

> In trees child nodes must have `one parent` and  
edges that are `not loops`  

## Graphs
> In mathematics and computer science, a `graph` is a  
collection of nodes and edges.  

> A tree is a kind of graph `DAG` (directed acyclic graph).  

> Lists, arrays and strings could be seens as `linear trees`.  
The linear tree `ends` at its one leaf.  

> H -> E -> L -> L -> O  

## Traversing a tree

> We can write `recursive function` to access data in any node   
by starting from the root.   

> The `base case` is the leaf node (no more child).  
This causes the algorithm to `backtrack` to a previous parent.  

> The `argument` to pass to the function is the next node.  
We get `closer` to the base naturally, because the trees are acyclic.  

## Stack overlow

> Trees that are `especially deep` will case a stack overflow.  
Each level deeper into the tree requires `yet another` recursion call. 

### References
> [The Recursive Book of Recursion (source code)](https://github.com/asweigart/the-recursive-book-of-recursion)  
[Invent with Python, Recursion (online book)](https://inventwithpython.com/recursion/)  
[The recursive book of recursion (buy)](https://www.amazon.com/gp/product/B09BKL34VL)