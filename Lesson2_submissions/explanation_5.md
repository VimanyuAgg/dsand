## Problem 5

#### Design Discussion
In `Blockchain` class, I have implemented
* `add_block()` which internally uses `create_block()`
* `get_prev_block()` which allows one to traverse to previous block in the chain
* `get_latest_block()` which allows one to get to the latest block in the chain 
* `get_size` to know how long is the blockchain and I made it a `non-callable` so that no one can modify it
* `__repr__` printing instances of `Blockchain`

In `Block` class, I have implemented
* `__repr__` printing instances of `Block`
* (modified) `calc_hash` to use utc timestamp so that each hash is unique

I have used Python's `datetime` module `utcnow()` to calculate the timestamp as UTC and GMT are equivalent
and also because I watched this -> `The Problem with Time & Timezones - Computerphile` (link: https://www.youtube.com/watch?v=-5wpm-gesOY&list=TLBBCouWmde2kE6qFG90Fsn3GusE_aTr8k)

Once design decision that I took was to create the blockchain using `tail` pointer instead of `head`. I felt because any
*ledger* (hotel bookings, bank summary etc.) always start with the **latest** entry. Moreover, as no element of a 
blockchain is supposed to be deleted, blocks can only be appended at the tail.
So, instead of keeping a `head` pointer, I maintained a `tail` pointer. But I made sure (tried my best!) to hide this abstraction
from the user of the class. 

#### Complexity Discussion & Possible Improvements
* `create_block`: O(1) in time and space
* `add_block()` : O(1) in time and space
* `get_prev_block()`: O(1) in time and space
* `get_latest_block()`: O(1) in time and O(1) in space 
     * *without* `self.has_elements` it would be O(n) in time because it'd check if the blockchain size is greater than 0 in order to hide the `tail` from the user
     * In order to make it O(1) in time, I can also create a separate class variable to maintain size (`self.size`)
         
* `get_size()`: O(n) in time and O(1) in space as Linked List traversal is O(n) where n is the number of blocks in the chain.
     * *Improvement:* If I create a `self.size` variable that keeps track of number of elements in blockchain, it'd also be O(1) in time.
     That way, I can get rid of `self.has_elements` and `get_latest_block()` would check `if self.size > 0` instead of `if self.has_elements`
   