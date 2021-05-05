from pyds.heap import Heap, HeapType
from .conf import SortOrder


class HeapSort:
    """
    Heap Sort creates the heap from the array and then deletes each node from the heap.
    For MIN Heap -> ascending order
    For MAX heap -> descending order
    """

    def __init__(self, order: int = SortOrder.ASC):
        """
        Initialize the heap with the type
        :param order: Whether to sort ascending / descending
        :type order:
        """

        self.heap_type = None

        if order == SortOrder.ASC:
            # initialize the heap type
            self.heap_type = HeapType.MIN
        else:
            self.heap_type = HeapType.MAX

        # initialize the heap
        self.heap = Heap(heap_type=self.heap_type)

    def _sort_n(self, arr: list):
        """
        Sorts the array using the heapify method which takes O(n) time. Check the heapify method for details.

        :param arr: list of items to sort
        :type arr: list
        :return: sorted list of items
        :rtype: list
        """
        sorted_array = []
        heap_as_arr = self.heap.create_heap_from_array(arr)

        # start deleting item from the heap
        for index in range(0, len(heap_as_arr)):
            node = self.heap.delete_node()
            sorted_array.append(node)

        return sorted_array

    def _sort_nlogn(self, arr: list):
        """
        Sort the array using heap.

        Time complexity is O(nlogn)
            nlogn -> n for number of elements, logn for each node added
            nlogn -> n for number of elements, logn for each node deleted

        Uses additional array to save the sorted array so space complexity is O(n).

        :param arr:
        :type arr:
        :return:
        :rtype:
        """

        sorted_array = []

        # create the heap from the array
        for item in arr:
            self.heap.add_node(item)

        # start deleting item from the heap
        for index in range(0, len(arr)):
            node = self.heap.delete_node()
            sorted_array.append(node)

        return sorted_array

    def sort(self, arr):
        """
        Given the list, sort it using heapsort.
        :param arr: list of items to sort
        :type arr: list
        :return: sorted array
        :rtype: list
        """

        if len(arr) < 2:
            return arr
        else:
            sorted_arr = self._sort_n(arr)
            return sorted_arr
