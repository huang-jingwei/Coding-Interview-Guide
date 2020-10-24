class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        res = 0  # 计数器，记录岛屿数量
        rows = len(grid)  # 二维数组的行、列数
        cols = len(grid[0])

        for rowIndex in range(rows):
            for colIndex in range(cols):
                if grid[rowIndex][colIndex] == '1':
                    res += 1
                    self.infect(grid, rowIndex, colIndex, rows, cols)
        return res

    # 函数功能：感染函数,将连在一片的1全部转化为2
    # 参数说明：grid：岛屿的二维矩阵，rows,cols分别为岛屿二维数组的行、列数
    # rowIndex,colIndex分别为当前位置的行、列坐标
    def infect(self, grid, rowIndex, colIndex, rows, cols):
        # 防止搜索下标越过二维数组的边界
        if rowIndex < 0 or colIndex < 0 or rowIndex >= rows or colIndex >= cols:
            return
        # 感染函数只感染数值为1的区域
        if grid[rowIndex][colIndex] != '1':
            return
        grid[rowIndex][colIndex] = 2
        # 沿着四个方向进行进一步的搜索
        self.infect(grid, rowIndex + 1, colIndex, rows, cols)
        self.infect(grid, rowIndex, colIndex + 1, rows, cols)
        self.infect(grid, rowIndex - 1, colIndex, rows, cols)
        self.infect(grid, rowIndex, colIndex - 1, rows, cols)