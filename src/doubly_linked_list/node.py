from src.utils.logger import Logger

logger = Logger('DoublyLinkedListNodeLogger').get_logger()


class Node:
    def __init__(self, value: int):
        """
        Represents a single node of a Doubly Linked List.
        :param value (int): The value to be stored in the Node.
        """
        logger.info(f'Creating a new node with value: {value}.')
        self.value: int = value
        self.next: Node | None = None
        self.prev: Node | None = None
        logger.info('Created new node successfully.')
