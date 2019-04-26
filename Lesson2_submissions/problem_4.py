# Problem 4: Active Directory
# Modified the self.group & self.users variables as the order
# in which there added isn't important and searching in a set is O(1)
# while searching in a list is O(n) where n is the length of the list
# Used recursion to avoid code duplicacy
# Time Complexity: O(n) where n is the total number of user entries inside the current group and sub-groups, sub-sub groups, sub-sub-sub...(till they exist) in curr group


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

parent_user = "parent"
parent.add_user(parent_user)
child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None or group is None:
        return False

    # searching in set is O(1)
    if user in group.get_users():
        return True

    # searching in set is O(1)
    inner_groups = group.get_groups()

    for g in inner_groups:
        if is_user_in_group(user, g):
            return True

    return False

# Test Case 1
print(is_user_in_group('', child))
# False

# Test Case 2
print(is_user_in_group(parent_user, None))
# False

# Test Case 3
print(is_user_in_group(parent_user, child))
# False

# Test Case 4
print(is_user_in_group(sub_child_user, parent))
# True