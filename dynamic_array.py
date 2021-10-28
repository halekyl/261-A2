# Course: CS261 - Data Structures
# Student Name: Kylee Hale
# Assignment: #2 Part 1 Dynamic Array
# Description: Program that implements a Dynamic Array class.


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/"+ str(self.capacity)
        out += " " + str(self.data[:self.size])
        return out

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the underlying storage for the array elements.
        Called by other class methods: append(), remove_at_index(), and insert_at_index() to
        manage the capacity of the underlying storage data structure.
        """
        # handles negative integers not accepted and new capacity being smaller than number of elements in array.
        if new_capacity <= 0 or new_capacity < self.size:
            return
            # to make a new array with new capacity
        new_data = [None] * new_capacity
        # to copy old array data over to new array
        for element in range(self.size):
            new_data[element] = self.data[element]
        self.data = new_data
        self.capacity = new_capacity
        return

    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array. If the internal storage of the dynamic array
        is already full, this method first doubles the capacity by calling resize() then adds new value.
        """
        # handles case where the storage is full
        if self.size >= self.capacity:
            self.resize(self.capacity * 2)
        # add new value
        self.data[self.size] = value
        self.size += 1
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the dynamic array. Index 0 refers to beginning of array.
        If the array contains N elements, valid indices for this method are [0, N] inclusive.
        """
        # handles invalid index
        if index < 0 or index > self.size:
            raise DynamicArrayException()
        # handles if array storage is full
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        # to shift elements over to insert
        for element in range(self.size, index, - 1):
            self.data[element] = self.data[element - 1]
        self.data[index] = value
        self.size += 1
        return

    def get_at_index(self, index: int) -> object:
        """
        Returns value from the specific index in the dynamic array.
        If the array contains N elements, valid indices for this method are [0, N - 1] inclusive.
        """
        # handles invalid index or returns value
        if not 0 <= index < self.size:
            raise DynamicArrayException()
        return self.data[index]


    def remove_at_index(self, index: int) -> None:
        """
        Removes the element from the dynamic array given its index. Index 0 refers to beginning of array.
        If the array contains N elements, valid indices for this method are [0, N - 1] inclusive.
        When the number of elements stored in the array (before removal) is STRICTLY LESS than ¼ of it current
        capacity, the capacity must be reduced to TWICE the number of current elements. At no time the capacity
        can be reduced to less than 10 elements, regardless of the actual number of elements in the array.
        """
        # handles invalid index
        if index < 0:
            raise DynamicArrayException
        if index > self.size - 1:
            raise DynamicArrayException

        # handles when number of elements in array is less than 1/4 of capacity
        if self.size < (self.capacity / 4) and self.size * 2 >= 10:
            self.resize(self.size * 2)
        # handles capacity cannot be less than 10
        elif self.size < (self.capacity / 4) and self.size * 2 < 10:
            self.resize(10)
        # to shift elements over to remove
        for element in range(index, self.size - 1, 1):
            self.data[element] = self.data[element + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return

    def is_empty(self) -> bool:
        """
         Returns True if there are no elements in the array, Otherwise returns False.
        """
        if self.data[0] == None:
            return True
        return False


    def length(self) -> int:
        """
        Returns the number of elements currently stored in the array.
        """
        length = self.size
        return length

    def slice(self, start_index: int, quantity: int) -> object:
        """
        Returns a new Dynamic Array object that contains the requested number of elements from the
        original array starting with the element located at the requested start index.
        """
        section_slice_array = DynamicArray()

        # handles invalid start index
        if start_index < 0:
            raise DynamicArrayException()
        if start_index >= self.size:
            raise DynamicArrayException()
        # handles too few elements (between start index and end of array) to make requested slice size.
        if start_index + quantity > self.size:
            raise DynamicArrayException()
        if quantity > self.size:
            raise DynamicArrayException()

        for element in range(start_index, start_index + quantity):
            section_slice_array.append(self.data[element])
        return section_slice_array

    def reverse(self) -> None:
        """
        Reverses elements stored in the array, reversal is done "in place" without temporary storage array.
        """
        number_of_swaps = self.size // 2
        for element in range(number_of_swaps):
            # to swap elements in place
            element_placeholder = self.data[element]
            self.data[element] = self.data[self.size - 1 - element]
            self.data[self.size - 1 - element] = element_placeholder
        return

    def sort(self) -> None:
        """
        Sorts the content of the current array in non-descending order.
        """
        length = self.size
        for element in range(length):
            a_element = self.data[element]
            b_element = element
            for comparable_element in range(element + 1, length):
                if a_element > self.data[comparable_element]:
                    a_element = self.data[comparable_element]
                    b_element = comparable_element
            if element != comparable_element:
                self.data[b_element] = self.data[element]
                self.data[element] = a_element
        return

    def merge(self, another_list: object) -> None:
        """
        Takes as a parameter another Dynamic Array object and appends all elements from the second array
        to the current one, in the same order as they are stored in the second array.
        """
        for element in range(another_list.size):
            self.append(another_list.data[element])
        return



# BASIC TESTING
if __name__ == "__main__":
    pass

    # # resize - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.resize(10)
    # print(da.size, da.capacity, da.data)
    # da.resize(2)
    # print(da.size, da.capacity, da.data)
    # da.resize(0)
    # print(da.size, da.capacity, da.data)

    # # resize - example 2
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # # append - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)

    # # append - example 2
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    # # append - example 3
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.size)
    # print(da.capacity)

    # # insert_at_index - example 1
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # # insert_at_index example 2
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)

    # # insert at index example 3
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Can not insert value", value, "at index", index)
    # print(da)

    # # get_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50])
    # print(da)
    # for i in range(4, -1, -1):
    #     print(da.get_at_index(i))

    # # get_at_index example 2
    # da = DynamicArray([100, 200, 300, 400, 500])
    # print(da)
    # for i in range(-1, 7):
    #     try:
    #         print("Index", i, ": value", da.get_at_index(i))
    #     except Exception as e:
    #         print("Index", i, ": exception occured")

    # # remove_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)

    # # remove_at_index - example 2
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.size, da.capacity)
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)

    # # remove_at_index - example 3
    # da = DynamicArray()
    # print(da.size, da.capacity)
    # [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                      # step 3 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 4 - remove 1 element
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 6 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 7 - remove 1 element
    # print(da.size, da.capacity)
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.size, da.capacity, end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.size, da.capacity)

    # # is_empty - example 1
    # da = DynamicArray()
    # print(da.is_empty(), da)
    # da.append(100)
    # print(da.is_empty(), da)
    # da.remove_at_index(0)
    # print(da.is_empty(), da)

    # # length - example 1
    # da = DynamicArray()
    # print(da.length())
    # for i in range(10000):
    #     da.append(i)
    # print(da.length())
    # for i in range(9999, 5000, -1):
    #     da.remove_at_index(i)
    # print(da.length())

    # # slice example 1
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")

    # slice example 2
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOUCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")

    # # merge example 1
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)

    # merge example 2
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)

    # # reverse example 1
    # da = DynamicArray([4, 5, 6, 7, 8, 9])
    # print(da)
    # da.reverse()
    # print(da)
    # da.reverse()
    # print(da)

    # # reverse example 2
    # da = DynamicArray()
    # da.reverse()
    # print(da)
    # da.append(100)
    # da.reverse()
    # print(da)

    # # sort example 1
    # da = DynamicArray([1, 10, 2, 20, 3, 30, 4, 40, 5])
    # print(da)
    # da.sort()
    # print(da)
