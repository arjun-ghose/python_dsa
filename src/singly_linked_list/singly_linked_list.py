from wsgiref.validate import validator

from node import Node
from src.utils.logger import Logger

logger = Logger("SinglyLinkedListLogger").get_logger()


class SinglyLinkedList:
    def __init__(self, value) -> None:
        """
        Creates a new Singly Linked List (SLL) with one Node.
        :param value: The value to be assigned to the initial Node
        """
        logger.info(f"Creating a new Singly Linked List with a single node with value - {value}")
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length: int = 1
        logger.info("Created Singly Linked List successfully.")

    def print_list(self) -> None:
        """
        Prints all the elements of the SLL as a list.
        :return: None
        """
        logger.info("Printing SLL as a list")
        temp= self.head
        sll = []
        while temp is not None:
            sll.append(temp.value)
            temp = temp.next
        logger.info(f"Singly Linked List - {sll}")

    def print_items(self) -> None:
        """Prints all the items of the SLL on a new line"""
        logger.info("Printing all items of the SLL")
        temp = self.head
        while temp is not None:
            logger.info(f"SLL Item - {temp.value}")
            temp = temp.next

    def append(self, value) -> bool:
        """
        Creates new Node and adds Node to the end.
        :param value: The value to be assigned to the new Node
        :return: bool
        """
        logger.info(f"Appending a new node with value - {value}.")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        logger.info("Appended new node successfully.")
        return True

    def pop(self) -> Node | None:
        """
        Deletes the last Node in the Linked List and returns its value.
        :return: The deleted node
        """
        logger.info("Deleting last node from the SLL")
        if self.length == 0:
            logger.warning("No nodes to delete.")
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        logger.info(f"Deleted last node with value - {temp.value}")
        return temp

    def prepend(self, value) -> bool:
        """
        Creates a new Node and inserts it at the beginning of the Linked List.
        :param value: The value assigned to the new Node.
        :return:
        """
        logger.info(f'Prepending a new node with value - {value}')
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        logger.info('Prepended new node successfully.')
        return True

    def pop_first(self) -> Node | None:
        """
        Deletes the first Node in the list and returns it.
        :return:
        """
        logger.info('Deleting the first node from the SLL')
        if self.length == 0:
            logger.warning('No nodes to delete.')
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        logger.info(f'Deleted node with value - {temp.value}')
        return temp

    def get(self, index: int) -> Node | None:
        """
        Returns the Node at the specified index.
        :param index: The position of the Node you want returned.
        :return:
        """
        logger.info(f'Getting the value of node at index - {index}')
        if index < 0 or index >= self.length:
            logger.warning('Invalid index')
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        logger.info(f'Returned node with value = {temp.value}')
        return temp

    def set_value(self, index: int, value) -> bool:
        """
        Updates the value of a Node to the specified value at the specified index.
        :param index: The position of the Node whose value you want to update.
        :param value: The new value that needs to be set.
        :return:
        """
        logger.info(f'Updating the value of node at index {index} to {value}')
        temp = self.get(index)
        if temp:
            temp.value = value
            logger.info('Updated value successfully')
            return True
        logger.warning('Invalid index')
        return False

    def insert(self, index: int, value) -> bool:
        """
        Creates a new Node and inserts it at the specified index.
        :param index: The position you want to insert the new Node.
        :param value: The value of the new Node.
        :return:
        """
        logger.info(f'Inserting new node with value {value} at index {index}')
        if index < 0 or index > self.length:
            logger.warning('Invalid index')
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        logger.info('Inserted new node successfully')
        return True

    def remove(self, index: int) -> Node | None:
        """
        Removes a Node from the Linked List at the specified index and returns it.
        :param index: The position of the Node you want to remove from the Linked List.
        :return:
        """
        logger.info(f'Removing node at index - {index}')
        if index < 0 or index > self.length:
            logger.warning('Invalid index')
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        logger.info('Removed node successfully')
        return temp

    def reverse(self) -> None:
        """
        Reverses the Linked List.
        """
        logger.info('Reversing the SLL')
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        logger.info('Reversed the SLL successfully')
        self.print_list()


## Usage
if __name__ == '__main__':
    # Creating list
    my_sll = SinglyLinkedList(1)

    # Append
    my_sll.append(2)
    my_sll.append(3)
    my_sll.append(4)

    # Print list
    my_sll.print_list()
    my_sll.print_items()

    # Pop
    my_sll.pop()
    my_sll.print_list()

    # Prepend
    my_sll.prepend(0)
    my_sll.print_list()

    # Pop first
    my_sll.pop_first()
    my_sll.print_list()

    # Get
    my_sll.get(2)

    # Set
    my_sll.set_value(2, 6)
    my_sll.print_list()

    # Insert
    my_sll.insert(3, 5)
    my_sll.print_list()

    # Remove
    my_sll.remove(3)
    my_sll.print_list()

    # Reverse
    my_sll.reverse()
