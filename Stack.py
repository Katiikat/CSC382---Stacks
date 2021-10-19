class Stack:
    def __init__(self):
        self.stack = []

    def add(self, value):
        # check if value is already in stack
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    # peek means to look at the last item added
    def peek(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the Stack"
        else:
            return self.stack.pop()


test = Stack()

test.add("The")
test.add("Moon")
test.add("Is")
test.add("Bright")
test.add("Tonight")

print(test.peek())

test.remove() # removes Tonight
print(test.remove()) # removes Bright

test.remove() # removes IS
print(test.remove()) # removes Moon

test.add("Lamp")
print(test.peek())

print(test.remove())


















