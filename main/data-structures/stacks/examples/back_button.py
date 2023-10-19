""" Back button
Example of using stacks for back button in a web browser
"""

from icecream import ic

class Browser:
    def __init__(self):
        self.history = [] # stack (LIFO)
        self.current_page = None
    
    # Simulate navigation
    def navigate(self, url):
        self.current_page = url
        self.history.append(url)
        ic("Navigate to =>", url)

    def back(self):
        if self.history:
            previous_page = self.history.pop() # retrive last (LIFO)
            self.current_page = previous_page
            ic("Back to =>", previous_page)
        else:
            print("No more pages in history")

# Example usage
browser = Browser()

#ic.disable()

print("Navigate:")
browser.navigate("https://www.example.com")
browser.navigate("https://www.example.com/page1")
browser.navigate("https://www.example.com/page2")

print("Current page:", browser.current_page, "\n")

print("Go back:")
browser.back() 
browser.back()   
browser.back()

print("Current page:", browser.current_page, "\n")

print("Go back:")
browser.back()

"""
    Navigate:
    ic| 'Navigate to =>', url: 'https://www.example.com'
    ic| 'Navigate to =>', url: 'https://www.example.com/page1'
    ic| 'Navigate to =>', url: 'https://www.example.com/page2'
    Current page: https://www.example.com/page2 

    Go back:
    ic| 'Back to =>', previous_page: 'https://www.example.com/page2'
    ic| 'Back to =>', previous_page: 'https://www.example.com/page1'
    ic| 'Back to =>', previous_page: 'https://www.example.com'
    Current page: https://www.example.com 

    Go back:
    No more pages in history
"""