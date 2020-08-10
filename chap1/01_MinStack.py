class MinStack:
    def __init__(self):
        self.stack=[]     #初始化数据栈
        self.minStack=[]  #初始化最小数据栈，栈顶元素为数据栈的最小值
        self.size=0       #记录栈中元素个数


    def push(self, x: int) -> None:
        if self.size==0:
            self.minStack.append(x)
        else:
            curMin=self.minStack[-1]
            if x<=curMin:
                self.minStack.append(x)
            else:
                self.minStack.append(curMin)
        self.stack.append(x)
        self.size +=1


    def pop(self) -> None:
        if self.size==0:
            return None
        else:
            self.stack.pop()
            self.minStack.pop()
            self.size -=1

    def top(self) -> int:
        if self.size==0:
            return None
        else:
            return self.stack[-1]


    def getMin(self) -> int:
        if self.size==0:
            return None
        else:
            return self.minStack[-1]