# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: # 2 Part 4 Queue ADT
# Description: Implement a Queue ADT class by using the Dynamic Array data structure that you have
# implemented in dynamic_array.py as underlying data storage for your Queue ADT.

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def enqueue(self, value: object) -> None:
        """
        Adds a new value to the end of the queue.
        """
        enqueue = self.da.append(value)
        return enqueue

    def dequeue(self) -> object:
        """
        Removes and returns the value from the beginning of the queue.
        If the queue is empty, the method raises “QueueException”.
        """
        # to handle empty queue
        if self.da.is_empty():
            raise QueueException

        beginning_index = 0
        beginning_value = self.da.get_at_index(beginning_index)
        self.da.remove_at_index(beginning_index)
        return beginning_value

    def is_empty(self) -> bool:
        """
        Returns True if there are no elements in the queue. Otherwise it returns False.
        """
        bool = self.da.is_empty()
        return bool

    def size(self) -> int:
        """
        Returns the number of elements currently in the queue.
        """
        size = self.da.length()
        return size


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # enqueue example 1
    #q = Queue()
    #print(q)
    #for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    #print(q)

    # # dequeue example 1
    #q = Queue()
    #for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    #print(q)
    #for i in range(6):
    #     try:
    #        print(q.dequeue())
    #     except Exception as e:
    #        print("No elements in queue", type(e))

    # # is_empty example 1
    #q = Queue()
    #print(q.is_empty())
    #q.enqueue(10)
    #print(q.is_empty())
    #q.dequeue()
    #print(q.is_empty())

    # # size example 1
    #q = Queue()
    #print(q.size())
    #for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    #print(q.size())