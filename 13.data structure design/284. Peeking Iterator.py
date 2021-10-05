# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.has_next = self.iter.hasNext()
        if self.has_next:
            self.nextnum = self.iter.next()

    def peek(self):
        return self.nextnum

    def next(self):
        temp = self.nextnum
        self.has_next = self.iter.hasNext()
        if self.has_next:
            self.nextnum = self.iter.next()
        return temp
        
    def hasNext(self):
        return self.has_next
        
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
