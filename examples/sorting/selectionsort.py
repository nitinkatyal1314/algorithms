from pyalgo.sorting import SelectionSort, SortOrder

if __name__ == "__main__":

    # list of items to be sorted
    items = [21, 100, 30, 55, 55, 1, 5, 18, 20, 2.3, -1, 11, 22, 4, 20.9, 45, 41.5, 38.9]

    # set sort order (ASC / DESC)
    selectionsort = SelectionSort(order=SortOrder.ASC)

    # For descending order uncomment
    # bubblesort = BubbleSort(order=SortOrder.DESC)

    sorted_array = selectionsort.sort(items)
    print("Sorted Array is : ", sorted_array)
