# coding=utf-8

# 基于Python中list的栈的实现
# 栈的抽象数据类型的实现是创建一个新类
# 栈的操作实现为类方法，
# 栈的操作包括判断是否为空，入栈，出栈，栈顶元素，栈的深度。

#   ADT Stack
#       Stack(self)       创建空栈
#       isEmpty(self)     判断栈是否为空 
#       push(self, item)  将item压入栈中，称为压入
#       pop(self)         删除栈里最后压的元素，称为弹出
#       top(self)         取得栈里最后压入的元素，不删除 
#       size(self)        取得栈里元素的个数，或者叫深度

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

# 以下为验证这个刚实现的栈的运行


# s = ArrayStack()
#
# print(s.isEmpty)
#
# s.push(4)
#
# s.push('dog')
#
# print(s.top())
#
# s.push(True)
#
# print(s.size())
#
# print(s.isEmpty())
#
# s.push(8.4)
#
# print(s.pop())
#
# print(s.pop())
#
# print(s.size())
