import Binary_Search
import unittest


class TestBinarySearch(unittest.TestCase):  # Testing our binary search without slicing
    def setUp(self) -> None:
        self.testlist = [0, 1, 3, 7, 11, 20, 28]

    def test(self):
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 0))
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 1))
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 3))
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 7))
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 11))  # Testing whole
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 20))  # list
        self.assertTrue(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 28))
        self.assertFalse(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 4))
        self.assertFalse(Binary_Search.binary_search_no_slice(self.testlist, 0, len(self.testlist), 47))