from src.utils.logger import Logger

logger = Logger('BinarySearchTreeNodeLogger').get_logger()


class Node:
    def __init__(self, value: int) -> None:
        """
        Creates a new Node to be used within a Binary Search Tree.
        :param value: The value of the node
        """
        logger.info(f'Creating new node with value - {value}')
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None
        logger.info('Created new node successfully')