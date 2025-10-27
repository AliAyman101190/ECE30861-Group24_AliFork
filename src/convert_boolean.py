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

def convertToBoolean(num: int, size: int) -> List[bool]:
    """
    Return a list of booleans representing the binary of `num` (MSB -> LSB),
    with a minimum length of `size` (pad with leading False as needed).

    Raises:
        ValueError: if `num` or `size` is not an integer.
    """
    if not isinstance(num, int) or not isinstance(size, int):
        raise ValueError("Both num and size must be integers.")

    # Binary for 0 is a single 0 bit.
    bits = "0" if num == 0 else bin(num)[2:]

    # Ensure minimum length of `size` with leading zeros.
    width = max(size, len(bits))
    padded = bits.zfill(width)

    # Map '1' -> True, '0' -> False (MSB first).
    return [ch == "1" for ch in padded]


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":

    # Write anything here to test your code.
    z = convertToBoolean(135, 10)
    print(z)
