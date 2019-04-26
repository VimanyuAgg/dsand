## Problem 4: Active Directory
 
#### Design Discussion
Used recursion for elegant code 

#### Complexity Discussion
I modified the `self.group` & `self.users` variables as the order in which there added isn't important and searching in a set is O(1)
whereas searching in a list is O(n) where n is the length of the list Instead of modifying the stub, 
I could have also converted the output in line `56` & `60` to `set()`. Doing so, would have 
increased the time complexity (*bigger constants although still linear overall*) but creating these variables as `set` in 
the first place looked more optimal. 

* Time Complexity: O(n) where `n` is the total number of user entries inside the 
current group and sub-groups, sub-sub groups, sub-sub-sub...(till they exist) in `group`

* Additional Space Complexity: O(k) where `k` is the number of entries we hit while traversing through deepest group hierarchy 
in `group`. O(n) feels like a looser bound as we aren't storing all entries at a given point unless all groups have user 
at which point it won't be counted as *additional* space.