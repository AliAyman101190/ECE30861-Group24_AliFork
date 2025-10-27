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

from convert_boolean import convertToBoolean


class TestConvertToBoolean(unittest.TestCase):
    def test_convertToBoolean(self):
        # Two required subtests:
        subtests = {
            "Normal Input Test": None,
            "Non-Integer Input Test": None,
        }

        # --- Normal Input Test ---
        with self.subTest(key="Normal Input Test"):
            # Example from the prompt: 135 with size 10
            expected = [False, False, True, False, False, False, False, True, True, True]
            self.assertEqual(convertToBoolean(135, 10), expected)

            # Another prompt example: 9 with size 3 -> expands to 4 bits
            expected_9 = [True, False, False, True]
            self.assertEqual(convertToBoolean(9, 3), expected_9)

        # --- Non-Integer Input Test ---
        with self.subTest(key="Non-Integer Input Test"):
            with self.assertRaises(ValueError):
                convertToBoolean(9.5, 4)   # invalid positive decimal for num


# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
    # Add a TextTestRunner that writes to testrun.txt
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestConvertToBoolean)
    testrun_path = os.path.join(PROJECT_ROOT, "testrun.txt")
    with open(testrun_path, "w") as fh:
        runner = unittest.TextTestRunner(stream=fh, verbosity=2)
        runner.run(suite)
    print(f"Test results written to {testrun_path}")
