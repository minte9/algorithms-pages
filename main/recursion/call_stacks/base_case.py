""" Base case 
To avoid a crash, there must be a base case, 
where function stop calling itself and just returns.

The code in a recursive call can be split in two parts, 
before the recursive call and after recursive call.
"""

def show_frame(i=1):
    print('Frame', i)

    if i == 3:
        print(i * " ", 'Base case')
        return

    print(i * " ",'Recursive case', i)
    show_frame(i+1)

    print(i * " ",'Recursive return', i)
    return

show_frame()

"""

Frame 1
  Recursive case 1
Frame 2
   Recursive case 2
Frame 3
    Base case
   Recursive return 2
  Recursive return 1

"""