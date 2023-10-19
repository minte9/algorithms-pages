""" Printer Queue Example
    https://vegibit.com/python-queue-example
"""

from icecream import ic

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item) # Add to the front of the queue (FIFO)

    def dequeue(self):
        return self.items.pop() # Remove from the end of the queue (FIFO)

    def is_empty(self):
        return self.items == []

class Job:
    def __init__(self):
        self.pages = 5

    # Simulate printing (by decrementing the page count)
    def print_page(self):

        ic('Print page', self.pages)

        if self.pages > 0:
            self.pages -= 1

    # Check if the print job is complete
    def check_complete(self):
        if self.pages == 0:
            return True
        return False

class Printer:
    def __init__(self):
        self.current_job = None

    def get_next_job(self, queue):
        try:
            return queue.dequeue()
        except IndexError:
            return "No more jobs to print"

    def process(self, job):
        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            print(f"Printing {job} complete.")
        else:
            print("An error occurred.")

j1 = Job()
j2 = Job()

queue = Queue()
queue.enqueue(j1)
queue.enqueue(j2)

printer = Printer()
job = printer.get_next_job(queue)
printer.process(job)

job = printer.get_next_job(queue)
printer.process(job)

job = printer.get_next_job(queue)
printer.process(job)

if queue.is_empty():
    print("Printing complete.")