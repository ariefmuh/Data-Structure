class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_items(self):
        for item in self.items:
           print(item, end=' ')

# create a new stack
my_stack = Stack()

# push some items onto the stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# my_stack.print_items()

# print the current size of the stack
print(my_stack.size())  # prints 3

# print the top item on the stack (without removing it)
print(my_stack.peek())  # prints 3

# pop an item from the stack and print it
print(my_stack.pop())  # prints 3

my_stack.print_items()

# print the size of the stack again
print(my_stack.size())  # prints 2

my_stack.print_items()
