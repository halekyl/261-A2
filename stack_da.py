# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: #2 Part 3 Stack ADT
# Description: Implement a Stack ADT class by using the Dynamic Array data structure that you have
# implemented in dynamic_array.py as underlying data storage for your Stack ADT.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def push(self, value: object) -> None:
        """
        Adds a new element to the top of the stack.
        """
        push = self.da.append(value)
        return push

    def pop(self) -> object:
        """
        Removes the top element from the stack and returns its value.
        If the stack is empty, raises the “StackException”.
        """
        # to handle empty stack
        if self.da.is_empty():
            raise StackException

        top_element_index = self.da.size - 1
        value_of_top_element = self.da.get_at_index(top_element_index)
        self.da.remove_at_index(top_element_index)
        return value_of_top_element

    def top(self) -> object:
        """
        Returns the value of the top element of the stack without removing it.
        If the stack is empty, raises the “StackException”.
        """
        # to handle empty stack
        if self.da.is_empty():
            raise StackException

        top_element_index = self.da.size - 1
        value_of_top_element = self.da.get_at_index(top_element_index)
        return value_of_top_element

    def is_empty(self) -> bool:
        """
        Returns True if there are no elements in the stack. Otherwise it returns False.
        """
        bool = self.da.is_empty()
        return bool

    def size(self) -> int:
        """
        Returns the number of elements currently in the stack.
        """
        size = self.da.length()
        return size




# BASIC TESTING
if __name__ == "__main__":
    pass

    # # push example 1
    #s = Stack()
    #print(s)
    #for value in [1, 2, 3, 4, 5]:
    #    s.push(value)
    #print(s)

    # # pop example 1
    #s = Stack()
    #try:
    #     print(s.pop())
    #except Exception as e:
    #     print("Exception:", type(e))
    #
    #for value in [1, 2, 3, 4, 5]:
    #    s.push(value)
    #
    #for i in range(6):
    #    try:
    #        print(s.pop())
    #    except Exception as e:
    #        print("Exception:", type(e))

    # # top example 1
    #s = Stack()
    #try:
    #     s.top()
    #except Exception as e:
    #     print("No elements in stack", type(e))
    #s.push(10)
    #s.push(20)
    #print(s)
    #print(s.top())
    #print(s.top())
    #print(s)

    # # is_empty example 1
    #s = Stack()
    #print(s.is_empty())
    #s.push(10)
    #print(s.is_empty())
    #s.pop()
    #print(s.is_empty())

    # # size example 1
    #s = Stack()
    #print(s.size())
    #for value in [1, 2, 3, 4, 5]:
    #    s.push(value)
    #print(s.size())
