class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return None
        else:
            a = self.stack[-1]
            self.stack.pop()
            return a


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            a = self.stack[-1]
            return a


    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()