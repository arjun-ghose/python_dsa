from node import Node
from src.utils.logger import Logger

logger = Logger("QueueLogger").get_logger()


class Queue:
    def __init__(self, value: int) -> None:
        """
        Creates a new Queue with an initial node.
        :param value: The value of the initial node.
        """
        logger.info(f'Creating a new Queue with initial node value = {value}')
        new_node = Node(value)
        self.first: Node | None = new_node
        self.last: Node | None = new_node
        self.length: int = 1
        logger.info('Created new Queue successfully.')

    def print_queue(self) -> None:
        """
        Prints all the values of the nodes in the Queue as a list.
        :return: None
        """
        queue = []
        temp = self.first
        while temp:
            queue.append(temp.value)
            temp = temp.next
        logger.info(f'Queue = {queue}')

    def enqueue(self, value: int) -> bool:
        """
        Adds a new node at the end of the queue.
        :param value: The value of the new node.
        :return: True if the new node is added to the queue successfully.
        """
        logger.info(f'Enqueueing new node with value - {value}')
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        logger.info('Enqueued new node successfully')
        return True

    def dequeue(self) -> Node | None:
        """
        Removes the first node in the queue.
        :return: The removed node.
        """
        logger.info('Dequeueing first node in queue')
        if self.length == 0:
            logger.info('No nodes in the queue')
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        logger.info('Dequeued first node successfully')
        return temp

# Usage
if __name__ == '__main__':
    # Creating new queue
    my_queue = Queue(4)

    # Printing queue
    my_queue.print_queue()

    # Enqueue
    my_queue.enqueue(5)
    my_queue.enqueue(6)
    my_queue.print_queue()

    # Deqeueue
    my_queue.dequeue()
    my_queue.print_queue()