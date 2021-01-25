# def fibonnaci(curr, next1):
#     # 1,1,2,3,5,8,13,21, 34

#     # Base Case
#     if curr == 34:
#         return 1
#     # Recursive case
#     else:
#         fibonnaci(next1, curr + next1)

def fibonnaci(n: int)-> int:
    # 1,1,2,3,5,8
    if  n == 0 or n == 1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
if __name__ == "__main__":
    fibon_index = fibonnaci(8)
    print(fibon_index)
