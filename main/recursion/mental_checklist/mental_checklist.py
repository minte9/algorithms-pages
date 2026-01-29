# RECURSION - MENTAL CHECKLIST
# ----------------------------
# Recursion is hard for almost everyone at first.
# It requires a different way of thinking than loops. 
# When you see a recursion problem, always answer these questions:
#
# MEMORIZE THIS:
# --------------------------------------
# 1) What is the smallest posible input?
#       -> Base case
#
# 2) What should happen at that smallest input?
#       -> Return value
# 
# 3) How does the problem get smaller?
#       -> Recursive step
# 
# 4) What stays the same?
#       -> Structure
# 
# 5) What does the function return?
#       -> Never forget this
#
# KEY IDEA:
# ----------------------------------------
# Recursion is just stacked function calls.
# Nothing magical.
#
# countdown(3)
#   print(3)
#   countdown(2)
#     print(2)
#     countdown(2)
#       print(1)
#       countdown(1)
#         return
#
# TRACE ON PAPER
# -------------------------------
# Always trace recursion on paper.
#
# countdown(3)
# countdown(2)
# countdown(1)
# countdown(0)
# --------------------------------

def countdown(n):
    if n == 0:  # Base case
        return
    
    print(n)
    countdown(n-1)  # Smaller problem

countdown(3)

# ----------
# 3
# 2
# 1