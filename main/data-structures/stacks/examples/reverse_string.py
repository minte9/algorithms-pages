""" Reverse string
Example of using a stack to reverse a string
"""

class StringReverser:
    def __init__(self, str):
        self.stack = []

        for char in str:
            self.stack.append(char)

    def reverse_string(self):
        rs = ""
        while self.stack:
            rs += self.stack.pop()
        return rs

# Example usage
R = StringReverser("Hello World!")
rs = R.reverse_string()

print("Reversed string:", rs)

"""
    Reversed string: !dlroW olleH
"""