# QUEUES - CONSTRAINS
# -------------------
# Concept:
#   - A queue is a collection with restricted access (just like a stack).
#   - You can only add items to the BACK
#   - You can only remove items from the FRONT
#   - Very fast O(1) operations
# 
# This rule is called FIFO:
#   - First In, First Out
# 
# Think of:
#   - A line at a movie theater
#   - Print jobs
#
# Python provides a proper queue structure in its standard library.
#
# PRINT QUEUE USING deque
# -----------------------

from collections import deque

# Initialize and empty queue
print_queue = deque()

# Documents arrive
print_queue.append("report.pdf")
print_queue.append("invoice.docx")
print_queue.append("photo.png")

print("Queue:", print_queue)
# --------------------------------------------------------
# Queue: deque(['report.pdf', 'invoice.docx', 'photo.png'])

# Printer prints the next document
next_job = print_queue.popleft()

print(next_job)
print("Queue:", print_queue)
# --------------------------
# report.pdf
# Queue: deque(['invoice.docx', 'photo.png'])
