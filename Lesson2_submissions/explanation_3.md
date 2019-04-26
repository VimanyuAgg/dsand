## Problem 3: Huffman Coding

#### Design/Data Structure Discussion
* Used collections.Counter to get the frequencies as it is written in C which is faster than writing same code in python
* Used OrderedDict to maintain the order of sorted dictionaries as 'dict' is inherently orderless in python and OrderedDict are implemented using doubly linked lists and removing items from edges is O(1)

#### Complexity Discussion
* Huffman encoding Time Complexity: O(n^2 log n) where n is the number of unique characters in the input string as the data is sorted 1log1 + 2log2 + 3log3 ...nlogn times
* Huffman decoding Time Complexity: O(nk) where n is the number of unique characters in input data and k is the avg height of huffman tree

#### Note to Reviewer
I have added certain assert statements to check for data validity (to check if input is indeed as string). I'd love to know
how I could have the asserts better!

