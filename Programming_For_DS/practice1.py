from typing import List
def flipAndInvertImage(A:List[List[int]]) -> List[List[int]]:
    # step 1 Flipping

    for i in range(len(A)):
        for j in range(len(A[0])):
            if j < len(A[0]) - 1 - j:
                A[i][j], A[i][-1-j] = A[i][-1-j], A[i][j] # Swapping
            else:
                break
        
    # step 2
    for i in range(len(A)):
        for j in range(len(A[0])):
            for j in range(len(A[0])):
                A[i][j] = 1- A[i][j] # reversing
    return A
    # print(A)
    # for row in A:
    #     print("row",row)
    #     for element in row:
    #         if element == 0:
    #             A[row][element] = 1
    #         else:
    #             A[row][element] = 0
    # print(A)
    return A

if __name__ == "__main__":
    input1 = [[1,1,0],[1,0,1],[0,0,0]]
    input2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1], [1,0,1,0]]
    newOutput1 = flipAndInvertImage(input1)
    newOutput2 = flipAndInvertImage(input2)
    print(newOutput1)
    print(newOutput2)