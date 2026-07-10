# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
        self.length = 0 # Initialize length here

    def push(self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)
        self.length += 1 # Increment length

    def pop(self):
        if self.length == 0:
            return -1
        x = self.q[self.front]
        self.front += 1
        self.length -= 1 # Decrement length
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x

    def getFront(self):
        if self.length == 0:
            return -1
        return self.q[self.front]

    def size(self):
        return self.length
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root is None:
            return ans
        queue = Queue()
        queue.push(root)
        ans.append(root.val)

        while queue.size() > 0:

            l = queue.size()
            level = []
            for i in range(l):
                front = queue.pop()
                if front.left!=None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right!=None:
                    queue.push(front.right)
                    level.append(front.right.val)
                    
            if len(level)>0:
                ans.append(level[-1])

        
        return ans
        