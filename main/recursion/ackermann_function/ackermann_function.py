""" Ackermann function
Mostly known of being a highly recursive function.
It doesn't have many practical applications, but 
no discussion about recursion would be complete without it.

It has two arguments (m, n) and two recursive cases.
Base case: when m = 0 is returning n + 1
When n = 0, returns ackerman(m - 1, 1)
When n > 0, returns ackerman(m - 1, ackerman(m, n-1))

ackerman(1, 1) means 3 recursive calls
ackerman(2, 3) means 43 recursive calls
ackerman(3, 5) means 42437 recursive calls
"""

def ackermann(m, n, i=0):
    print(' ' * i, 'ackerman(%s, %s) '% (m, n))

    if m == 0:    
        return n + 1 # Base case
    
    if m > 0 and n == 0:
        return ackermann(m - 1, 
                1, 
                    i + 1)

    if m > 0 and n > 0:
        return ackermann(m - 1, 
                ackermann(m, n-1, i + 1), 
                    i + 1)

x = ackermann(2, 3)
print(x)

"""
 ackerman(2, 3) 
  ackerman(2, 2) 
   ackerman(2, 1) 
    ackerman(2, 0) 
     ackerman(1, 1) 
      ackerman(1, 0) 
       ackerman(0, 1) 
      ackerman(0, 2) 
    ackerman(1, 3) 
     ackerman(1, 2) 
      ackerman(1, 1) 
       ackerman(1, 0) 
        ackerman(0, 1) 
       ackerman(0, 2) 
      ackerman(0, 3) 
     ackerman(0, 4) 
   ackerman(1, 5) 
    ackerman(1, 4) 
     ackerman(1, 3) 
      ackerman(1, 2) 
       ackerman(1, 1) 
        ackerman(1, 0) 
         ackerman(0, 1) 
        ackerman(0, 2) 
       ackerman(0, 3) 
      ackerman(0, 4) 
     ackerman(0, 5) 
    ackerman(0, 6) 
  ackerman(1, 7) 
   ackerman(1, 6) 
    ackerman(1, 5) 
     ackerman(1, 4) 
      ackerman(1, 3) 
       ackerman(1, 2) 
        ackerman(1, 1) 
         ackerman(1, 0) 
          ackerman(0, 1) 
         ackerman(0, 2) 
        ackerman(0, 3) 
       ackerman(0, 4) 
      ackerman(0, 5) 
     ackerman(0, 6) 
    ackerman(0, 7) 
   ackerman(0, 8) 
9
"""