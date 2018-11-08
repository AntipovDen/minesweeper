


field = [[1, 0, 1, 1, 1, 0, 1, 0],
         [1, 0, 0, 1, 1, 1, 0, 1],
         [0, 0, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1],
         [0, 1, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0]]

visited = [[False] * 8 for _ in range(6)]




def dfs(x, y, come_from):
    visited[y][x] = True
    if field[y][x] == 0:
        x_n = x - (come_from % 2) * (-1) ** (come_from // 2)
        y_n = y + ((come_from + 1) % 2) * (-1) ** (come_from // 2)
        if x_n == 2 and y_n == 6:
            print('finished')
            print(x, y)
            visited[y][x] = False
            return True
        if 0 <= x_n < 8 and 0 <= y_n < 6 and not visited[y_n][x_n]:
            res = dfs(x_n, y_n, come_from)
            if res:
                print(x, y)
            visited[y][x] = False
            return res
        visited[y][x] = False
        return False
    else:
        x_n = x + ((come_from + 1) % 2)
        y_n = y + (come_from % 2)
        res1 = res2 = False
        if 0 <= x_n < 8 and 0 <= y_n < 6 and not visited[y_n][x_n]:
            res1 = dfs(x_n, y_n, ((come_from + 1) % 2) * 3)
            if res1:
                print(x, y)

        x_n = x - ((come_from + 1) % 2)
        y_n = y - (come_from % 2)
        if 0 <= x_n < 8 and 0 <= y_n < 6 and not visited[y_n][x_n]:
            res2 = dfs(x_n, y_n, 1 + (come_from % 2))
            if res2:
                print(x, y)
        visited[y][x] = False
        return res1 or res2

dfs(7, 4, 1)
