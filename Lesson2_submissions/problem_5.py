import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string:{} of data!".format(self.timestamp).encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()

    @property
    def get_hash(self):
        return self.hash

    def __repr__(self):
        # return f"Block(timestamp={self.timestamp},data={self.data},hash={self.hash})" # Too ugly output
        return f"Block(data={self.data})"


class Blockchain:

    def __init__(self, data=None):
        self.tail = Block(datetime.datetime.utcnow(), None, None)
        self.has_elements = False
        if data:
            self.add_block(data)

    def create_block(self, data):
        '''Creates and returns a new block
        :args: data - (transaction Data)
        :returns: newly created Block element
        '''
        self.has_elements = True
        new_block = Block(datetime.datetime.utcnow(), data, self.tail.get_hash)
        return new_block

    def add_block(self,data):
        '''Adds a new block in the blockchain with given data
        :args: data - (transaction Data)
        :return: None
        '''
        new_block = self.create_block(data)
        new_block.prev = self.tail
        self.tail = new_block


    def get_prev_block(self, block=None):
        '''
        :args: block - Block element whose previous block is desired in current blockchain
        :return: previous Block element in blockchain if valid input else returns None
        '''
        if isinstance(block, Block):
            return block.prev
        else:
            return None

    @property
    def get_latest_block(self):
        '''Returns the last block element in the blockchain that's not tail '''
        if not self.has_elements:  # To hide tail from user
            return None
        else:
            return self.tail

    @property
    def get_size(self):
        '''Returns number of elements in blockchain (int)'''
        size = 0  # Time complexity can be improved from O(n) to O(1) using a self.size variable but seemed overkill
        runner = self.tail
        while runner:
            size += 1
            runner = runner.prev

        return size - 1  # We start by creating a bogus element tail that we hide from user

    def __repr__(self):
        if not self.has_elements:
            return "Blockchain(Empty)"
        res = ""
        runner = self.tail

        # looping till prev element exists so that bogus tail element that gets initialized on blockchain
        # creation isn't printed
        while runner.prev:
            res = f"<-{runner}" + res
            runner = runner.prev
        res = f"Blockchain({res[2:]})"  # Removing the "<-" symbol at the end
        return res

print("#### TC1 ####")
# #### TC1 ####
# Test Case 1 - Empty Block Chain

bc = Blockchain()
print(bc.get_size)
# 0

print(bc.get_latest_block)
# None

print(bc)
# Blockchain(Empty)

print(bc.get_prev_block())
# None

print("#### TC2 ####")
# #### TC2 ####
# Test Case 2 - Blockchain of single element
bc2 = Blockchain()
bc2.add_block("data1")

print(bc2.get_size)
# 1

print(bc2.get_latest_block)
# Block(data=data1)

print(bc2)
# Blockchain(Block(data=data1))

print(bc2.get_prev_block())
# None

print("#### TC3 ####")
# #### TC3 ####
# Test Case 3 - Blockchain of multiple elements & Initialized in a slightly different way
bc3 = Blockchain("data1")
bc3.add_block("data2")
bc3.add_block("data3")
bc3.add_block("data4")

print(bc3.get_size)
# 4

print(bc3.get_latest_block)
# Block(data=data4)

print(bc3)
# Blockchain(Block(data=data1)<-Block(data=data2)<-Block(data=data3)<-Block(data=data4))

print(bc3.get_prev_block(bc3.get_latest_block))
# Block(data=data3)

# Checking if next block contains hashcode of previous blockchain element
print(bc3.get_latest_block.previous_hash == bc3.get_prev_block(bc3.get_latest_block).get_hash)
# True
