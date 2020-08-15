class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 若输入为空或者输入矩阵为行向量，则返回空
        if matrix == None or len(matrix) < 1:
            return []
        array = list()  # 空数组，用来存放矩阵顺时针打印过程中的数字

        leftRow = 0     # 打印区域的左上角，右下角端点坐标
        leftCol = 0
        rightRow = len(matrix) - 1
        rightCol = len(matrix[0]) - 1

        while True:

            # 按照四次过程来获取顺时针打印过程的数值
            for index in range(leftCol, rightCol + 1): array.append(matrix[leftRow][index])
            leftRow = leftRow + 1    # 更新左上角端点行坐标
            if leftRow > rightRow: break

            for index in range(leftRow, rightRow + 1): array.append(matrix[index][rightCol])
            rightCol = rightCol - 1   # 更新右下角端点列坐标
            if leftCol > rightCol: break

            for index in range(rightCol, leftCol - 1, -1): array.append(matrix[rightRow][index])
            rightRow = rightRow - 1   # 更新右下角端点行坐标
            if leftRow > rightRow: break

            for index in range(rightRow, leftRow - 1, -1): array.append(matrix[index][leftCol])
            leftCol = leftCol + 1     # 更新左上角端点的列坐标
            if leftCol > rightCol: break

        return array