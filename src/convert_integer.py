#######################################################
# Author: Ali Omar
# email: omar13@purdue.edu
# ID: ee364b20
# Date: 10/26/2025
#######################################################

import os # List of module import statements
import sys # Each one on a line
from typing import Optional

#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################

def convertToInteger(boolList) -> Optional[int]:
    """
    Convert a list of booleans (MSB -> LSB) to its integer value.
    Returns None if:
      - the input is not a list,
      - any element is not a bool,
      - the list is empty.
    """

    print("hello") #making a change to test github actions
    if not isinstance(boolList, list):
        return None
    if len(boolList) == 0:
        return None
    if not all(isinstance(x, bool) for x in boolList):
        return None

    # 'True' -> '1', 'False' -> '0', MSB first
    bit_str = "".join('1' if b else '0' for b in boolList)
    return int(bit_str, 2)


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":

    # Write anything here to test your code.
    z = convertToInteger([True, False, False, False, False, True, True, True])
    print(z)
