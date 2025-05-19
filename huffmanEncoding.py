# Everything about huffman encoding
"""
Algorithm
    Convert text to zero one encoding
    Take two smalesst frequencies, make binary tree where they are siblings.
    new node -> sum of two freq, then take next two small freq
    Left branch = 0, Right branch = 1
To prevent ambiguity

Steps-:
Build min heap to select two least freq count char
Convert to code recurse the tree.
Encode the input text, stored this padding information, in 8 bits, in the beginning of the resultant code.
Write the result to an output binary file, which will be our compressed file.
"aabacabad"


"""

"""
Build a Min-Heap Tree
    Each node represents a character and its frequency.
    Combine the two least frequent nodes into a new node whose frequency is the sum.
    Repeat until you have one tree.

Step 1: c(1), d(1) → combine → cd(2)
Step 2: cd(2), b(2) → combine → bcd(4)
Step 3: bcd(4), a(5) → combine → root(9)
"""


from collections import Counter

import heapq

string = "aabacabad"
freq = Counter(string)
heapq.heapify(string)
print(string)


# class HuffmanTree:
#     def __init__(self) -> None:
#         self.char = ""
#         self.freq = int

# def two_least_freq():
# logic for combining two least freq nodes into new node whose freq = sum
