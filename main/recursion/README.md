# Algorithms Recursion

- [Call stacks](#call-stacks) 
- [Base case](#base-case) 
- [Iterative approach](#iterative-approach) 
- [Exponents](#exponents) 
- [Tail head](#head-tail) 
- [Palindrome](#palindrome)
- [Tower of hanoi](#tower-of-hanoi)  
- [Flood fill](#flood-fill)  
- [Ackermann function](#ackermann-function)  



## Call Stacks

### Line remember
  pp05
The programs remembers which `line of code` called the function.

#-- line_remembering.py --#

### LIFO
  pp06
To really `understand` recursion, you must first understand stacks.

#-- lifo_lists.py --#

### Frame objects
  pp09
The program's call stack is a `stack of frame` objects.

#-- frame_objects.py --#

### Stack overflow
  pp13
The limit of stack size is `1000` function calls in Python.

#-- stack_overflow.py --#




## Base case
  pp13
To avoid a crash, there must be a base case.

#-- base_case.py ---#

### Recursive case
  pp14
Reaching the base case doesn't means the end of program. 

#-- recursive_case.py ---#




## Iterative approach

### Factorial
  pp22
For calculating factorials the iterative approach is better.

#-- factorial.py --#

### Fibonacci 
  pp25
The recursive approach will take f(100) million years to complete.

#-- fibonacci_sequence.py --#




## Exponents
  pp34
Exponents are calculated by multiplying a number by itself.

#-- calculating_exponents.py --#

### Insights
  pp36
Iterative function based on power rule from recursive approach.

#-- recursive_insights.py --#


----------------------------------------------------------------------


## Head Tail

### Sum Numbers
   pp46
We add the head to the sum of tail array.

#-- sum_numbers.py --#

### Reverse Strings
  pp49
To reverse a string we need to place the head behind the tail.

#-- reverse_strings --#


----------------------------------------------------------------------


## Palindrome
  pp52
Word or phrase spelled the same forward or backword.

#-- palindrome.py --#


----------------------------------------------------------------------


## Tower of Hanoi
  pp54
A puzzle involving a tower of stacked disks.

#-- tower_of_hanoi.py --#

### Interactive 

Solve the puzzle yourself, in interactive mode.

#-- tower_of_hanoy2_play.py


----------------------------------------------------------------------


## Flood Fill
  pp60
Begins on one pixel and spreads until it meets a non-white pixel.

#-- flood_fill.py --#


----------------------------------------------------------------------



## Ackermann Function
  pp64
Known of being an example of highly recursive function.

#-- ackermann_function --#