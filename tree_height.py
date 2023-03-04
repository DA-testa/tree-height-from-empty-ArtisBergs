# python3

import sys
import threading
import numpy


def compute_height(n, parents, needle = set({-1}), max_height = set(), count = -1):
    count += 1
    max_height.add(count)
    temp = set()

    for j in needle:
        for i in range(n):
            if parents[i] == j:
                temp.add(i)

    if len(temp) != 0:
        compute_height(n, parents, temp, max_height, count)

    return len(max_height)-1


def main():
    # implement input form keyboard and from files
    n = 0
    parents = ""
    switch = input()
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    if "F" in switch:
        filename = input()
        if filename != "a":
            f = open("./test/"+filename, "r")
            n = f.readline()
            parents = f.readline()
            f.close()
    elif "I" in switch:
        # data = input("Data: ")
        # input number of elements
        # input values in one variable, separate with space, split these values in an array
        n = input()
        parents = input()

    # call the function and output it's result
    print(compute_height(int(n), numpy.fromstring(parents, dtype=int, sep=' ').tolist()))
    # pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))