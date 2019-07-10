## Problem 1: Square Root of an Integer

#### Algorithm Choice
There were many different ways to solve this problem without using any library function, like - going iteratively from  
from 1, and computing squares 1*1, 2*2, 3*3, stopping as soon as we reach a result which is greater than input `number` 
and returning `result-1` so as to give the floor value. But the question asked to be solved in `O(log n)` time, and 
Binary search yields results in log n time. So, I solved the question using Binary search.
 
#### Complexity Discussion
* Time Complexity: O(log n)
* (Additional) Space Complexity: O(1)