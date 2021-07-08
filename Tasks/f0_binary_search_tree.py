"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
import networkx as nx

bst = {}

from typing import Any, Optional, Tuple

# import networkx as nx

"""
{
    'key': 5, 'value': 123, 
        'left': {'key': 2, 'value': 123, 
                 'left': {'key': -4, 'value': 123}, 
                 'right':{'key': 3, 'value': 123}
                 }, 
        'right':{'key': 21, 'value': 123, 
                 'left': {'key': 19, 'value': 123}, 
                 'right':{'key': 25, 'value': 123}
                 }
 }
"""


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    print(key, value)

    if key is None:
        return None

    # internal procedure
    def insertRoutine(root_: dict, key_: int, value_: Any) -> dict:
        # if BST is empty, insert the root
        if not len(root_):
            root_ = {'key': key_, 'value': value_}
            return root_
        else:
            # check key if equal to parameter
            if root_['key'] == key_:
                # and update value if its changed
                if root_['value'] != value_:
                    root_['value'] = value_
                return root_
            # if parameter is bigger than key - goes to the right
            elif root_['key'] < key_:
                root_['right'] = insertRoutine(root_['right'], key_, value_)
            # if parameter is smaller than key - goes to the left
            else:
                root_['left'] = insertRoutine(root_['left'], key_, value_)
        return root_

    global bst

    insertRoutine(bst, key, value)


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    print(key)

    def minValueFind(root_):
        current = root_

        # loop down to find the leftmost leaf
        while current['left'] is not None:
            current = current['left']
        return current

    # internal procedure
    def removeRoutine(root_: dict, key_: int) -> Optional[Tuple[int, Any]]:
        # if BST is empty, insert the root
        if not len(root_):
            return None
        # if parameter is bigger than key - goes to the right
        if root_['key'] < key_:
            return removeRoutine(root_['right'], key_)
        # if parameter is smaller than key - goes to the left
        elif root_['key'] > key_:
            return removeRoutine(root_['left'], key_)
        # if parameter is equal
        else:
            # check left and right
            if root_['left'] is None and root_['right'] is None:
                root_ = None
                return root_['key'], root_['value']
            # check left
            elif root_['right'] is None:
                root_ = None
                return root_['key'], root_['value']
            # check right
            elif root_['left'] is None:
                root_ = None
                return root_['key'], root_['value']
            # both are OK
            else:
                min_child = minValueFind(root_['right'])
                root_ = min_child
                return removeRoutine(root_['right'], key_)

    return removeRoutine(bst, key)


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    print(key)

    if key is None:
        return None

    # internal procedure
    def findRoutine(root_: dict, key_: int) -> Any:
        # if BST is empty, insert the root
        if not len(root_):
            return None
        if root_['key'] == key_:
            return root_['value']

        # if parameter is bigger than key - goes to the right
        if root_['key'] < key_:
            return findRoutine(root_['right'], key_)
        # if parameter is smaller than key - goes to the left
        else:
            return findRoutine(root_['left'], key_)

    global bst

    return findRoutine(bst, key)


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    bst.clear()

    return None
