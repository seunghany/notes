# L = [ 1,2,3,4]
# target (int)

# target = 7
# [2,3]

def practice(L: list, target: int)-> list:

    for indexX in range(len(L)):
        x = L[indexX]
        dict[x] = indexX

    for i in range(len(i)):
        # 7 - 3 = 4
        indexY = target - L[i]  # 7 - 3 = 4
        return [L[i], indexY]

if __name__ == '__main__':
    L = [1, 2, 3, 4]
    x = practice(L, 7)
    print(x)
