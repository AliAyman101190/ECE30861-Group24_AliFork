#######################################################
# Author: Ali Omar
# email: omar13@purdue.edu
# ID: ee364b20
# Date: 10/26/2025
#######################################################

import os # List of module import statements
import sys # Each one on a line
import unittest

#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################

# Make src importable regardless of where tests are run from
TESTS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(TESTS_DIR, os.pardir))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from streak_product import getStreakProduct


class TestGetStreakProduct(unittest.TestCase):
    def test_getStreakProduct(self):
        # A sequence not less than 20 digits, and maxSize above 5
        seq = "54789654321687984321"
        max_size = 6

        # Three subtests (keys are the product values)
        cases = {
            288: ["984", "32168"],
            140: ["547"],
            17:  [],
        }

        for prod, expected in cases.items():
            with self.subTest(product=prod):
                actual = getStreakProduct(seq, max_size, prod)
                self.assertEqual(expected, actual)


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
    # Add a TextTestRunner that writes to testrun.txt (per instructions)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGetStreakProduct)
    testrun_path = os.path.join(PROJECT_ROOT, "testrun.txt")
    with open(testrun_path, "w") as fh:
        runner = unittest.TextTestRunner(stream=fh, verbosity=2)
        runner.run(suite)
    print(f"Test results written to {testrun_path}")
