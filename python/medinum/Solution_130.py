# 130. Surrounded Regions

class Solution:

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x_length = len(board)
        if x_length == 0: 
            return

        y_length = len(board[0])
        confirmed = set()
        dfs = []
        for i in range(x_length):
            if board[i][0] == 'O':
                board[i][0] = 'temp'
                dfs.append((i, 0))
            if board[i][y_length - 1] == 'O':
                board[i][y_length - 1] = 'temp'
                dfs.append((i, y_length - 1))
        for j in range(y_length):
            if board[0][j] == 'O':
                board[0][j] = 'temp'
                dfs.append((0, j))
            if board[x_length - 1][j] == 'O':
                board[x_length - 1][j] = 'temp'
                dfs.append((x_length - 1, j))
        while dfs:
            i, j = dfs.pop()
            confirmed.add((i, j))
            if i+1 < x_length and board[i+1][j] == 'O':
                board[i+1][j] = 'temp'
                dfs.append((i + 1, j))
            if i > 0 and board[i-1][j] == 'O':
                board[i-1][j] = 'temp'
                dfs.append((i-1, j))
            if j+1 < y_length and board[i][j+1] == 'O':
                board[i][j+1] = 'temp'
                dfs.append((i, j + 1))
            if j > 0 and board[i][j-1] == 'O':
                board[i][j-1] = 'temp'
                dfs.append((i, j-1))
        for i in range(x_length):
            for j in range(y_length):
                if (i, j) in confirmed:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return

arr = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
arr2 = [["X","O","X","X"],["X","O","X","X"],["X","O","O","X"],["X","X","O","X"]]
arr3 = [
    ["O","X","O","O","O","O","O","O","O"],
    ["O","O","O","X","O","O","O","O","X"],
    ["O","X","O","X","O","O","O","O","X"],
    ["O","O","O","O","X","O","O","O","O"],
    ["X","O","O","O","O","O","O","O","X"],
    ["X","X","O","O","X","O","X","O","X"],
    ["O","O","O","X","O","O","O","O","O"],
    ["O","O","O","X","O","O","O","O","O"],
    ["O","O","O","O","O","X","X","O","O"]]
ans = Solution().solve(arr2)
for i in ans:
    print(i)
# print(ans)

