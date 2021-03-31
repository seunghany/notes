#
# 1. Obtain an adjacency matrix in the form of a two dimensional array.
# The input has the form of {input node0:[(output node1, weight01), (output node2,
# weight02), …], input node1: [(output node0, weight10), (output node2, weight12), …], …}.
# The pair of the output node and weight can be omitted for zero weight.
# The output is [[0, weight01, weight02,...],[weight10, 0, weight12,...],…].
# For example, if the input is
# {0:[(1,10), (2,5), (4,8)],
# 1:[(0,5), (3,4), (4,2)],
# 2:[(1,5), (4,4)],
# 3:[(0,9), (2,7)],
# 4:[(1, 2), (2, 5), (3,5)]}, then its output is
# [[0, 10, 5, 0, 8],
# [5, 0, 0, 4, 2],
# [0, 5, 0, 0, 4],
# [9, 0, 7, 0, 0],
# [0, 2, 5, 5, 0]].
def answer(input):
    N = len(input)
    answer = [[0 for i in range(N)] for j in range(N)]
    for key in input:
        # print(key)
        for j, weight in input[key]:
            # print(j, weight)
            answer[key][j] = weight
    print(answer)

if __name__ == '__main__':
    input = {}
    input[0] = [(1, 10), (2, 5), (4, 8)]
    input[1] = [(0, 5), (3, 4), (4, 2)]
    input[2] = [(1, 5), (4, 4)]
    input[3] = [(0, 9), (2, 7)]
    input[4] = [(1, 2), (2, 5), (3, 5)]
    answer(input)