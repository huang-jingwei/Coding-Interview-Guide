class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)            # 路径网格的行、列
        cols = len(grid[0])

        if rows == 0 or cols == 0:  # 网格的行或列为0时，则认为输入网格矩阵为空，返回0
            return 0

        # pathCount[i][j]代表第i行，第j列交点位置的路径总和
        pathCount = [[0 for i in range(cols)] for j in range(rows)]
        pathCount[0][0] = grid[0][0]

        for rowIndex in range(rows):
            for colIndex in range(cols):

                if rowIndex == 0 and colIndex == 0:   # 原点位置已经初始化，不再进行任何操作
                    continue

                elif rowIndex == 0 and colIndex > 0:  # 第1行元素
                    pathCount[rowIndex][colIndex] = pathCount[rowIndex][colIndex - 1] + grid[rowIndex][colIndex]
                elif colIndex == 0 and rowIndex > 0:  # 第1列元素
                    pathCount[rowIndex][colIndex] = pathCount[rowIndex - 1][colIndex] + grid[rowIndex][colIndex]
                else:                                 # 其他位置元素
                    pathCount[rowIndex][colIndex] = min(pathCount[rowIndex][colIndex - 1],pathCount[rowIndex - 1][colIndex]) + grid[rowIndex][colIndex]
        return pathCount[-1][-1]