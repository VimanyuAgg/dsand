## Problem 2: Search in a Rotated Sorted Array

#### Algorithm - Dual Binary Search
As the input array is a rotated sorted array, we first find the index of the lowest value using `find_index_of_lowest` 
that uses Binary Search and consumes O(log n) time & O(1) space. 
Then we create the original sorted array, as it's given that the array was sorted but then was rotated. 
This consumes O(n) space. Now, searching for the target value is the simple O(log n) binary search but 
in order to return it's index in the `input_list`, we must adjust for shifting the lowest value to far left (similar to origin shifting). 

 
#### Complexity Discussion
* Time Complexity: O(log n)
* (Additional) Space Complexity: O(n) to store the sorted array