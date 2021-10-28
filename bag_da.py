# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: #2 Part 2 Bag ADT
# Description: Implement a Bag ADT class by using the Dynamic Array data structure that you
# have implemented in dynamic_array.py as underlying data storage for your Bag ADT.

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of bag in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag.
        """
        self.da.append(value)
        return

    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the provided “value” object.
        Returns True if some object was actually removed from the bag. Otherwise, returns False.
        """
        for element in range(self.da.length()):
            if self.da.get_at_index(element) == value:
                self.da.remove_at_index(element)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Counts the number of elements in the bag that match the provided “value” object.
        """
        count = 0
        for element in range(self.da.length()):
            if self.da.get_at_index(element) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the content of the bag.
        """
        for element in range(self.da.length() - 1, - 1, - 1):
            self.da.remove_at_index(element)
        return

    def size(self) -> int:
        """
        Returns the number of elements currently in the bag.
        """
        size = self.da.length()
        return size

    def equal(self, second_bag: object) -> bool:
        """
        Compares the content of the bag with the content of the second bag provided by the user.
        Returns True if the bags are equal (same number of elements and same elements regardless of order)
        Otherwise, returns False.
        """
        # handles if bags do not have same number of elements
        if self.da.length() != second_bag.da.length():
            return False
        # handles if elements in bags are not the same elements
        for element in range(self.da.length()):
            compare_element = self.da.get_at_index(element)
            if self.count(compare_element) != second_bag.count(compare_element):
                return False
        return True


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # add example 1
    # bag = Bag()
    # print(bag)
    # values = [10, 20, 30, 10, 20, 30]
    # for value in values:
    #     bag.add(value)
    # print(bag)

    # # remove example 1
    # bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(bag)
    # print(bag.remove(7), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)

    # # count example 1
    # bag = Bag([1, 2, 3, 1, 2, 2])
    # print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    # # clear example 1
    # bag = Bag([1, 2, 3, 1, 2, 3])
    # print(bag)
    # bag.clear()
    # print(bag)

    # # size example 1
    # bag = Bag([10, 20, 30, 40])
    # print(bag.size(), bag.remove(30), bag.size())
    # bag.clear()
    # print(bag.size())

    # # equal example 1
    #bag1 = Bag([1, 2, 3, 4, 5, 6])
    #bag2 = Bag([6, 5, 4, 3, 2, 1])
    #bag3 = Bag([1, 2, 3, 4, 5])
    #bag_empty = Bag()
    #
    #print(bag1, bag2, bag3, bag_empty, sep="\n")
    #print(bag1.equal(bag2), bag2.equal(bag1))
    #print(bag1.equal(bag3), bag3.equal(bag1))
    #print(bag2.equal(bag3), bag3.equal(bag2))
    #print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    #print(bag_empty.equal(bag_empty))
    #print(bag1, bag2, bag3, bag_empty, sep="\n")
