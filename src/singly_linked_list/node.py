from src.utils.logger import Logger

logger = Logger("SinglyLinkedListNodeLogger").get_logger()


class Node:
    def __init__(self, value) -> None:
        """
        Represents a single Node of a Singly Linked List.
        :param value: The initial value assigned to the Node.
        """
        logger.info(f"Creating new node with value: {value}")
        self.value = value
        self.next: Node | None = None
        logger.info("Created new node successfully.")
