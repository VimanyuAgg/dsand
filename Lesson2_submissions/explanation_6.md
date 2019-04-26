## Problem 6: Union & Intersection

#### Design Discussion & Possible Improvements
* `union(llist_1, llist_2)` - If we use inner function(`_add_nodes()` on line `67`), we'll save time spent in the union operation but 
then it'd need to be implemented twice - once for `union` and once for `intersection`. 
I chose to sacrifice a bit of time efficiency *(still keeping the time complexity linear)* 
and maintain 'Do Not Repeat Code' principle.

*`intersection(llist_1, llist_2)` -  We could have gotten the size of both linked lists and chosen to create 
`elements_set` on line `102` with smaller linked list so as to improve space efficiency. 
But after looking at the current stub code, getting size would have made the code a bit slower as `size()` iterates 
through entire linked list. A workaround would be to include a `self.size` variable in linkedlist that 
increases/decreases on adding/removing a node. 

Moreover, if we have a scenario that one list is significantly longer than the other one to the point that one of them 
cannot be stored in memory, then storing elements from the smaller list would make sense. So, this is one possible 
improvement that I can think of. I'd love to know if there are more!

### Complexity Discussion
* `union(llist_1, llist_2)`: Time complexity is O(n+m) where n and m are the size of `llist1` and `llist2` respectively. 
Space complexity is O(1) as no additional space is needed.

* `intersection(llist1, llist2)` - Time complexity is O(n+m) where n and m are the size of `llist1` and `llist2` respectively.
    Space Complexity is O(n) where n is the size of `llist1` (Possible improvement as discussed in design discussions on top).

