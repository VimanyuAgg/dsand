## Problem 1: LRU Cache

#### Data Structure Choice
As the problem demands to maintain an order and presents the input in form of key,value pairs - I chose OrderedDict(). 
OrderedDict() is a built-in Python's collections library which supports removal of edge elements in O(1) time.
As get, put operations of LRU cache needed to be O(1) - Choosing OrderedDict() felt like a natural choice.
However, I could also use a dict() and a doubly linked list (I believe that's what OrderedDict() also uses) to implement my solution. 
I have presented that as well in the problem_1.py  

#### Complexity Discussion
* Time Complexity O(1)
* (Additional) Space Complexity O(1)