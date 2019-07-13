## Problem 4: Dutch National Flag

#### Algorithm - Sort of QuickSort Patitioning
This is a well-known problem and has variants of 2-way partitioning as well as 3-way partitioning. Current problem falls 
under 3-way partitioning as we have 0, 1 and 2 filling up the array. The resultant array can be thought of as having below regions:
* [0:low-1] : Filled with zeroes
* [low: mid-1]: Filled with ones
* [mid: hi]: Unknown region (to be shrunk by algorithm)
* [hi+1:]: Filled with twos

Note: The above ranges are inclusive of both end-points. We start with the unknown region and shrink it as we traverse
the array by placing the digits in appropriate positions in accordance with above ranges. Finally, we end up with a sorted
array in a single traversal

 
#### Complexity Discussion
* Time Complexity: O(n) as there is a single pass
* (Additional) Space Complexity: O(1) as the sorting is done in-place