## Algorithms - Recursion

- [Call stacks](#call-stacks) 
- [Base case](#base-case) 
- [Iterative approach](#iterative-approach) 
- [Exponents](#exponents)
- [Head tail](#head-tail) 
- [Middle](#middle)
- [Tower of hanoi](#tower-of-hanoi)  
- [Flood fill](#flood-fill) 
- [Tree traversal](#tree-traversal)  
- [Maze solve](#maze-solve)  
- [Binary search](#binary-search)
- [Quicksort](#quicksort)

#

## Call Stacks
Programming languages remember `which line` called the function.    [p05](./01_call_stacks/line_remembering.py)   
To really understand recursion, you must first `understand stacks`  [p06](./01_call_stacks/lifo_lists.py)  
The program's call stack is a stack of `frame objects`              [p09](./01_call_stacks/frame_objects.py)  
The limit of stack size is `1000 function calls` in Python.         [p13](./01_call_stacks/stack_overflow.py)  

### Base case 
To avoid `a crash` there must be a base case.                       [p14](./02_base_case/base_case.py)  
Reaching the base case `doesn't means` the end of program.          [p15](./02_base_case/before_after.py)  

#

## Iterative approach
For calculating `factorials` the iterative approach is better.      [p22](./03_iterative_approach/factorial_number.py)  
The recursive approach will take `fibonacci(100)` million years.    [p25](./03_iterative_approach/fibonacci_sequence.py)  

### Exponents
Exponents are calculated by `multiplying` a number by itself.       [p34](./04_exponents/calculating_exponents.py)  
Iterative function based on `power rule` from recursive approach.   [p36](./04_exponents/recursive_insights.py)   

#

## Head Tail
To sum numbers we `add the head` to the sum of tail array.          [p46](./05_head_tail/sum_numbers.py)   
To reverse a string we `place the head behind` the tail.            [p49](./05_head_tail/reverse_strings.py)   

### Middle
A palindrome is a word `spelled the same` forward or backward.      [p52](./06_palindrome/palindrome.py)  

### Tower of Hanoi
A puzzle involving a tower of `stacked disks`                       [p54](./07_tower_of_hanoi/tower_of_hanoi.py)   
Solve the puzzle yourself, in `interactive` mode.                   [p54](./07_tower_of_hanoi/tower_of_hanoi2_play.py)   

## Flood Fill
Begins on one pixel and `spreads` until it meets a non-white.       [p60](./08_flood_fill/flood_fill.py)  


## Tree Traversal
We can write code to `access any node` by starting from root node.  [p73](./09_tree_traversal/tree_traversal.py)  

### Maze Solve
A perfect maze has exactly `one path` from start to exit.           [p83](./10_maze_solve/maze_solve.py)  

#

## Divide and conquer

Binary search we determe `which half` of the list the item is in.   [p93](./11_divide_conquer/binary_search.py)
Quicksort uses a divide-concuer technique called `partitioning`     [p96](./11_divide_conquer/quicksort.py)


##


### References

[The Recursive Book of Recursion (source code)](https://github.com/asweigart/the-recursive-book-of-recursion)  
[Invent with Python, Recursion (online book)](https://inventwithpython.com/recursion/)  

[![The recursive book of recursion](https://www.minte9.com/lib/images/references/book_recursion.png)](https://www.amazon.com/gp/product/B09BKL34VL)
