# RECURSION that RETURNS a value
# ------------------------------
# Problem: 
#       Sum all numbers from 1 to n
# Result: 
#       sum_to(4) = 1 + 2 + 3 + 4 = 10
#
# THE 5-STEP MENTAL CHECKLIST (APPLIED)
# -------------------------------------
# 1) What is the smallest posible input?
#       - n = 1
#
# 2) What should happen at that smallest input?
#       - return 1
#       - the sum of numbers up to 1 is 1
# 
# 3) How does the problem get smaller?
#       - Insteed of summing up to n, sum up to (n - 1)
# 
# 4) What stays the same?
#       - The idea: "sum numbers from 1 to n"
#       - The function logic does NOT change
# 
# 5) What does the function return?
#       - A number (the sum)
#       - Every recursive call MUST return a number
#
# TRACE THE EXECUTION (DO NOT SKIP)
# ---------------------------------
# Write this on paper:
#
# sum_to(4)
#    = 4 + sum(3)
#    = 4 + (3 + sum(2))
#    = 4 + (3 + (2 + sum(1)))
#    = 4 + (3 + (2 + 1))
#    = 10
# --------------------------------

def sum_to(n):
    if n == 1:                  # Base case
        return 1
    
    print(n)                    # 4, 3, 2
    return n + sum_to(n-1)      # Smaller problem

result = sum_to(4)
print(result)

# ---------------
# 4
# 3
# 2
# 10