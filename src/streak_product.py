#######################################################
# Author: Ali Omar
# email: omar13@purdue.edu
# ID: ee364b20
# Date: 10/26/2025
#######################################################

import os # List of module import statements
import sys # Each one on a line
from typing import List

#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################

def getStreakProduct(sequence: str, maxSize: int, product: int) -> List[str]:
    """
    Search the string `sequence` (digits) for all contiguous sub-sequences whose
    size is between 2 and `maxSize` (inclusive) and whose digital product equals `product`.
    Return all matches in order of appearance; overlaps are allowed.
    """
    results: List[str] = []
    if not sequence or maxSize < 2:
        return results

    n = len(sequence)
    limit = min(maxSize, n)

    # Convert to ints once
    digits = [int(ch) for ch in sequence]

    for size in range(2, limit + 1):
        for start in range(0, n - size + 1):
            prod = 1
            for k in range(size):
                prod *= digits[start + k]
            if prod == product:
                results.append(sequence[start:start + size])

    return results


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":

    # Write anything here to test your code.
    demo = getStreakProduct("14822", 3, 32)
    print(demo)
