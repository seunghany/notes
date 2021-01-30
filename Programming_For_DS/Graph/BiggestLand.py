#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
#
# **Note**: The length of each dimension in the given grid does not exceed 50.
class undi_graph():
    def __init__(self, V: list, E: list) -> None:
        self.V = V[:]
        self.neighbor = {}
        for v in V:
            self.neighbor[v] = []
        for (v, w) in E:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)
        self.max = 0
        self.local = 0

    def __DFTHelp(self, visited: list, v: int) -> None:
        if not visited[v]:
            self.local += 1
            visited[v] = True
            for w in self.neighbor[v]:
                self.__DFTHelp(visited, w)

    def DFT(self) -> None:
        if self.V:
            visited = {}
            for v in self.V:
                visited[v] = False
            for v in self.V:
                self.__DFTHelp(visited, v)
                self.max = max(self.max, self.local)
                self.local = 0
        return self.max

def P2(grid) -> int:
    # 바다를 없애고 land의 index 만 구하기
    all_vertex = []
    all_edges = []
    new_grid = []
    for j in range(len(grid)):
        land_index = []
        for i in range(len(grid[j])):
            if grid[j][i] == 1:
                # land
                position = i + j*10
                land_index.append(position)
                all_vertex.append(position)
        new_grid.append(land_index)
    print("new_index_grid:", new_grid)
    # make edges
    land_dict = {}
    for i in range(len(new_grid)):
        land_dict[i] = {}
        slist = new_grid[i]
        land_dict[i]['vertices'] = new_grid[i]
        # print(land_dict)
        edges = []
        for j in range(len(slist) -1):
            if slist[j+1] - slist[j] == 1:
                edges.append([slist[j], slist[j+1]])
        land_dict[i]["edges"] = edges
        all_edges.extend(edges)
    print("dictionary:", land_dict)
    print("---" * 50)
    num_list = len(new_grid)
    print(all_vertex)
    for i in range(num_list - 1):
        # 이렇게 하면 graph 들이 생김
        for vertex in land_dict[i+1]['vertices']:
            vertex_before = vertex - 10
            if vertex_before in land_dict[i]['vertices']:
                new_edge = [vertex, vertex_before]
                all_edges.append(new_edge)

    print("all edges:", all_edges)
        # graph 를 combine 할 수 있음 좋음
    UG = undi_graph(all_vertex, all_edges)
    UG.DFT()
    print(UG.max)
if __name__ == '__main__':
    P2([
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ])
    P2([[0, 0, 0, 0, 0, 0, 0, 0]])
    P2(
        [[1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
         [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
         [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
         [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
         [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
         [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
         [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0]]
    )
    ##################
    # Your code here #
    ##################