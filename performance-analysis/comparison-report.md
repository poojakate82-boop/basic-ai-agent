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

Metric	              Best case	                  Average case	                    Worst case
Time Complexity	       O(1)	                         O(n)	                          O(n)
Execution Time	  0.002215147018432617 sec    0.003108978271484375 sec	     0.008442401885986328 sec
Search Method	     Sequential	                   Sequential	                    Sequential

### Binary Search

- Searches by repeatedly dividing the search space into two halves.
- Requires sorted data.
- Time Complexity: O(log n)

Metric                 Best case	                     Average case	                  Worst case
Time Complexity	        O(1)	                           O(log n)	                       O(log n)
Execution Time	    1.5974044799804688e-05 sec	   5.0067901611328125e-06 sec 	  6.198883056640625e-06 sec
Search Method	      Divide and Conquer	          Divide and Conquer	          Divide and Conquer

## Comparison

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| Time Complexity | O(n) | O(log n) |
| Data Requirement | Unsorted or Sorted | Sorted Only |
| Speed | Slower | Faster |
=
## Conclusion

Binary Search performed much faster than Linear Search because it reduces the search space by half in every step. Linear Search checks elements one by one, making it slower for large datasets.
