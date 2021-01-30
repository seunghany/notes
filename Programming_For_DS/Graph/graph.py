# There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.
#
# Some courses may have prerequisites, for example to take course `0`
# you have to first take course `1`, which is expressed as a pair: `[0,1]`
#
# Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses?
#
# **Hints**:
# 1. You can create other functions outside of `P1`
# 2. Try using ideas from *graphs*
#
# **Constraints**:
#
# - The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
# - You may assume that there are no duplicate edges in the input prerequisites.
# - `1 <= numCourses <= 10^5`

class Directed_Graph:
    
    def __init__(self, V: list, E:list) -> None:
        self.V = V[:]
        self.neighbor = {}
        for v in V:
            self.neighbor[v] = []
        for (v, w) in E:
            self.neighbor[w].append(v)
        self.total_count = 0


    def DFT(self, roots) -> int:
        for root in roots:
            self.DFTHelp(root)
        # if self.V:
        #     visited = {}
        #     for v in self.V:
        #         visited[v] = False
        #     for v in self.V:
        #         self.DFTHelp(visited, v)

    def DFTHelp(self, v: int) -> None:
        self.total_count += 1
        for w in self.neighbor[v]:
            self.DFTHelp(w)
def P1(n: int, pres) -> bool:
    # P1(2, [[1,0]])
    # 1 을 들으려면 0을 들어야 한다.
    # 0 -> 1
    vertex = set()
    roots = set()
    for elements in pres:
        vertex.add(elements[0])
        vertex.add(elements[1])
        roots.add(elements[1])
    for elements in pres:
        if elements[0] in roots:
            roots.remove(elements[0])
    roots = list(roots)
    vertex = list(vertex)
    DG = Directed_Graph(vertex, pres)
    print("Vertex: ", DG.V)
    print("Neighbor: ", DG.neighbor)
    print("Roots: ", roots)
    if len(roots) == 0:
        return False
    return DG.total_count < n

if __name__ == '__main__':
    x = P1(2, [[1, 0], [0, 1]])  # return True
    print(x)
    # 총 2개의 수업을 들어야 한다.
    #P1( # of classes, [  [courseA, Prerequisite] ]