class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]        #用栈结够来模拟队列结构
        self.stack=[]        #辅助数据栈
        self.size=0          #队列中的元素个数


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        self.size +=1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size==0:
            return None
        else:
            while len(self.queue)>1:
                self.stack.append(self.queue.pop())
            popValue=self.queue.pop()
            while len(self.stack)>=1:
                self.queue.append(self.stack.pop())
            self.size -=1
            return popValue



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.size==0:
            return None
        else:
            while len(self.queue)>1:
                self.stack.append(self.queue.pop())
            peekValue=self.queue.pop()
            self.stack.append(peekValue)
            while len(self.stack)>=1:
                self.queue.append(self.stack.pop())
            return peekValue


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size==0:
            return True
        else:
            return False