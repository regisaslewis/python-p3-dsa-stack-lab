class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        for n in items:
            if self.full() == False:
                self.items.append(n)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.full():
            return None
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        return self.items[- 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if target in self.items:
            return (self.size() - self.items.index(target)) - 1
        return -1

# test = Stack([3, 4], 3)
# print(test.full())
# test.push(0)
# print(test.full())
# print(test.items)
# test.push(3)
# print(test.full())
# print(test.items)
# print(test.peek())
# print(test.search(3))
# print(test.search(0))
# print(test.search(5))
