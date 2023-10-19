""" Keyboard Undo
Example of using a queue to implement Undo function
"""

from collections import deque
from icecream import ic

class Keyboard:
    def __init__(self):
        self.queue = deque()
        self.current_text = ""

    # Perform the key press and store it in the history
    def press_key(self, key):
        self.queue.append(self.current_text)
        self.current_text += key

        ic(key)
        ic(self.current_text)

    # Revert to the previous text state
    def undo(self):
        if self.queue:
            previous_text = self.queue.pop() # LIFO
            self.current_text = previous_text
            ic('Undo =', self.current_text)
        else:
            print('Nothing to undo')

# Example usage
keyboard = Keyboard()

print("Start keybord typing:")

keyboard.press_key("H")
keyboard.press_key("e")
keyboard.press_key("l")
keyboard.press_key("l")
keyboard.press_key("o")

print("Start repeatedly undo:")

keyboard.undo()
keyboard.undo()
keyboard.undo()
keyboard.undo()
keyboard.undo()

keyboard.undo()
keyboard.undo()

"""
    Start keybord typing:
    ic| key: 'H'
    ic| self.current_text: 'H'
    ic| key: 'e'
    ic| self.current_text: 'He'
    ic| key: 'l'
    ic| self.current_text: 'Hel'
    ic| key: 'l'
    ic| self.current_text: 'Hell'
    ic| key: 'o'
    ic| self.current_text: 'Hello'

    Start repeatedly undo:
    ic| 'Undo =', self.current_text: 'Hell'
    ic| 'Undo =', self.current_text: 'Hel'
    ic| 'Undo =', self.current_text: 'He'
    ic| 'Undo =', self.current_text: 'H'
    ic| 'Undo =', self.current_text: ''

    Nothing to undo
    Nothing to undo
"""