from src.utils.logger import Logger

logger = Logger("QueueNodeLogger").get_logger()


class Node:
    def __init__(self, value: int):
        """
        Creates a new Node to be used within a Queue.
        :param value: The value of the node.
        """
        logger.info(f'Creating a new node with value = {value}')
        self.value = value
        self.next = None
        logger.info('Created new node successfully')