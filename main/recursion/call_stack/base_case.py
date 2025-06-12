""" When using recursion, to avoid a crash, there always must be a base case. 
The function stop calling itself and just returns.

The code in a recursive call can be split in two parts, 
before the recursive call and after recursive call.
"""

def show_frame(i=0):
  sep = i * " "

  if i == 3:
    print(f"{sep}-- Base case --")
    return

  print(f"{sep}Frame {i} / Recursion {i}")

  # Recursion
  show_frame(i+1)

  print(f"{sep}Frame {i} / Return")
  return

show_frame()

"""
  Frame 0 / Recursion 0
    Frame 1 / Recursion 1
      Frame 2 / Recursion 2
      -- Base case --
      Frame 2 / Return
    Frame 1 / Return
  Frame 0 / Return
"""