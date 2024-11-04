from node import Node
from src.utils.logger import Logger

logger = Logger("StackLogger").get_logger()


class Stack:
    def __init__(self, value: int):
        """
        Creates a new Stack with a single node.
        :param value: The value of the initial node.
        """
        logger.info(f"Creating a new Stack with value of the initial node = {value}")
        new_node: Node = Node(value)
        self.top: Node | None = new_node
        self.height: int = 1
        logger.info('Created new Stack successfully')

    def print_stack_as_list(self) -> None:
        """
        Prints out the node values of the stack as a list.
        :return:
        """
        stack = []
        temp = self.top
        while temp:
            stack.append(temp.value)
            temp = temp.next
        logger.info(f'Stack as List - {stack}')

    def print_stack_items(self) -> None:
        """
        Prints out the node values on new lines.
        :return:
        """
        temp = self.top
        while temp:
            logger.info(f'Node value = {temp.value}')
            temp = temp.next

    def push(self, value: int) -> bool:
        """
        Adds a new node at the top of the stack.
        :param value: The value of the new node.
        :return: Returns true if the new node is pushed successfully.
        """
        logger.info(f'Adding a new node with value = {value}')
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        logger.info("Added new node successfully")
        return True

    def pop(self) -> Node | None:
        """
        Removes the top node in the stack
        :return: Returns the top Node of the stack or None if there are no nodes in the stack.
        """
        logger.info('Popping the top node of the Stack')
        if self.height == 0:
            logger.info('No nodes present in the stack')
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        logger.info('Popped the top element successfully')
        return temp

# Usage
if __name__ == '__main__':
    # Creating new stack
    my_stack = Stack(4)

    # Printing Stack
    my_stack.print_stack_as_list()
    my_stack.print_stack_items()

    # Push
    my_stack.push(7)
    my_stack.push(8)
    my_stack.push(3)
    my_stack.print_stack_as_list()

    # Pop
    my_stack.pop()
    my_stack.print_stack_as_list()