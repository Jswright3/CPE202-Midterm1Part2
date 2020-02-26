"""
Problem 6
Midterm 1
John Wright
"""
import unittest
from problem7 import *

class MyTest(unittest.TestCase):
   def test_remove_multiple(self):
      self.assertRaises(ValueError, remove_multiple, Node(3), None)
      self.assertEqual(remove_multiple(None, 3), None)
      int_list = Node(0, Node(1, Node(2, Node(2, Node(1, Node(4))))))
      self.assertEqual(remove_multiple(int_list, 2), Node(0, Node(1, Node(1, Node(4)))))
      self.assertEqual(remove_multiple(int_list, 1), Node(0, Node(2, Node(2, Node(4)))))
      int_list2 = Node(8, Node(8, Node(8, Node(7, Node(7, Node(6))))))
      self.assertEqual(remove_multiple(int_list2, 8), Node(7, Node(7, Node(6))))
      self.assertEqual(remove_multiple(int_list2, 6), Node(8, Node(8, Node(8, Node(7, Node(7))))))

if __name__ == '__main__':
    unittest.main()
