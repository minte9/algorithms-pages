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

<br/>


## Call Stacks

### Line remember
 
The programs `remembers` which line of code called the function. `p05`

https://github.com/minte9/algorithms-pages/blob/5b306af38b361bf535fcf646fd50b4f4736a71f2/main/recursion/call_stacks/line_remembering.py#L1-L24

### LIFO

To really `understand` recursion, you must first understand stacks. `p06`

https://github.com/minte9/algorithms-pages/blob/9b4a81c77a96ec597c9fc27aaa5f3622c5c9873f/main/recursion/call_stacks/lifo_lists.py#L1-L27

### Frame objects

The program's call stack is a `stack of frame` objects. `p09`

https://github.com/minte9/algorithms-pages/blob/aa1930181f6afffe978c80af763cdfcf4eaa2fb1/main/recursion/call_stacks/frame_objects.py#L1-L42

### Stack overflow
 
The limit of stack size is `1000` function calls in Python. `p13`

https://github.com/minte9/algorithms-pages/blob/aa1930181f6afffe978c80af763cdfcf4eaa2fb1/main/recursion/call_stacks/stack_overflow.py#L1-L15

<br/>



## Base case
  pp13
To avoid a crash, there must be a base case.

#-- base_case.py ---#

### Recursive case
  pp14
Reaching the base case doesn't means the end of program. 

#-- recursive_case.py ---#

<br/>



## Iterative approach

### Factorial
  pp22
For calculating factorials the iterative approach is better.

#-- factorial.py --#

### Fibonacci 
  pp25
The recursive approach will take f(100) million years to complete.

#-- fibonacci_sequence.py --#

<br/>



## Exponents
  pp34
Exponents are calculated by multiplying a number by itself.

#-- calculating_exponents.py --#

### Insights
  pp36
Iterative function based on power rule from recursive approach.

#-- recursive_insights.py --#

<br/>



## Head Tail

### Sum Numbers
   pp46
We add the head to the sum of tail array.

#-- sum_numbers.py --#

### Reverse Strings
  pp49
To reverse a string we need to place the head behind the tail.

#-- reverse_strings --#

<br/>



## Palindrome
  pp52
Word or phrase spelled the same forward or backword.

#-- palindrome.py --#

<br/>



## Tower of Hanoi
  pp54
A puzzle involving a tower of stacked disks.

#-- tower_of_hanoi.py --#

### Interactive 

Solve the puzzle yourself, in interactive mode.

#-- tower_of_hanoy2_play.py --#

<br/>



## Flood Fill
  pp60
Begins on one pixel and spreads until it meets a non-white pixel.

#-- flood_fill.py --#

<br/>



## Ackermann Function
  pp64
Known of being an example of highly recursive function.

#-- ackermann_function --#

<br/>
