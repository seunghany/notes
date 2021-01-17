def retainAll(set1, set2):
    for element in set1.copy():
        if element in set2:
            print(element)
        else:
            set1.remove(element)
    return set1, set2

if __name__ == "__main__":
    set1 = {0,19,8,9,12,13,14,15}
    set2 = {0,19,2,4,5,9,10,11}

    set1, set2 = retainAll(set1, set2)
    print("set1: ", set1)
    print("set2: ", set2)