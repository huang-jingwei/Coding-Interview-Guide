class SortedStack:

    def __init__(self):
        self.sortedStack = []     # 排序好的数据栈
        self.helpStack = []       # 辅助栈
        self.size = 0             # 记录栈结构中元素的个数

    def push(self, val: int) -> None:

        if self.size == 0:
            self.sortedStack.append(val)
            self.size += 1
        else:
            while len(self.sortedStack) > 0 and self.sortedStack[-1] > val:
                self.helpStack.append(self.sortedStack.pop())
            self.sortedStack.append(val)
            while len(self.helpStack) > 0:
                self.sortedStack.append(self.helpStack.pop())
            self.size += 1

    # 这里的pop函数是弹出栈底元素
    def pop(self) -> None:
        if self.size == 0:
            return None
        else:
            while len(self.sortedStack) > 1:
                self.helpStack.append(self.sortedStack.pop())
            peekValue = self.sortedStack.pop()
            while len(self.helpStack) > 0:
                self.sortedStack.append(self.helpStack.pop())
            self.size -= 1
            return peekValue

    def peek(self) -> int:
        # print(self.sortedStack)
        if self.size == 0:
            return -1
        else:
            while len(self.sortedStack) > 1:
                self.helpStack.append(self.sortedStack.pop())
            peekValue = self.sortedStack.pop()
            self.helpStack.append(peekValue)
            while len(self.helpStack) > 0:
                self.sortedStack.append(self.helpStack.pop())
            return peekValue

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False