""" Printer Queue Example
    https://vegibit.com/python-queue-example
"""

from icecream import ic

class Queue:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def popleft(self):
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

printer = Printer()
jobs = Queue()

j1 = Job()
jobs.enqueue(j1)

j2 = Job()
jobs.enqueue(j2)

while jobs.is_empty() == False:
    current_job = printer.get_next_job(jobs)
    printer.process(current_job)

print("Printing complete.")