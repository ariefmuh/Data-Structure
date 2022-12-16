class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_items(self):
        for item in self.items:
           print(item, end=' ')


# create a new queue
my_queue = Queue()

# enqueue some items onto the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# print the current size of the queue
print(my_queue.size())  # prints 3

# dequeue an item from the queue and print it
print(my_queue.dequeue())  # prints 1

# print the size of the queue again
print(my_queue.size())  # prints 2