# Python code​​​​​​‌​‌​‌‌‌​‌‌‌‌‌‌​​‌​‌​‌​‌‌​ below
import heapq

# Class needed for solution. Do not edit.
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


def process_tasks(tasks):
    # Create a priority queue
    pq = PriorityQueue()

    # Iterate through the tasks
    for task, priority in tasks:
        # Add each task to the priority queue along with its priority value
        pq.put(task, priority)
    # Use the "accumulator pattern."
    # Start with an "empty bucket" of the right data type (list in this case)
    # and build the solution by filling the bucket within a loop.
    ordered_task_list = []

    # Use a while loop with the exit condition that the priority queue is empty.
    # Within this loop, update result with items got from the priority queue.

    while not pq.is_empty():
        task = pq.get()
        ordered_task_list.append(task)

    return ordered_task_list
