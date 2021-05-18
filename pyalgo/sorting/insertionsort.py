from .conf import SortOrder


class InsertionSort:

    """
    Insertion sort divide the array into a sorted (left subarray) and the unsorted (right subarray). In insertion sort,
    the iteration moves through each element in unsorted array compares it with the elements in the sorted subarray
    till it reached the right location within the subarray. This process is repeated till all the items
    in the right subarray are visited.

    Insertion sort is O(n^2) algorithm since it compares the all the element in the right subarray O(n) to all the
    element in the left subarray until it is inserted at the correct place.

    """

    def __init__(self, order: SortOrder.ASC):
        """
        Initialize the sort order.
        :param order:
        :type order:
        """

        self.current_order = order

    def _sort_ascending(self, arr: list):
        """
        Sorts the list of items in the ascending order.
        :param arr: list of items to sort
        :type arr: list
        :return: sorted array
        :rtype: list
        """

        # right most index of left sub array
        index_left_subarray = 0
        index_right_subarray = 1

        while index_right_subarray < len(arr):

            if arr[index_right_subarray] < arr[index_left_subarray]:

                temp = arr[index_left_subarray]
                arr[index_left_subarray] = arr[index_right_subarray]
                arr[index_right_subarray] = temp

                index = index_left_subarray

                while index > 0:

                    if arr[index - 1] > arr[index]:

                        # swap on left sub array
                        temp = arr[index - 1]
                        arr[index - 1] = arr[index]
                        arr[index] = temp

                        index -= 1
                    else:
                        # break the loop because of the elements before are already sorted
                        break

            index_right_subarray += 1
            index_left_subarray += 1

        return arr

    def _sort_descending(self, arr: list):
        """
        Sorts the list of items in the descending order.
        :param arr: list of items to sort
        :type arr: list
        :return: sorted array
        :rtype: list
        """

        #right most index of left sub array
        index_left_subarray = 0
        index_right_subarray = 1

        while index_right_subarray < len(arr):

            if arr[index_right_subarray] > arr[index_left_subarray]:

                temp = arr[index_left_subarray]
                arr[index_left_subarray] = arr[index_right_subarray]
                arr[index_right_subarray] = temp

                index = index_left_subarray

                while index > 0:

                    if arr[index - 1] < arr[index]:

                        # swap on left sub array
                        temp = arr[index-1]
                        arr[index - 1] = arr[index]
                        arr[index] = temp

                        index -= 1
                    else:
                        # break the loop because of the elements before are already sorted
                        break

            index_right_subarray += 1
            index_left_subarray += 1

        return arr

    def sort(self, arr: list):
        """
        Sorts the items in the array based on the order.
        :param arr: list of items to sort
        :type arr: list
        :return: sorted array
        :rtype: list
        """

        if len(arr) < 2:
            return arr
        else:
            if self.current_order == SortOrder.ASC:
                return self._sort_ascending(arr)
            elif self.current_order == SortOrder.DESC:
                return self._sort_descending(arr)