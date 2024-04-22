"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-04-07"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
# Use any appropriate data structure here.
from List_array import List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(List())

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates an integer key from a food key (name and origin).
        Use: h = hash(food)
        -------------------------------------------------------
        Returns:
            returns
            value - the total of the characters in the name string
            (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.name:
            value = value + ord(c)
        value *= self.origin
        return value

    def _hashfunction(self, element):
        """
        -------------------------------------------------------
        Returns the index in the table where the element can
        be inserted. 
        Use: list = self._hashfunction(element)
        -------------------------------------------------------
        Returns:
        index - the position of the element in self._table
        -------------------------------------------------------
        """
        key = hash(element)  # returns an integer key for the element
        return key % len(self._table)

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        # your code here
        index = self._hashfunction(key)
        slot = self._table[index]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        # your code here

        index = self._hashfunction(value)
        slot_list = self._table[index]
        if value in slot_list:
            # Do not insert data if already in hash set.
            inserted = False
        else:
            inserted = True
            slot_list.insert(0, value)
            self._count += 1

            # Check the load factor and rehash if necessary.
            if self._count > (Hash_Set._LOAD_FACTOR * self._capacity):
                self._rehash()

        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        index = hash(key) % self._capacity
        slot = self._table[index]
        value = None

        for item in slot:
            if item[0] == key:
                value = item[1]  # Return the value associated with the key

        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        value = None
        slot = self._find_slot(key)
        if key in slot:
            slot.remove(key)
            self._count -= 1
            value = key

        return value

        # index = hash(key) % self._capacity
        # original_index = index

    #     return self._remove_recursively(key, index, original_index)
    #
    # def _remove_recursively(self, key, index, original_index):
    #     """Recursive function to remove the key."""
    #     if key in self._table[index]:
    #         self._table[index].remove(key)
    #         self._count -= 1
    #         return key
    #     elif index == original_index:
    #         return None
    #     else:
    #         next_index = (index + 1) % self._capacity
    #         return self._remove_recursively(key, next_index, original_index)

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        # Copy the current data to a temporary slot.
        temp_table = self._table

        # Increase the number of slots and define them.
        self._capacity = self._capacity * 2 + 1
        self._table = []

        for _ in range(self._capacity):
            self._table.append(List())

        # Copy old data to new slots.
        while len(temp_table) > 0:
            old_slot = temp_table.pop(0)

            while not old_slot.is_empty():
                value = old_slot.remove_front()
                slot = self._find_slot(value)
                slot.insert(0, value)
        return

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Hash_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a hash set (Hash_Set)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        # your code here
        return

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        print(f"{self._capacity} slots")

        for i in range(len(self._table)):
            print(SEP)
            print(f"Slot {i}")
            slot = self._table[i]
            print()

            for v in slot:
                print(v)

        print(SEP)
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
