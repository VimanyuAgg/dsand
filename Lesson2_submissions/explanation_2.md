## Problem 2: File Recursion

#### Design Choice Discussion 
Used recursion to reduce code repeatability. Approach is basically to look at all the entries in the current directory. 
If there are any files in the current directory that have `suffix` as extension, we add them to our result list `res`. 
If there are any directories in the current directory, we go inside and recurse.
I used the output as a `list` as opposed to a `set` because there may be same filename but different content.

Also, it was unwarranted to assume that we can omit duplicate files in this operation. e.g. if this is used as search 
functionality, user should know *all* the files that have `suffix` rather than just unique filenames.

#### Complexity Discussion
* Time Complexity is O(n) where n is number of all the entries in the directory *hierarchy* (not just current directory).
* Space Complexity is also O(n) where n is number of all the entries in the directory *hierarchy*
(not just current directory). This is because we are storing (though temporarily) all the contents of a given directory and 
we are looping over all the directories. However, it can be argued that a tighter bound on space complexity is actually
the number of entries in the deepest hierarchical directory because we aren't storing *all* contents at any given time 
(unless all filenames have `suffix` but then it wouldn't count as *additional* space complexity!).  