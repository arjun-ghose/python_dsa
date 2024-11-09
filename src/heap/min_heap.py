from src.utils.logger import Logger

logger = Logger('MinHeapLogger').get_logger()


class MaxHeap:
    def __init__(self) -> None:
        """
        Creates an empty Max Heap.
        """
        self.heap: list = []
        logger.info('Created Max Heap successfully')

    def _left_child(self, index: int) -> int:
        """
        Returns the index of the left child of the given index.
        :param index: The index whose left child is required.
        :return: Left child index.
        """
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """
        Returns the index of the right child of the given index.
        :param index: The index whose right child is required.
        :return: Left child index.
        """
        return 2 * index + 2

    def _parent(self, index: int) -> int:
        """
        Returns the parent node of the given index.
        :param index: The index whose parent is required.
        :return: Index of the parent.
        """
        return (index - 1) // 2

    def _swap(self, index_1: int, index_2: int) -> None:
        """
        Swaps the values stored in the two given indices within the Heap.
        :param index_1: The first index.
        :param index_2: The second index.
        :return: None
        """
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def _sink_down(self, index: int) -> None:
        """
        Moves a value at a given index down the heap to the appropriate index.
        :param index: The index of the value you want to sink down.
        :return: None
        """
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and
                    self.heap[left_index] < self.heap[min_index]):
                min_index = left_index

            if (right_index < len(self.heap) and
                    self.heap[right_index] < self.heap[min_index]):
                min_index = right_index

            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def print_heap(self) -> None:
        """
        Logs the heap.
        :return: None
        """
        logger.info(f'Heap - {self.heap}')

    def insert(self, value: int) -> bool:
        """
        Inserts a new value into the Heap.
        :param value: The value that needs to be inserted into the Heap.
        :return: True if the value is inserted successfully, false otherwise.
        """
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        logger.info(f'Inserted value {value} into the heap successfully')
        return True

    def remove(self) -> int | None:
        """
        Removes the root of the Heap and returns it's value.
        :return: The value of the root of the Heap.
        """
        if len(self.heap) == 0:
            logger.warning('No values to remove')
            return None

        if len(self.heap) == 1:
            min_value = self.heap.pop()
            logger.info(f'Removed value - {min_value}')
            return min_value

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        logger.info(f'Removed value - {min_value}')
        return min_value


# Usage
if __name__ == '__main__':
    # Initializing heap
    my_heap = MaxHeap()

    # Insert
    my_heap.insert(99)
    my_heap.insert(72)
    my_heap.insert(61)
    my_heap.insert(58)
    my_heap.print_heap()

    my_heap.insert(100)
    my_heap.print_heap()

    my_heap.insert(75)
    my_heap.print_heap()

    # Remove
    my_heap.remove()
    my_heap.print_heap()

    my_heap.remove()
    my_heap.print_heap()

    my_heap.remove()
    my_heap.print_heap()
