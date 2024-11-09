from src.utils.logger import Logger
from node import Node

logger = Logger('BinarySearchTreeLogger').get_logger()


class BinarySearchTree:
    def __init__(self) -> None:
        """
        Creates an empty Binary Search Tree (BST) with an empty root Node.
        """
        self.root: Node | None = None
        logger.info('Created empty binary search tree successfully')

    def insert(self, value: int) -> bool:
        """
        Creates and inserts a new node in the BST with the specified value.
        :param value: The value of the new node.
        :return: Returns true if the new node is inserted successfully, false otherwise.
        """
        logger.info(f'Inserting new node with value - {value}')
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            logger.info('Inserted new node successfully')
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                logger.warning('Value already exists, cannot insert')
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    logger.info('Inserted new node successfully')
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    logger.info('Inserted new node successfully')
                    return True
                temp = temp.right

    def contains(self, value: int) -> bool:
        """
        Checks if a certain value is present in the BST.
        :param value: The value whose presence needs to be checked.
        :return: Returns true if the value is present, false if the value is not.
        """
        logger.info(f'Checking if {value} is present in the tree')
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                logger.info('Value present')
                return True
        logger.info('Value not present')
        return False

# Usage
if __name__ == '__main__':
    # Create empty BST
    my_tree = BinarySearchTree()
    print(my_tree.root)

    # Inserting values
    my_tree.insert(2)
    my_tree.insert(1)
    my_tree.insert(3)

    print(my_tree.root.value)
    print(my_tree.root.left.value)
    print(my_tree.root.right.value)

    # Contains
    my_tree.contains(1)
    my_tree.contains(2)
    my_tree.contains(3)
    my_tree.contains(4)
