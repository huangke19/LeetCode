class Empty(Exception):
    '''Error attempting to access an element from an empty container.'''
    pass


class ArrayStack:
    """ LIFO Stack implemented by a Python list """
    
    def __init__(self):
        '''Create an empty stack.'''
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.items[-1]
    
    def size(self):
        return len(self.items)


class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t1 = ArrayStack()
        self.t2 = ArrayStack()
    
    def push(self, x=None):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.t1.push(x)
    
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.t1.isEmpty():
            r = self.t1.pop()
            self.t2.push(r)
        t = self.t2.pop()
        while not self.t2.isEmpty():
            self.t1.push(self.t2.pop())
        return t
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while not self.t1.isEmpty():
            r = self.t1.pop()
            self.t2.push(r)
        t = self.t2.top()
        while not self.t2.isEmpty():
            self.t1.push(self.t2.pop())
        return t
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.t1.isEmpty()


myqueue = MyQueue()
print(myqueue)
myqueue.push(1)
myqueue.push(2)
print(myqueue.peek())
myqueue.push(3)
print(myqueue.peek())
