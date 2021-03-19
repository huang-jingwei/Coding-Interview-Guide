class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1

        fibArray = [0] * (N + 1)
        fibArray[0] = 0
        fibArray[1] = 1
        for index in range(2, len(fibArray)):
            fibArray[index] = fibArray[index - 1] + fibArray[index - 2]
        return fibArray[-1]