import sys
from collections import Counter, OrderedDict


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def generate_huffman_tree(freq_map):
    if len(freq_map) == 1:
        return freq_map

    freq_map = OrderedDict(sorted(freq_map.items(), key=lambda x: x[1]))

    low1 = freq_map.popitem(last=False)
    low2 = freq_map.popitem(last=False)
    n = Node("*")
    n.left = low1[0]
    n.right = low2[0]
    freq_map[n] = low1[1]+low2[1]
    return generate_huffman_tree(freq_map)


def traverse_tree(t,encoding_map,path):
    if not isinstance(t.left, Node):
        encoding_map[t.left] = path+"0"

    else:
        # go down the left subtree
        traverse_tree(t.left, encoding_map, path+"0")

    if not isinstance(t.right, Node):
        encoding_map[t.right] = path+"1"
    else:
        # go down the right subtree
        traverse_tree(t.right, encoding_map, path + "1")


def get_encoding_map_from_huffman_tree(tree):
    encoding_map = {}
    traverse_tree(tree, encoding_map, "")
    return encoding_map


def generate_encoded_data(tree,data):
    encoding_map = get_encoding_map_from_huffman_tree(tree)
    # print(encoding_map)
    encoded_str = ""
    for d in data:
        encoded_str += encoding_map[d]
    return encoded_str


def huffman_encoding(data):
    # Assert to check if input is a valid string
    if not isinstance(data, str):
        assert 1 == 0, "Input is not a valid string"

    # Checks if input is a non-empty string
    if data is None or len(data) == 0:
        return "", None

    freq = OrderedDict(Counter(data))
    huffman_tree = generate_huffman_tree(freq)
    root = list(huffman_tree.items())[0][0]

    if isinstance(root, Node):
        encoded_str = generate_encoded_data(root, data)

    elif isinstance(root,str):
        # handles the case when len(data) == 1
        encoded_str = "1"
    else:
        # Unexpected error
        assert 1 == 0, "Unexpected error"

    return encoded_str, huffman_tree


def huffman_decoding(data, tree):

    if tree is None:
        return ""

    decoded_str = ""
    root = list(tree.items())[0][0]

    if isinstance(root,str):
        # Handles the case when string to encode is of len 1
        return root

    curr = root
    for d in data:
        if d == "0":
            curr = curr.left
        else:
            curr = curr.right

        if isinstance(curr,str):
            decoded_str += curr
            curr = root

    return decoded_str


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))