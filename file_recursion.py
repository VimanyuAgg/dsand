# Problem 2: File Recursion
# Uses Recursion if a directory is found
# Time Complexity is O(n) where n is number of all the entries in the directory hierarchy
# Space Complexity is also O(n) where n is number of all the entries in the directory hierarchy
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # result list for current path
    # Returns an empty list if current path doesn't any results
    res = []

    dir_entries = os.listdir(path)

    for entry in dir_entries:

        # Go inside if it's a directory directory
        if os.path.isdir(os.path.join(path, entry)):
            inner_files = find_files(suffix, os.path.join(path, entry))

            # Add to current result list if a non-empty list is returned
            if len(inner_files) > 0:
                res += inner_files

        # it's a file
        # Checking the file ending
        # Complexity of endswith should be O(a+b) where a is length of current file extension and b is the length of suffix
        # Since O(a+b) is lower in magnitude than O(n), time complexity is still O(n)
        elif entry.endswith(suffix):
            res.append(entry)
    return res

print(find_files('.h','.'))