from .conf import SortOrder


class MergeSort:
    """
    Merge sort uses the divide and rule strategy to break down array into
    smaller arrays in each recursive step and then combine the steps to generate
    the sorted array.
    Merge sort is O(nlogn) and is useful for sorting larger arrays. Merge sort takes 'n' more
    memory cause it does not sort the array in-line (saves sorted data in new array)
    """

    def __init__(self, order: int = SortOrder.ASC):
        """
        Initialize merge sort with order (ASC / DESC)
        :param order: ASC / DESC
        :type order: int
        """
        self.current_sort_order = order

    def merge(self, arr1, arr2):
        """
        Merge two arrays based on order. (order 1 means ASCENDING, 0 means DESCENDING)
        :param arr1: The first array
        :type arr1: list
        :param arr2: The second array
        :type arr2: list
        :return: combined sorted array
        :rtype: list
        """

        # separate array required to save combined result
        # size will be len(arr1) + len(arr2)
        combined_array = []
        index_arr1, index_arr2 = 0, 0

        # run while one of the index reached end of the respective arr
        while index_arr1 < len(arr1) and index_arr2 < len(arr2):

            item_arr1 = arr1[index_arr1]
            item_arr2 = arr2[index_arr2]
            if item_arr1 <= item_arr2:
                if self.current_sort_order == SortOrder.ASC:
                    combined_array.append(item_arr1)
                    index_arr1 += 1
                elif self.current_sort_order == SortOrder.DESC:
                    combined_array.append(item_arr2)
                    index_arr2 += 1

            elif item_arr1 > item_arr2:
                if self.current_sort_order == SortOrder.ASC:
                    combined_array.append(item_arr2)
                    index_arr2 += 1
                elif self.current_sort_order == SortOrder.DESC:
                    combined_array.append(item_arr1)
                    index_arr1 += 1

        # if arr1 is complete, add all items in arr2 into combined array
        if index_arr1 == len(arr1):
            combined_array.extend(arr2[index_arr2:])

        # if arr2 is complete, add all items in arr1 into combined array
        elif index_arr2 == len(arr2):
            combined_array.extend(arr1[index_arr1:])

        return combined_array

    def _sort(self, arr):
        """
        Sorts the array by recursively calling itself. Splits the array into 2 sub-arrays,
        and call the merge method to merge two sorted subarrays.
        :param arr:
        :type arr:
        :return:
        :rtype:
        """

        lower_bound = 0
        upper_bound = len(arr) - 1
        mid = int(len(arr) / 2)

        if lower_bound < upper_bound:
            # call sort on left sub-array
            left_subarray = arr[lower_bound:mid]
            left_merged_arr = self.sort(left_subarray)

            # call sort on right sub-array
            # add 1 to upper bound so that the element at that index is included
            right_subarray = arr[mid:upper_bound + 1]
            right_merged_arr = self.sort(right_subarray)

            # return the combined sorted array
            return self.merge(left_merged_arr, right_merged_arr)

        # this is the exit condition of recursion when there is only 1 element in sub array
        else:
            return arr

    def sort(self, arr):
        """
        Sort using merge sort.
        :param arr: The array to be sorted
        :type arr: list
        :return: sorted array
        :rtype: list
        """

        if len(arr) == 1:
            return arr
        else:
            return self._sort(arr)




