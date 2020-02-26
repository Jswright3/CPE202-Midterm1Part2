"""
Problem 6
Midterm 1
John Wright
"""
class Node:
   """IntList is one of None or Node.
   Attributes:
      val (int) : integer value
      next (Node) : Pointer to the next node of the intList
      prev (Node) : Pointer to the previous node of the intList
   """
   def __init__(self, val, nxt=None, prev=None):
      self.val = val
      self.next = nxt
      self.prev = prev

   def __repr__(self):
      pass

   def __eq__(self, other):
      if self.val == other.val and self.next == other.next and self.prev == other.prev:
         return True
      return False

def remove_multiple(int_list, target):
   """removes all instances of target in list recursively
   Arguments:
      int_list (Node)
      target (int):
   returns:
      (Node)
   """
   if int_list is None:
      return None
   if target is None:
      raise ValueError
   if int_list.val == target:
      return remove_multiple(int_list.next, target)
   return Node(int_list.val, remove_multiple(int_list.next, target))
