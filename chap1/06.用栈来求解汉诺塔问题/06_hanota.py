class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        n = len(A)
        self.move(n, A, B, C)

    # 定义move 函数移动汉诺塔
    def move(self, n, A, B, C):
        if n == 1:
            C.append(A.pop())
            return
        else:
            self.move(n - 1, A, C, B)  # 将A上面n-1个通过C移到B
            C.append(A[-1])  # 将A最后一个移到C
            A.pop()  # 这时，A空了

            # 这样以来我们又回到了最开始的问题，把B上面剩下的n-1个盘子通过A拿到C上面去
            # 盘子变了，但是只是现在B和A互换了一下功能而已
            self.move(n - 1, B, A, C)  # 将B上面n-1个通过空的A移到C