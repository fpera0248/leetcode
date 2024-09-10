class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(0)  # Remove and return the first element (FIFO)
        return -1  # Return a default value if the queue is empty

    def peek(self) -> int:
        if not self.empty():
            return self.stack[0]  # Return the first element without removing it
        return -1  # Return a default value if the queue is empty

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()