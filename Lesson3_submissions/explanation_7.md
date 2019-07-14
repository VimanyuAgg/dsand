## Problem 6: Request Routing in a webserver with Trie

#### Design Choices
There are many ways to design the request routing in the webserver with Trie. A lot of implementation details can vary
depending on the business logic e.g. Do specific users (e.g. authenticated users/admin users) 
view different error pages (404, 403 pages etc.) than regular users. If yes, then it would be a good practice to implement
not_found_handler as a property of RouteTrieNode. Commonly, in a web application, the same function/template is rendered 
 for all the 404 errors, so we can save some space by just making it an attribute at RouteTrie Level rather than putting 
 it at RouteTrieNode Level. 
 
 Also, if there is a business use case that there can co-exist different routers which segregate Handlers not by a "/"
 but by any other symbol/logic (e.g. if we were building a router for Operating System rather than web where Windows support
  path segregation by "\" rather than "/" as in Unix/Linux systems), it would be helpful to actually use `split_path` at Router level implementation. But as
 URLs are almost universally segregated by "/" symbol for a webserver, we can safely put this implementation detail in RouterTrie Level.
 

 
#### Complexity Discussion
* Time Complexity: 
    * `Add_Handler`: O(n) where n is the number of list items when path is split by "/"
    * `Lookup`: O(n) worst case where n is the number of list items when path is split by "/". It's worst case because the algorithm
    might detect that the path doesn't exist at a certain point and yield the `not_found_handler`.

* (Additional) Space Complexity: O(n) where n is the number of RouterTrieNodes that need to be put inside the Trie.