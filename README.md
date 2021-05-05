# Algorithms implemented in Python.

The python package is available as pyalgo, which can be installed using :

```bash
git clone https://github.com/nitinkatyal1314/algorithms.git
python setup.py install
```

# Dependencies

The package depends on data-structures repo here : https://github.com/nitinkatyal1314/data-structures/tree/main . 

These data structures are used in algorithms throughout. The package is alreaded added as a dependecy in setup.py
so the above installation instruction will recolve the package (with correct version).


# Sorting Algorithms

Following sorting algorithms are available: 

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Heap Sort
6. Quick Sort

The logic of implementation is available within the code with their big-oh notations.


## To use sorting algorithm like Mergesort, following are the steps:

```bash

# import MergeSort from pyalgo sorting module
# SortOrder is to specify order of sort (ASC - Ascending, DESC - Descending)
from pylogo.sorting import MergeSort, SortOrder


# items to be sorted
items = [1, 6, 3]

# prints the sorted list in Ascending order
MergeSort(order=SortOrder.ASC).sort(items)

OR 

# prints the sorted list in Descending order
MergeSort(order=SortOrder.DESC).sort(items)

```

### The examples directory contain the examples for the available algorithms.

### Note: These algorithms are for learning purpose only. Contributions are welcomed.

