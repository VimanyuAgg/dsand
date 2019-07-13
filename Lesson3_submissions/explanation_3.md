## Problem 3: Rearrange Array Digits

#### Algorithm - Merge Sort
As the expected runtime is `O(nlogn)`, merge sort is used to sort the array as it always gives O(n log n) time complexity
regardless of input. Quicksort has better *constants* than merge sort but its time complexity  depends on the selection of 
pivot and can give `O(n^2)` in the worst case. In order to meet the expected time complexity, I decided to stick with merge
sort even though it uses `O(n)` space complexity. I could also have used Heap sort as it also gives O(n logn) time complexity,
while maintaining `O(1)` space complexity but that would have meant permanently changing the `input_list`. 

 
#### Complexity Discussion
* Time Complexity: O(n log n) in every case where input is valid
* (Additional) Space Complexity: O(n) to store the sorted array during merge sort