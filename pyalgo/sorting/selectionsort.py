from .conf import SortOrder


class SelectionSort:
    """
    Selection sort works by dividing the array into left and right subarrays.
    The smallest / biggest item from the unsorted (right) subarray is selected in each iteration and
    put inside left subarray thereby making it sorted.

    This is O(n^2) algorithm since in each iteration i, (n-i) items are compared.
    """

    def __init__(self, order: SortOrder.ASC):
        """
        Initialize the sort order.
        :param order: sort order ASC / DESC
        :type order: int
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

        iteration_count = len(arr)
        left_subarray_index = 0

        # repeat n-1 times (n is length of array)
        while iteration_count > 1:

            # iterate through the right sub array
            for i in range(left_subarray_index + 1, len(arr)):

                #  the max item is the last item in the left subarray
                max_item = arr[left_subarray_index]

                # if the item
                if arr[i] < max_item:
                    # swap
                    temp = arr[i]
                    arr[i] = max_item
                    arr[left_subarray_index] = temp

            left_subarray_index += 1
            iteration_count -= 1

        return arr

    def _sort_descending(self, arr: list):
        """
        Sorts the list of items in the descending order.
        :param arr: list of items to sort
        :type arr: list
        :return: sorted array
        :rtype: list
        """
        iteration_count = len(arr)
        left_subarray_index = 0

        # repeat n-1 times (n is length of array)
        while iteration_count > 1:

            # iterate through the right sub array
            for i in range(left_subarray_index+1, len(arr)):

                #  the max item is the last item in the left subarray
                max_item = arr[left_subarray_index]

                # if the item
                if arr[i] > max_item:

                    # swap
                    temp = arr[i]
                    arr[i] = max_item
                    arr[left_subarray_index] = temp

            left_subarray_index += 1
            iteration_count -= 1

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