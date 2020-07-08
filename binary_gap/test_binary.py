import unittest
import binary


class TestBinaryGap (unittest.TestCase):
    def testgap(self):
        self.assertEqual(binary.max_gap(32),0)
        self.assertEqual(binary.max_gap(647),4)
        self.assertEqual(binary.max_gap(1041),5)
        self.assertEqual(binary.max_gap(483),3)