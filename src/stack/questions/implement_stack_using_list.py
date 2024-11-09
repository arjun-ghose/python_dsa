"""
Q1. Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.

Q2. Add a method to push a value onto the Stack implementation that we began in the last Coding Exercise.

Q3. Add a method to pop a value from the Stack implementation that we began in the last two Coding Exercises.
"""

class Stack:
    def __init__(self) -> None:
        self.stack_list = []

    def push(self, value: int) -> bool:
        self.stack_list.append(value)
        return True

    def pop(self) -> int | None:
        if self.stack_list:
            temp = self.stack_list.pop()
            return temp
        return None
