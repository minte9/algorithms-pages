## Recursion

### Call Stacks  
> Programming languages remember `which line` called the function.  p05  
To really understand recursion, you must first `understand stacks`  p06  
The program's call stack is a stack of `frame objects`              p09  
The limit of stack size is `1000 function calls` in Python.         p13  
To avoid `a crash` there must be a base case.                       p14  
Reaching the base case `doesn't means` the end of program.          p15  

### Recursion vs Iteration  
> For calculating `factorials` the iterative approach is better.    p22  
The recursive approach will take `fibonacci(100)` million years.    p25  

### Exponents  
> Exponents are calculated by `multiplying` a number by itself.     p34  
Iterative function based on `power rule` from recursive approach.   p36   

### Memoization
> Memoization is a technique of `remembering` the return values.    p151  
Memoize means `to store` (the result of computed expression).

### Sum numbers    
> To sum numbers we `add the head` to the sum of tail array. p46   

### Reverse strings   
> To reverse a string we `place the head behind` the tail. p49  

### Palindrome    
> A palindrome is a word `spelled the same` forward or backward. p52  

### Sets
> A set is a collection of `unique objects` {A,B,C}. p124  
Order `doesn't matter` for a set, {A,B,C} is the same as {B,A,C}  
A set like {A,B,C,A} has repeate A and so is `not a set`.  

### Permutations
> A permutation of a set is a `specific ordering` of all elements. p127  
For example {A,B,C} has `six` permutations.  
ABC ACB BAC BCA CAB CBA  

### Combinations
> A combination is a `selection of elements` from a set. p134  
We say a `k-combination` is a subset of k elements for a set.  
The 1-combinations of {A,B,C} are: {A}, {B}, {C}  
The 2-combinations of {A,B,C} are: {A,B}, {A,C}, {B,C}  
The 3-combinarions of {A,B,C} are: {A,B,C}  
>
> The term `n choose k` refers to the number of possible combinations.  
For example 4 choose 2 is `6 combinations` without repetition.   
{A,B,C,D} -> {A,B} {A,C} {A,D} {B,C} {B,D} {C,D}  
> 
> The `formula` for calculating n choose k is:  
C(n,k) = (n!) / (k! x (n-k)!)  


### References
> [The Recursive Book of Recursion (source code)](https://github.com/asweigart/the-recursive-book-of-recursion)  
[Invent with Python, Recursion (online book)](https://inventwithpython.com/recursion/)  
[The recursive book of recursion (buy)](https://www.amazon.com/gp/product/B09BKL34VL)
