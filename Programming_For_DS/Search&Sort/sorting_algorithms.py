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
    """
    - 제자리 정렬 (In-place sorting method)
        -> 추가 메모리를 요구하지 않는 정렬 방법
    - 해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘
        - 첫 번째 순서에는 첫 번쨰 위치에 가장 최소값을 넣는다.
        - 두 번째 순서에는 두 번째 위치에 남은 값 중에서 최소값을 넣는다
        - ..... 게속
    Step by Step Procedures
    1. Find minimum value - 최소값 찾기
    2. swap the position with the first element in the list  - 첫 원소랑 교체
    3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다
    4. 하나의 원소만 남을 때까지 위 1~3 step 을 반복한다
    특징
    Time complexity = O(n^2) for worst and best cases
    Space complexity = O(1)
    In place
    not Stable
    """
    for i in range(len(L)): # list 전체를 봐야 하니
        # Find the smallest unsorted list
        smallest = i
        for j in range(i+1, len(L)):
            if L[j] < L[smallest]:
                smallest = j
        # swapping
        L[i], L[smallest] = L[smallest], L[i]


def insertionSort(L: list) -> None:
    """
    1. 사입 정렬은 두 번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후
        자료를 뒤로 옮기고 지정한 자리에 자료를 삽입하여 정렬 하는 알고리듬이다.
    2. 즉 두번째 자료는 첫 번째 자료, 세 번째 자료는 두 번째와 첫 번째 자료, ~~~~~~

    """
    print("list before sorting:", L)
    # step 1 loop 을 돌린다
    for i in range(1, len(L)):  # 두번째 index 부터 시작한다

        for j in  range(i, 0, -1):  # 뒤로 가는 것이 아닌 앞으로 가는 것이기 때문에 -1
            if L[j] < L[j-1]:  # Condition Check -> 전 element 보다 숫자가 작으면 바꿔주기
                L[j], L[j-1] = L[j-1], L[j]
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