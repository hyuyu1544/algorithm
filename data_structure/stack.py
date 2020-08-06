"""A STACK
.. Last in/ First out (LIFO)
.. PUSH in, POP out

good third-party packages:
.. list
.. collections.deque
.. queue.LifoQueue

ref.
https://realpython.com/how-to-implement-python-stack/
"""
from collections import deque
from queue import LifoQueue
# from .. import utils.TypePrints
from functools import wraps
import time
import sys
import os


def TypePrints(func):
    """Print func.__doc__ like type prints."""
    @wraps(func)
    def wrappers(*args, **kwargs):
        for c in func.__doc__:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.08)
        sys.stdout.flush()
        sys.stdout.write('\n')
        return func(*args, **kwargs)
    return wrappers


@TypePrints
def stack_list():
    """Use list to implement stack.
    Issue: list can run into speed issues as it grows.
    Because it built upon blocks of contiguous memory.
    You should never use list for any data structure that can be accessed by multiple threads. list is not thread-safe.
    """
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)  # [1,2,3]
    print(stack)
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1


@TypePrints
def stack_collections_deque():
    """Use collections.deque to implement stack.
    It is built upon a doubly linked list.
    Both the .append() and .pop() operations are atomic, meaning that they won't be interrupted by a different thread.
    """
    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)  # deque(['1', '2', '3'])
    print(stack)
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    print(stack.pop())  # 1


@TypePrints
def stack_queue_LifoQueue():
    """Use queue.Lifoqueue to implement stack.
    not necessary use this unless you need use threading.
    """
    stack = LifoQueue()
    stack.put(1)
    stack.put(2)
    stack.put(3)  # <queue.LifoQueue object at 0x7f408885e2b0>
    print(stack)
    print(stack.get())  # 3
    print(stack.get())  # 2
    print(stack.get())  # 1


if __name__ == "__main__":
    stack_list()
    stack_collections_deque()
    stack_queue_LifoQueue()
