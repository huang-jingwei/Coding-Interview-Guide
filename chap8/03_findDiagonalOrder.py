class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:  # 矩阵只有一个元素或无元素时
            return []
        elif len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]

        rows = len(matrix)   # 矩阵的行、列
        cols = len(matrix[0])
        data = []            # 用来存放打印的元素
        direction = True     # direction=False，右向左打印；反之，左向右打印

        leftRow = 0          # 待打印的对角线的左端点、右端点
        leftCol = 0
        rightRow = 0
        rightCol = 0

        while leftCol < cols:
            # 本轮打印的元素
            item = self.process(matrix, leftRow, leftCol, rightRow, rightCol, direction)
            for i in item:
                data.append(i)

            # 更新端点坐标、打印方向
            direction = bool(1 - direction)
            if leftRow < rows - 1:
                leftRow += 1
            else:
                leftCol += 1

            if rightCol < cols - 1:
                rightCol += 1
            else:
                rightRow += 1
        return data

    # direction=False，右向左打印；反之，左向右打印
    def process(self, matrix, leftRow, leftCol, rightRow, rightCol, direction):
        item = []
        if direction:  # 左向右打印
            for i in range(rightCol - leftCol + 1):
                item.append(matrix[leftRow - i][leftCol + i])
        else:  # 右向左打印
            for i in range(rightCol - leftCol + 1):
                item.append(matrix[rightRow + i][rightCol - i])
        return item