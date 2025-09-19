'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        visited = set()
        
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr=curr.next
        return False
        e
