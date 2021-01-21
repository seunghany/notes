# Implement
# selectionSort(L: list) -> None:
# insertionSort(L: list) -> None:
# mergeSort(L: list) -> None:
# quicksort(L: list) -> None:
#
# Check if all of them actually sort a list!
#
# Measure their time complexity by using import time
# When list lengths are 10000 and 20000

def selectionSort(L: list) -> None:
    for i in range(len(L)):
        # Find the smallest unsorted list
        smallest = i
        for j in range(i+1,len(L)):
            if L[j] < L[smallest]:
                smallest = j
        # swapping
        L[i], L[smallest] = L[smallest], L[i]

def insertionSort(L: list) -> None: # 송다영씨
    print("list before sorting:", L)
    # step 1 loop 을 돌린다
    for i in range(1, len(L)):
        # step 2 compare the current element to its predecessor 전꺼랑 비교하기
        # if L[i] < L[i-1]: # 전거보다 작으면 바꿔주기
        #     L[i-i], L[i] = L[i], L[i-1] # 위치 바꿔주기
        # # step 3 위에 step 2 를 반복한다. 언제까지? 그 전꺼 보다 클때까지.
        for j in  range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j]
    print("list after sorting:", L)

    # key = L[i]
    # j = i - 1
    # while j >= 0 and key < L[j]:
    #     L[j], L[j + 1] = L[j + 1], L[j]  # 위치 바꿔주기
    #     j -= 1
# def mergeSort(L: list) -> None: # 이창엽씨
#
def quickSort(L: list) -> None: # 신승한
    partitionSort(L, 0, len(L)-1)


def partitionSort(L: list, first: int, last: int) -> None:
    # Base case condition check
    if first == last:
        return
    else: # recursive case
        pi_idx = piSelect(L, first, last)
        pi_idx = partition(L, first, last, pi_idx)
        # pivot is in right place
        partitionSort(L, first, pi_idx-1)
        partitionSort(L, pi_idx+1, last)


def piSelect(L: list, first: int, last: int) -> int:
    # find approximate median
    med = first + (last + first)//2

def partition(L: list, first: int, last: int, pi_idx: int) -> int:
    pi = L[pi_idx]
    i, j = first, last
    while i < j:
        # left partition scan
        while i <= last and L[i] <= pi:
            i += 1
        # right partition
        while j >= first and L[j] >=pi:
            j -= 1
        # now time to swap
        if i < j:
            L[i], L[j] = L[j], L[i]
            
if __name__ == '__main__':
    L = [3, 7, 8, 4, 5, 2, 1]
    insertionSort(L)