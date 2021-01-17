# retainAll
# Write a method called retainAll that takes two sets of integers as parameters and that removes any values in the first set that are not found in the second set. 

# For example, given sets: 

# s1: [0, 19, 8, 9, 12, 13, 14, 15] 
# s2: [0, 19, 2, 4, 5, 9, 10, 11] 
# If the following call is made: 

# retainAll(s1, s2); 
# after the call, the sets would store the following values: 

# s1: [0, 19, 9] 
# s2: [0, 19, 2, 4, 5, 9, 10, 11] 
# You are implementing a two-argument alternative to the standard Set method called retainAll, so you are not allowed to call that method to solve this problem. 

# You are also not allowed to construct any structured objects to solve the problem (no set, list, stack, queue, string, etc) although you can construct iterators. 

# Your method should not change the second set passed as a parameter.
def retainAll(set1, set2):
    for element in set1.copy():
        if element in set2:
            print(element)
        else:
            set1.remove(element)
    return set1, set2

# java
#  Iterator<Integer> iterator = set.iterator();
#         while(iterator.hasNext()) {
#             Integer setElement = iterator.next();
#             if(!s2.contains(setElement)) {
#                 iterator.remove();
#             }


if __name__ == "__main__":
    # set1 = {0,19,8,9,12,13,14,15}
    # set2 = {0,19,2,4,5,9,10,11}

    set1 = {0, 19, 8, 9, 12, 13, 14, 15}
    set2 = {0, 19, 2, 4, 5, 9, 10, 11}
    set1, set2 = retainAll(set1, set2)
    print("set1: ", set1)
    print("set2: ", set2)

