"""
-------------------------------------------------------
Morse Code Definitions and Functions
-------------------------------------------------------
Author:  Khamosh Mehta
ID:      169088625
Email:   meht8625@wlu.ca
__updated__ = "2024-04-03"
-------------------------------------------------------
"""
from BST_linked import BST
# In order by letters.
DATA1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..-'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

# In order by splitting.
DATA2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..-'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))

# In order by popularity.
DATA3 = (('E', '.'), ('T', '-'), ('A', '.-'),
         ('O', '---'), ('I', '..'), ('N', '-.'),
         ('S', '...'), ('H', '....'), ('R', '.-.'),
         ('D', '-..'), ('L', '.-..'), ('U', '..-'),
         ('C', '-.-.'), ('M', '--'), ('P', '.--.'),
         ('F', '..-.'), ('Y', '-.--'), ('W', '.--'),
         ('G', '--.'), ('B', '-...'), ('V', '...-'),
         ('K', '-.-'), ('J', '.---'), ('X', '-..-'),
         ('Z', '--..'), ('Q', '--.-'))


class ByLetter:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by letter attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByLetter object.
        Use: var = ByLetter(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByLetter object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their letters match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if letters match, False otherwise (boolean)
        -------------------------------------------------------
        """

        result = False

        if self.letter == target.letter:
            result = True

        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        # Your code here

        result = False

        if self.letter < target.letter:
            result = True
        return result

    # def __gt__(self, target):
    #     """
    #     -------------------------------------------------------
    #     Determines if source comes after target.
    #     Use: source > target
    #     -------------------------------------------------------
    #     Parameters:
    #         target - ByLetter to compare source to (ByLetter)
    #     Returns:
    #         result - True if source precedes target,
    #           False otherwise (boolean)
    #     -------------------------------------------------------
    #     """
    #     result = False
    #
    #     if self.letter > target.letter:
    #         result = True
    #     return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByLetter to compare source to (ByLetter)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.letter <= target.letter

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByLetter data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByLetter (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.letter, self.code)


class ByCode:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by code attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByCode object.
        Use: var = ByCode(letter, code)
        -------------------------------------------------------
        Parameters:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Returns:
            A ByCode object.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares source against target for equality.
        Object are equal if their codes match.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if codes match, False otherwise (boolean)
        -------------------------------------------------------
        """
        # Your code here
        result = False
        if self.code == target.code:
            result = True

        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if source comes before target.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        # Your code here

        return self.code < target.code

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if source precedes or is or equal to target.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - ByCode to compare source to (ByCode)
        Returns:
            result - True if source precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        # Your code here

        return self.code <= target.code

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByCode data.
        Use: print(source)
        Use: string = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of ByCode (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.code, self.letter)


def fill_letter_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByLetter Morse code letter/code pairs
    (Function must convert contents of values to ByLetter objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """
    for letter, code in values:  # Iterate over the list of tuples
        by_letter_obj = ByLetter(letter, code)     # Create a ByLetter object
        bst.insert(by_letter_obj)     # Insert the ByLetter object into the bst

    return


def fill_code_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByCode Morse code letter/code pairs.
    (Function must convert contents of values to ByCode objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """
    # Your code here
    for letter, code in values:
        by_code_obj = ByCode(letter, code)
        bst.insert(by_code_obj)
    return


def encode_morse(bst, text):
    """
    -------------------------------------------------------
    Converts English text to Morse code
    Use: code = encode_morse(bst, text)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by letter (BST)
        text - English text to convert (str)
    Returns:
        result - Morse code version of text (str)
    -------------------------------------------------------
    """
    # Your code here
    result = ""

    # Iterate through each individual character in text
    for char in text:
        # Check if the character is not a space
        if char != " ":
            # Check if the character matches with the letter in DATA1 tuples list,
            # If so, return the corresponding morse code.
            m_code = ""
            for letter, code in DATA1:
                if letter == char.upper():
                    m_code = code
                    break
            # Add the morse code to the result string
            result += m_code
            # Only add space if the morse code exists for the correspondonng letter
            if m_code:
                result += " "
        else:
            result += ' '
    # encoded_message = []
    #
    # for char in text:
    #     if char != " ":
    #         morse_code = None
    #         for letter, code in DATA1:
    #             if letter == char.upper():
    #                 morse_code = code
    #                 break
    #         by_letter_obj = ByLetter(char, morse_code)
    #         morse_code_bst = bst.retrieve(by_letter_obj)
    #         if morse_code_bst:
    #             encoded_message.append(morse_code_bst)
    #         else:
    #             encoded_message.append('')
    #     else:
    #         encoded_message.append(' ')
    #
    # result = " ".join(str(v) for v in encoded_message)
    return result.strip()  # Remove any trailing spaces within the string.


def decode_morse(bst, code):
    """
    -------------------------------------------------------
    Converts Morse code to English text
    Use: text = decode_morse(bst, code)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by code (BST)
        code - Morse code to convert (str)
    Returns:
        result - English version of code (str)
    -------------------------------------------------------
    """
    result = ""
    morse_code_parts = code.split(' ')

    for part in morse_code_parts:
        if part != " ":
            letter = None
            for _, code in DATA1:
                if code == part:
                    letter = _
                    break
            if letter:
                result += letter
        else:
            result += ' '
    # Your code here
    # decoded_message = []
    # code_list = code.split()
    #
    # for m_code in code_list:
    #     # Go through DATA1 to identify the corresponding letter associated with the code
    #     for letter, d_code in DATA1:
    #         val = ""
    #         if d_code == m_code:
    #             val = letter
    #             break
    #
    #     # Create a ByCode object to compare the key with that in the bst
    #     by_code_obj = ByCode(letter, m_code)
    #     decoded_morse_bst = bst.retrieve(by_code_obj)
    #
    #     # Add the corresponding letter to an empty list.
    #     if decoded_morse_bst:
    #         decoded_message.append(decoded_morse_bst)
    #     else:
    #         decoded_message.append('')
    #
    # result = ' '.join(str(v) for v in decoded_message)
    return result


# def draw_tree(data):
#     """
#     Draw a tree based on the provided data tuples.
#     """
#     # Initialize an empty string to store the tree representation
#     tree_representation = ""
#
#     # Assume the maximum depth of the tree
#     # Adjust this based on the expected depth of the tree
#     max_depth = max(ord(letter) - ord('A') for letter, _ in data) + 1
#
#     # Create a list to store nodes at each level of the tree
#     levels = [[] for _ in range(max_depth)]
#
#     # Populate levels with nodes based on the provided data tuples
#     for letter, _ in data:
#         # Calculate the depth based on ASCII values
#         depth = ord(letter) - ord('A')
#         levels[depth].append(letter)
#
#     # Build the tree representation
#     for level in levels:
#         if not level:
#             continue
#         tree_representation += " " * \
#             (max_depth - len(level))  # Add indentation
#         # Add nodes at the current level
#         tree_representation += " ".join(level)
#         tree_representation += "\n"  # Move to the next line
#
#     # Print or return the tree representation
#     print(tree_representation)
#
#
# def draw_tree_2(data):
#     """
#     Draw a tree with each letter as a node.
#     """
#     # Sort the data tuples based on the letters
#     sorted_data = sorted(data)
#
#     # Find the maximum length of the letters
#     max_length = max(len(letter) for letter, _ in sorted_data)
#
#     # Calculate the maximum number of spaces needed for indentation
#     max_spaces = max_length // 2
#
#     # Print each letter with appropriate indentation
#     for letter, _ in sorted_data:
#         spaces_before = max_spaces - (ord(letter) - ord('A'))
#         spaces_after = max_spaces - (ord('Z') - ord(letter))
#         print(" " * spaces_before + letter + " " * spaces_after)
#
#
# draw_tree(DATA1)
# draw_tree_2(DATA1)
