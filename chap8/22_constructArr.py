class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        listLength = len(a)
        if listLength == 0:
            return []
        elif listLength == 1:
            return a

        # left[index]:代表A[0]*A[1]*...*A[index-1]
        left = [1] * listLength
        for index in range(1, listLength):
            left[index] = left[index - 1] * a[index - 1]

        # right[index]:代表A[index+1]*A[index+2]*...*A[listLength-1]
        right = [1] * listLength
        for index in range(listLength - 2, -1, -1):
            right[index] = right[index + 1] * a[index + 1]

        answer = [1] * listLength
        for index in range(listLength):
            answer[index] = left[index] * right[index]
        return answer         