class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        res = []
        if self.is_word:
            res.append(suffix)

        for child in self.children:
            res += self.children[child].suffixes(suffix=suffix + child)

        return res

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        runner = self.root
        for char in word:
            if char not in runner.children:
                runner.insert(char)

            runner = runner.children[char]

        runner.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        runner = self.root

        for p in prefix:
            if p not in runner.children:
                return None

            runner = runner.children[p]

        return runner


def test(prefix):
    if prefix != '' and prefix != " ":
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print(prefixNode.suffixes())
        else:
            print(f"{prefix} not found!")
    else:
        print("")

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

testcase1 = test("a")
# ['nt', 'nthology', ntagonist', 'ntonym']
testcase2 = test("an")
# ['t', 'thology', tagonist', 'tonym']
testcase3 = test("djinn")
# 'djinn not found!'
testcase4 = test(" ")
# ''
testcase5 = test("fu")
# ['n', 'nction']
testcase6 = test("Tr")
# 'Tr not found!'  # Checking case sensitivity


