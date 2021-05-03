from .conf import SortOrder


class QuickSort:
    """
    Quick sort works by finding the right index for the item in the
    array. The element which is moved to its rightful index is called pivot and
    can be picked on following criteria:
    1. Randomly from the list
    2. The first element from the list
    3. The middle element from the list

    Once the pivot moves to the correct index, it divides the remaining
    list into 2 sub-arrays, and can therefore be processed in a recursive way.
    The algorithm uses divide and conquer strategy.

    In algorithm implementation we create a partitioning mechanism which
    will bring pivot to the right index and create 2 subarrays. To pick the pivot
    element, we will use approach 2. (one can use 1. or 3. as well).

    Note that in the worst case scenario sorting can lead to O(n^2)
    running time rather than O(nlogn). This can occur more often as list might be
    partially sorted.

    Refer this video for more info: https://youtu.be/-qOVVRIZzao
    """
    def __init__(self, order=SortOrder.ASC):
        """
        Initializes the Quicksort with the order
        """
        self.current_order = order

    def partition(self, arr, start, end):
        """
        Moves the pivot to its correct index within the array and returns its index.
        Note that partition will allow split around the pivot point such that all elements
        on the left sub array will be smaller / bigger (depending on sort order), and all the
        elements in the right will be bigger / smaller (depending on sort order).
        :param arr: List if items
        :type arr: list
        :param start: start index for the list
        :type start: int
        :param end: end index for ths list
        :type end: int
        :return: correct index of the pivot element
        :rtype: int
        """

        # Initializing pivot's index to start
        pivot_index = start
        pivot_el = arr[pivot_index]

        start_index = pivot_index + 1
        end_index = end

        while start_index <= end_index:

            if self.current_order == SortOrder.ASC:

                while arr[start_index] <= pivot_el and (start_index <= end):
                    start_index += 1

                    # break the loop if start goes beyond end
                    if start_index > end:
                        break

                while (arr[end_index] > pivot_el) and (end_index >= start):
                    end_index -= 1

                    # break the loop if start goes beyond end
                    if end_index < start:
                        break

            elif self.current_order == SortOrder.DESC:

                while (arr[start_index] >= pivot_el) and (start_index <= end):
                    start_index += 1
                    # break the loop if start goes beyond end
                    if start_index > end:
                        break

                while (arr[end_index] < pivot_el) and (end_index >= start):
                    end_index -= 1
                    # break the loop if start goes beyond end
                    if end_index < start:
                        break

            if start_index < end_index:

                temp = arr[start_index]
                arr[start_index] = arr[end_index]
                arr[end_index] = temp

                # move the indexes after the swap
                start_index += 1
                end_index -= 1

        temp = arr[end_index]
        arr[end_index] = pivot_el
        arr[pivot_index] = temp

        # return end index as it is the correct location
        return end_index

    def _sort(self, arr, start, end):
        """
        Recursively calls itself to find the partition on the array. This is an in place sorting mechanism so
        no extra space to store the sorted array is required.
        :param arr: list of items to be sorted
        :type arr: list
        :param start: start index for the list
        :type start: int
        :param end: end index for the list
        :type end: int
        """

        if start < end:
            partition_index = self.partition(arr, start, end)

            # since we implement do while internally we add 1 to partition index so that the array
            # includes the partitioned item

            self._sort(arr, start, partition_index - 1)
            self._sort(arr, partition_index + 1, end)

    def sort(self, arr):
        """
        Given the list, sort it using quicksort.
        :param arr: list of items to sort
        :type arr: list
        :return: sorted array
        :rtype: list
        """

        if len(arr) < 2:
            return arr
        else:
            # we pass end as len(arr) as end and not len(arr) - 1 because we implement do while internally
            self._sort(arr, 0, len(arr) - 1)
            return arr


