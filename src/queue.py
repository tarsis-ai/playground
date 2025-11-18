class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if not self._queue:
            return None  # Or raise an exception, depending on desired behavior
        return self._queue.pop(0)
