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
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            logger.info(f'Inserted new node with value {value} successfully')
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                logger.warning('Value already exists, cannot insert')
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    logger.info(f'Inserted new node with value {value} successfully')
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    logger.info(f'Inserted new node with value {value} successfully')
                    return True
                temp = temp.right

    def contains(self, value: int) -> bool:
        """
        Checks if a certain value is present in the BST.
        :param value: The value whose presence needs to be checked.
        :return: Returns true if the value is present, false if the value is not.
        """
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                logger.info(f'Value {value} is present in the tree')
                return True
        logger.info(f'Value {value} is not present in the tree')
        return False

    def __r_contains(self, current_node: Node, value: int) -> bool:
        """
        Helper function to check if a certain value is present in the BST using recursion.
        :param current_node: The starting node for the search.
        :param value: The value to be checked against.
        :return: True if the value exists in the tree, false otherwise.
        """
        if current_node is None:
            logger.info(f'Value {value} does not exist in the BST')
            return False
        if value == current_node.value:
            logger.info(f'Value {value} exists in the BST')
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value: int) -> bool:
        """
        Checks if a certain value is present in the BST using recursion.
        :param value: The value whose presence needs to be checked for.
        :return: True if the value exists in the tree, false otherwise.
        """
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node: Node, value: int) -> Node:
        """
        Helper function to insert a node into the tree using recursion.
        :param current_node: The starting node, usually the root.
        :param value: The value that needs to be inserted.
        :return: A node with the value.
        """
        if current_node is None:
            logger.info(f'Inserted new node with value {value} successfully')
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value: int) -> None:
        """
        Inserts a new node in the tree using recursion.
        :param value: The value of the new node.
        :return: None
        """
        if self.root is None:
            self.root = Node(value)
            logger.info(f'Inserted new node with value {value} successfully')
        self.__r_insert(self.root, value)

    def min_value(self, current_node: Node) -> int:
        """
        Returns the value of the smallest node under the current node.
        :param current_node: The starting point for the search of the min value.
        :return: The minimum value.
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node: Node, value: int) -> Node | None:
        """
        Helper method to delete a node from the tree and returns it.
        :param current_node: The starting node, usually the root.
        :param value: The value of the node to be deleted.
        :return: The deleted node, or none if the node does not exist.
        """
        if current_node is None:
            logger.info(f'Deleted node with value {value} successfully')
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                logger.warning(f'Tree does not have a node with value {value}')
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        logger.info(f'Deleted node with value {value} successfully')
        return current_node

    def delete_node(self, value: int) -> Node | None:
        """
        Deletes a node with a given value from the tree.
        :param value: The value of the node that needs to be deleted.
        :return: The deleted node, or none if the node doesn't exist.
        """
        return self.__delete_node(self.root, value)


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

    ## RECURSIVE METHODS
    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    # Recursive contains
    my_tree.r_contains(27)
    my_tree.r_contains(17)

    # Recursive Insert
    my_tree = BinarySearchTree()
    my_tree.r_insert(2)
    my_tree.r_insert(1)
    my_tree.r_insert(3)
    print(f'Root: {my_tree.root.value}')
    print(f'Root -> Left: {my_tree.root.left.value}')
    print(f'Root -> Right: {my_tree.root.right.value}')

    # Delete
    my_tree.delete_node(2)
    print(f'Root: {my_tree.root.value}')
    print(f'Root -> Left: {my_tree.root.left.value}')
    print(f'Root -> Right: {my_tree.root.right}')
