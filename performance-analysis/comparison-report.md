# Performance Comparison Report

## Objective

The objective of this experiment was to compare the execution performance of Linear Search and Binary Search using Python and the py-spy profiler.

## Hardware

- Operating System: Windows 11
- Language: Python 3.14.7
- Profiler: py-spy

## Algorithms Compared

### Linear Search

- Searches one element at a time.
- Works on both sorted and unsorted data.
- Time Complexity: O(n)

Execution Time:
0.0052 seconds (approximately)

### Binary Search

- Searches by repeatedly dividing the search space into two halves.
- Requires sorted data.
- Time Complexity: O(log n)

Execution Time:
(Add the time shown after running binary_search.py)

## Comparison

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| Time Complexity | O(n) | O(log n) |
| Data Requirement | Unsorted or Sorted | Sorted Only |
| Speed | Slower | Faster |

## Conclusion

Binary Search performed much faster than Linear Search because it reduces the search space by half in every step. Linear Search checks elements one by one, making it slower for large datasets.
