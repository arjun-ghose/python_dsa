from node import Node
from src.utils.logger import Logger

logger = Logger('DoublyLinkedListLogger').get_logger()


class DoublyLinkedList:
    def __init__(self, value: int):
        """
        Creates a new Doubly Linked List (DLL) with a single node.
        :param value (int): The value of the initial node.
        """
        logger.info(f'Creating a new Doubly Linked List with a single node with value - {value}')
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length: int = 1
        logger.info('Created a new Doubly Linked List successfully.')

    def print_list(self):
        """Prints all the values stored in the DLL as a list."""
        logger.info('Printing Doubly Linked List as a list')
        temp = self.head
        dll = []
        while temp is not None:
            dll.append(temp.value)
            temp = temp.next
        logger.info(f"Doubly Linked List - {dll}")

    def print_items(self):
        """Prints each item in the DLL on a new line."""
        logger.info('Printing all items of the doubly linked list')
        temp = self.head
        while temp is not None:
            logger.info(f"Doubly Linked List Item - {temp.value}")
            temp = temp.next

    def append(self, value: int) -> bool:
        """
        Adds a new node at the end of the DLL with the new value.
        :param value: The value of the new node.
        :return: True if the value is entered successfully.
        """
        logger.info(f"Appending a new node to the DLL with value - {value}")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        logger.info("Appended the new node successfully.")
        return True

    def pop(self) -> Node | None:
        """
        Deletes the last node in the DLL.
        :return: Returns the last node in the DLL.
        """
        logger.info("Deleting the last node of the DLL.")
        if self.length == 0:
            logger.info("No nodes to delete.")
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        logger.info("Deleted node successfully.")
        return temp

    def prepend(self, value: int) -> bool:
        """
        Adds a new Node at the beginning of the DLL.
        :param value: The value of the new node.
        :return: True if the node is prepended successfully.
        """
        logger.info(f"Prepending a new node to the DLL with value - {value}")
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        logger.info("Prepended value successfully.")
        return True

    def pop_first(self) -> Node | None:
        """
        Deletes and returns the first node of the DLL.
        :return: Node.
        """
        logger.info("Deleting the first node of the DLL")
        if self.length == 0:
            logger.info("No nodes to delete.")
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        logger.info("Deleted the first node successfully.")
        return temp

    def get(self, index: int) -> Node | None:
        """
        Returns the Node at the given index.
        :param index: The index of the required Node.
        :return: Node at the given index.
        """
        logger.info(f"Getting the node at index - {index}")
        if index < 0 or index >= self.length:
            logger.warning("Invalid index.")
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        logger.info(f"Returned node with value - {temp.value}")
        return temp

    def set_value(self, index: int, value: int) -> bool:
        """
        Updates the value of the Node at the given index.
        :param index: The index of the Node to be updated.
        :param value: The new value of the updated Node.
        :return: True if the value was updated successfully.
        """
        logger.info(f"Updating the value of node at index - {index}")
        temp = self.get(index)
        if temp:
            temp.value = value
            logger.info(f"Updated value of node at {index} to {value}")
            return True
        logger.warning(f"No node at index - {index}")
        return False

    def insert(self, index: int, value: int) -> bool:
        """
        Inserts a new node at the given index with the given value.
        :param index: The index of the new Node.
        :param value: The value of the new Node.
        :return: True if the new node was inserted successfully.
        """
        logger.info(f"Inserting a new node with value {value} at index {index}")
        if index < 0 or index > self.length:
            logger.warning("Invalid index.")
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        logger.info("Inserted new node successfully.")
        return True

    def remove(self, index: int) -> Node | None:
        """
        Removes and returns the Node at the given index.
        :param index: The index of the Node to be removed.
        :return: The removed Node, or none if the node doesn't exist.
        """
        logger.info(f"Removing the node at index - {index}")
        if index < 0 or index >= self.length:
            logger.warning("Invalid index.")
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        logger.info("Removed node successfully")
        return temp


## Usage
if __name__ == '__main__':
    # Creating list
    my_dll = DoublyLinkedList(1)

    # Append
    my_dll.append(2)
    my_dll.append(3)
    my_dll.append(4)

    # Print list
    my_dll.print_list()
    my_dll.print_items()

    # Pop
    my_dll.pop()
    my_dll.print_list()

    # Prepend
    my_dll.prepend(0)
    my_dll.print_list()

    # Pop first
    my_dll.pop_first()
    my_dll.print_list()

    # Get
    my_dll.get(2)

    # Set
    my_dll.set_value(2, 6)
    my_dll.print_list()

    # Insert
    my_dll.insert(3, 5)
    my_dll.print_list()

    # Remove
    my_dll.remove(3)
    my_dll.print_list()
