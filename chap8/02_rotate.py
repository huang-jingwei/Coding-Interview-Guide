class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)  # 矩阵的行、列
        cols = len(matrix[0])
        if rows == 0 or rows == 1:
            return matrix

        leftRow = 0         # 移动区域的左上角、右下角
        leftCol = 0
        rightRow = rows - 1
        rightCol = cols - 1

        while leftRow < rightRow:
            self.rotate_process(matrix, leftRow, leftCol, rightRow, rightCol)
            leftRow += 1        # 更新端点坐标
            leftCol += 1
            rightRow -= 1
            rightCol -= 1
        return matrix

    def rotate_process(self, matrix, leftRow, leftCol, rightRow, rightCol):
        times = rightCol - leftCol
        for i in range(times):
            item = matrix[leftRow][leftCol + i]
            matrix[leftRow][leftCol + i] = matrix[rightRow - i][leftCol]
            matrix[rightRow - i][leftCol] = matrix[rightRow][rightCol - i]
            matrix[rightRow][rightCol - i] = matrix[leftRow + i][rightCol]
            matrix[leftRow + i][rightCol] = item
