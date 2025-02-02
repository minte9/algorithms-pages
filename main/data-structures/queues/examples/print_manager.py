""" Printer Manager 
Example of using queue for printing
https://vegibit.com/python-queue-example
"""

import random

class Queue:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def popleft(self):
        curr = self.items[0]
        self.items = self.items[1:]
        return curr

    def is_empty(self):
        return self.items == []

class Document:
    def __init__(self, title):
        self.title = title
        self.queue = Queue() # Look Here

        # Add pages to queue
        self.add_pages() 

    def add_pages(self):
        n = random.randint(1, 5)

        # Simulate pages reading
        for k in range(n):
            self.queue.append(k+1)

    def print_pages(self):
        print('Print document =', self.title)
        
        while not self.queue.is_empty():
            page = self.queue.popleft()

            # Simulate printing
            print('Print page', page) 

class PrintManager:
    def __init__(self):
        self.queue = Queue() # Look Here

    def add_job(self, document):
        self.queue.append(document)

    def run(self):
        while not self.queue.is_empty():
            document = self.queue.popleft()
            document.print_pages()

pm = PrintManager()

pm.add_job(Document("First"))
pm.add_job(Document("Second"))
pm.add_job(Document("Third"))

pm.run()

"""
    Print document = First
    Print page 1
    Print page 2
    Print document = Second
    Print page 1
    Print document = Third
    Print page 1
    Print page 2
    Print page 3
    Print page 4
    Print page 5
"""