from .conf import SortOrder


class BubbleSort:
    """
    Bubble sort works by comparing items with the next one, and swaps them if the item is bigger / smaller (based on
    Sort order). In each iteration the smaller / larger item will surface (like a bubble)

    This is an O(n^2) algorithms since for every item O(n) comparisons are done.
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

        :param arr:
        :type arr:
        :return:
        :rtype:
        """

        iteration_count = len(arr)
        while iteration_count > 1:

            # for every iteration the number of items to be sorted are iteration_count - 1
            for index in range(0, iteration_count - 1):
                if arr[index + 1] < arr[index]:
                    # swap
                    temp = arr[index + 1]
                    arr[index + 1] = arr[index]
                    arr[index] = temp

            # reduce iteration count
            iteration_count -= 1

        return arr

    def _sort_descending(self, arr: list):
        """
        Sorts the list in descending order.

        Use iteration count to track every iteration. Post each iteration the smallest element
        will surface to the end of the list.

        Therefore, after iteration i, the total items to sort is:
            n - i (n is the number of items in list)

        :param arr: list of items to sort
        :type arr: list
        :return: list of sorted items
        :rtype: list
        """

        iteration_count = len(arr)
        while iteration_count > 1:

            # for every iteration the number of items to be sorted are iteration_count - 1
            for index in range(0, iteration_count - 1):
                if arr[index + 1] > arr[index]:

                    # swap
                    temp = arr[index + 1]
                    arr[index + 1] = arr[index]
                    arr[index] = temp

            # reduce iteration count
            iteration_count -= 1

        return arr

    def sort(self, arr: list):
        """
        Sorts the items in the array based on the order.
        :param arr:
        :type arr:
        :return:
        :rtype:
        """

        if len(arr) < 2:
            return arr
        else:
            if self.current_order == SortOrder.ASC:
                return self._sort_ascending(arr)
            elif self.current_order == SortOrder.DESC:
                return self._sort_descending(arr)
