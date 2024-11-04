from src.utils.logger import Logger

logger = Logger('HashTableLogger').get_logger()


class HashTable:
    def __init__(self, size: int = 7) -> None:
        """
        Creates an empty Hash Table with the specified size.
        :param size: The number of available addresses in the hash table.
        """
        self.data_map: list = [None] * size
        logger.info(f'Created Hash Table of size {size} successfully')

    def __hash(self, key: str) -> int:
        """
        The Hash function used to convert a key to an address in the Hash Table.
        :param key: The key for which you want to create an address.
        :return: Int which is an address in the Hash Table.
        """
        my_hash: int = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self) -> None:
        """
        Prints all items in the Hash Table.
        :return: None
        """
        for i, val in enumerate(self.data_map):
            logger.info(f'{i} : {val}')

    def set_item(self, key: str, value: int) -> bool:
        """
        Adds a new key-value pair to the Hash Table.
        :param key: Key
        :param value: Value
        :return: True if the key-value pair is set successfully.
        """
        logger.info(f'Inserting pair {key} - {value}')
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        logger.info('Inserted pair successfully')

    def get_item(self, key: str) -> int | None:
        """
        Returns the value associated with the key if it is present in the Hash Table.
        :param key: The key for which the associated value is required.
        :return: The value associated with the key. Returns none if the key does not exist.
        """
        logger.info(f'Getting value associated with {key}')
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    logger.info(f'{key} - {self.data_map[index][i][1]}')
                    return self.data_map[index][i][1]
        logger.warning('Key does not exist in the Hash Table')
        return None

    def keys(self) -> list:
        """
        Returns a list of all the keys present in the Hash Table.
        :return: List of all keys.
        """
        logger.info('Getting all keys from the Hash Table')
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        logger.info(f'Keys - {all_keys}')
        return all_keys

# Usage
if __name__ == '__main__':
    # Creating empty hash table
    my_hash_table = HashTable()
    my_hash_table.print_table()

    # Setting items
    my_hash_table.set_item('bolts', 1400)
    my_hash_table.set_item('washers', 50)
    my_hash_table.set_item('lumber', 70)
    my_hash_table.print_table()

    # Getting items
    my_hash_table.get_item('bolts')
    my_hash_table.get_item('washers')
    my_hash_table.get_item('lumber')
    my_hash_table.get_item('screws')

    # Getting all keys
    my_hash_table.keys()
