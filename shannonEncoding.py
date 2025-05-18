# Shannon coding essentially sorts the elements of a file from most to least likely to appear.
import math
from collections import Counter


"""
Sort symbols by prob
Symbol	Frequency	Probability
  A	           5	0.5
  B	           2	0.2
  C	           2	0.2
  D	           1	0.1

| Symbol | P (probability) | F (cumulative) |
| ------ | --------------- | -------------- |
| A      | 0.5             | 0              |
| B      | 0.2             | 0.5            |
| C      | 0.2             | 0.7            |
| D      | 0.1             | 0.9            |

L = ⌈-log₂(P)⌉

| Symbol | P   | F   | L (bits) | Code (F in binary, L bits) |
| ------ | --- | --- | -------- | -------------------------- |
| A      | 0.5 | 0   | 1        | `0`                        |
| B      | 0.2 | 0.5 | 3        | `100`                      |
| C      | 0.2 | 0.7 | 3        | `101`                      |
| D      | 0.1 | 0.9 | 4        | `1110`                     |

Example: Encode "ABCD"
    A → 0
    B → 100
    C → 101
    D → 1110

Encoded = 0 100 101 1110 → 01001011110
"""


def fractional_to_binary(fraction, length):
    binary_code = ""
    frac = fraction
    for _ in range(length):
        frac *= 2
        bit = int(frac)
        frac -= bit
        binary_code += str(bit)
    return binary_code


def shannon_encoding(string: str):
    freq = Counter(string)
    total = sum(freq.values())
    prob_lst = [(sym, count / total) for sym, count in freq.items()]
    prob_lst.sort(key=lambda x: x[1], reverse=True)

    cumulative_sum = 0
    cumulative_probabilities = []
    for symbol, prob in prob_lst:
        cumulative_probabilities.append((symbol, prob, cumulative_sum))
        cumulative_sum += prob

    # Don't round here to keep precision
    codes = {}
    for symbol, prob, cum_prob in cumulative_probabilities:
        L = math.ceil(-math.log2(prob))
        code = fractional_to_binary(cum_prob, L)
        codes[symbol] = code

    encoded_str = "".join(codes[ch] for ch in string)
    return codes, encoded_str


def shannon_decode(encoded: str, codes):
    inverse_codes = {v: k for k, v in codes.items()}
    decoded = ""
    current_bits = ""
    for bit in encoded:
        current_bits += bit
        if current_bits in inverse_codes:
            decoded += inverse_codes[current_bits]
            current_bits = ""
    return decoded


def main():
    string = "AAAAABBCCD"
    codes, encoded = shannon_encoding(string)
    print("Symbol codes:", codes)
    print("Encoded string:", encoded)
    decoded = shannon_decode(encoded, codes)
    print("Decoded string:", decoded)


main()
