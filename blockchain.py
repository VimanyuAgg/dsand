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

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()

    @property
    def get_hash(self):
        return self.hash

    def __repr__(self):
        return f"Block(timestamp={self.timestamp},data={self.data},hash:{self.hash})"


class Blockchain:

    def __init__(self, data=None):
        self.tail = Block(datetime.datetime.utcnow(), None, None)
        if data:
            self.add_block(data)

    def create_block(self, data):
        '''Creates and returns a new block'''
        new_block = Block(datetime.datetime.utcnow(), data, self.tail.get_hash())
        return new_block

    def add_block(self,data):
        '''Adds a new block in the blockchain with given data'''
        new_block = self.create_block(data)
        new_block.prev = self.tail
        self.tail = new_block

    @property
    def get_prev_block(self):
        return self.tail.prev

    @property
    def get_latest_block(self):
        return self.tail

    @property
    def get_size(self):
        size = 0
        runner = self.tail
        while runner:
            size += 1
            runner = runner.prev

        return size - 1  # We start by creating a bogus element tail

    def __repr__(self):
        res = ""
        runner = self.tail

        # looping till prev element exists so that bogus tail element that gets initialized on blockchain
        # creation isn't printed
        while runner.prev:
            res = f"<-{runner}" + res
            runner = runner.prev

        return res[2:]  # Removing the "<-" symbol at the end





