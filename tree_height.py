# python3

import sys
import threading
import numpy

results = numpy.array([])

def compute_height(n, parents):
    d = {}

    for i in range(n):
        if parents[i] in d:
            d[parents[i]].append(i)
        else:
            d[parents[i]] = [i]
    
    helper(d, -1, 0)

def helper(d, needle, counter):
    if needle in d:
        
        counter += 1
        global results
        results = numpy.append(results, counter)

        for i in d[needle]:
            helper(d, i, counter)

def main():
    # implement input from keyboard and from files
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
    substrings = parents.split()
    int_values = [int(s) for s in substrings]
    np_array = numpy.array(int_values)
    
    compute_height(int(n), np_array)
    print("%.0d" % (numpy.max(results)))
    # pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))