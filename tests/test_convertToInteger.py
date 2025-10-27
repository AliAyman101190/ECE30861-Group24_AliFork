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

from convert_integer import convertToInteger


class TestConvertToInteger(unittest.TestCase):
    def test_convertToInteger(self):
        # ---- Normal Input Test ----
        with self.subTest(key="Normal Input Test"):
            # Example 1 from prompt -> 135
            bList = [True, False, False, False, False, True, True, True]
            self.assertEqual(convertToInteger(bList), 135)
            # Example 2 from prompt -> 9
            bList2 = [False, False, True, False, False, True]
            self.assertEqual(convertToInteger(bList2), 9)

        # ---- Non-List Test ----
        with self.subTest(key="Non-List Test"):
            self.assertIsNone(convertToInteger("not a list"))

        # ---- Invalid List Test ----
        with self.subTest(key="Invalid List Test"):
            self.assertIsNone(convertToInteger([True, 1, False]))

        # ---- Empty List Test ----
        with self.subTest(key="Empty List Test"):
            self.assertIsNone(convertToInteger([]))


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
    # Add a TextTestRunner that writes to testrun.txt
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestConvertToInteger)
    testrun_path = os.path.join(PROJECT_ROOT, "testrun.txt")
    with open(testrun_path, "w") as fh:
        runner = unittest.TextTestRunner(stream=fh, verbosity=2)
        runner.run(suite)
    print(f"Test results written to {testrun_path}")
