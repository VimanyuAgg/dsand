## Problem 5: Autocomplete Trie

#### Algorithm - Recursion
The crux of the autocomplete functionality is the implementation of `suffixes()` in `TrieNode` class. The optional suffixes
argument is used to track the suffixes gathered while recursing down the Trie before finally adding it to resultant array which
is returned. The type of recursion used is of type Depth-First-Search as we just need to keep track of the ongoing 
suffix. If we had used BFS, we would have to keep track of lots of partial suffixes and it would be much more difficult to 
implement.

 
#### Complexity Discussion
* **Time Complexity**:
Building the Trie would be O(n*m) where `n`=number of elements and `m`=average length of words as we would have to traverse
all the words in the input `wordList`. `find()` operation would be O(D) in the worst case, where D = Max Depth of the Trie.
Finding `trieNode.suffixes()` would be O(k) where k=number of nodes in the subtree of `trieNode` in the Trie.  

* **Space Complexity**:
In order to store Trie, we would need space of the *order* of O(n*m) where n=number of words in `wordList` and m=average
length of the word. We end up saving some space because of the overlap of prefixes in different words.  