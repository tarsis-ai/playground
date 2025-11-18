import pytest
from src.queue import Queue

def test_enqueue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty() is True

def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

def test_is_empty():
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    assert queue.is_empty() is False
    queue.dequeue()
    assert queue.is_empty() is True

def test_size():
    queue = Queue()
    assert queue.size() == 0
    queue.enqueue(1)
    assert queue.size() == 1
    queue.enqueue(2)
    assert queue.size() == 2
    queue.dequeue()
    assert queue.size() == 1
    queue.dequeue()
    assert queue.size() == 0
