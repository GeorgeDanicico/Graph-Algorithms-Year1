from queue import PriorityQueue

class Pair:
    def __init__(self, value, priority):
        self._first = value
        self._second = priority

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second


class Priority_Queue(object):
    def __init__(self):
        self._queue = []

    def is_empty(self):
        return len(self._queue) == 0

    def push(self, pair):
        position = 0
        if len(self._queue) == 0:
            self._queue.append(pair)
        else:
            while position < len(self._queue) and self._queue[position].second < pair.second:
                position += 1

            if position < len(self._queue) and self._queue[position].second == pair.second:
                while position < len(self._queue) and self._queue[position].first < pair.first and self._queue[position].second == pair.second:
                    position += 1

            self._queue.insert(position, pair)

    def pop(self):
        return self._queue.pop(0)


