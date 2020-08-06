"""
First In / First Out
"""


def queue_collections_deque():
    """"""
    from collections import deque
    _queue = deque('abcdefgh')
    _queue.append('v')
    _queue.popleft()
    # or
    _queue.appendleft('v')
    _queue.pop()
