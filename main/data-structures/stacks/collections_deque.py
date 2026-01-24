# COLLECTIONS - DEQUE
# -------------------
# Features:
#   - Similar performance as custom stack implementation.
#   - Better for queues
#   - Also used as stack sometimes
#
# No custom class needed most of the time.
# 
# ----------------------------
# BROWSER HISTORY STACK (deque)
# -----------------------------


from collections import deque

# Max number of pages to remember
MAX_HISTORY = 5

# Stack for browser history
history = deque(maxlen=MAX_HISTORY)

# User visits pages
history.append("google.com")
history.append("openai.com")
history.append("gitub.com")
history.append("python.org")
history.append("minte9.com")

print("History:", list(history))

# Visit one more page (oldest is removed automatically) - Look Here
history.append("stackoverflow.com")

print("History:", list(history))

# User click BACK
last_page = history.pop()

print("Back to:", last_page)
print("History:", list(history))

# ------------------------------
# History: ['google.com', 'openai.com', 'gitub.com', 'python.org', 'minte9.com']
# History: ['openai.com', 'gitub.com', 'python.org', 'minte9.com', 'stackoverflow.com']
# Back to: stackoverflow.com
# History: ['openai.com', 'gitub.com', 'python.org', 'minte9.com']