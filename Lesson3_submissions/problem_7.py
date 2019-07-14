# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,root_handler=None, not_found_handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

        # Not Found Handler would be a property of the RouteTrie and not of individual Trie Node
        # 404 Page wouldn't/shouldn't vary if there's no page like /about/me/blahblah or /about/you/foobar
        # 404 Page is same across the entire application & Hence not_found_handler is created as an attribute for
        # RouteTrie and not of RouteTrieNode
        if not not_found_handler:
            self.not_found_handler = "404 Page Not Found Handler!"
        else:
            self.not_found_handler = not_found_handler

    def insert(self, node_path, given_handler_name=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        runner = self.root
        default_handler = ""
        for node in node_path.split("/"):
            if node not in runner.children:
                runner.insert(node)

            runner = runner.children[node]
            default_handler += node + " "

        if len(runner.children) == 0:
            if given_handler_name:
                runner.handler = given_handler_name
            else:
                runner.handler = default_handler


    def find(self, node_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        runner = self.root

        if node_path == "":
            return self.root.handler

        for node in node_path.split("/"):
            if node not in runner.children:
                return self.not_found_handler

            runner = runner.children[node]

        if runner.handler:
            return runner.handler

        else:
            return self.not_found_handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, node):
        # Insert the node as before
        self.children[node] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self,root_handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path, handler_name):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.router.insert(path, handler_name)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if len(path) == 0 or path[-1] == "/":
            return self.router.find(path[:-1])
        return self.router.find(path)


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        return path.split("/")  # Redundant in current implementation



# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup(""))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one