# t = int(input()) #num test case
# for i in range(t):
#     s, c, s0_cost = list(map(int, input().split())) # num station, capacity of tank, cost of fuel per liter
#     station_list = []
#     for i in range(s):
#         station_list.append(list(map(int, input().split())))
#
#     print(station_list) # [fuel needed, cost at station]


import numpy as NUMPY
import re


def chunks(s, numChar):
    for j in range(0, len(s), numChar):
        yield s[j:j+numChar]


def findCharater(char, array):
    result = []
    for irow in range(len(array)):
        for icol in range(len(array[irow])):
            if array[irow][icol] == char:
                result.append([irow,icol])
    return result

isSmallest = True
word = []
cipher_array = []
cipher = []
p = int(input())
n = int(input())
r, c = list(map(int, input().split(",")))
if input() != "S":
    isSmallest = False
for i in range(p):
    word.append(list(input()))
for i in range(n):
    line = input()
    clean = re.compile('<.*?>')
    line = re.sub(clean, '',line)
    if len(line) > 0:
        cipher_array.append(line)

cipher_string = "".join(cipher_array)
# print(cipher_string)
for chunk in chunks(cipher_string[:(c*r)], c):
    cipher.append(list(chunk))

cipher = NUMPY.array(cipher)

for w in word:
    solution = []
    for character in w:
        # find charater in cipher table
        temp = NUMPY.argwhere(cipher == character)
        # temp = findCharater(character, cipher)
        # print(temp)
        if len(temp) == 0:
            solution.append(0)
        elif len(temp) == 1:
            solution.append(temp[0][0] + 1)
            solution.append(temp[0][1] + 1)
        else:
            if isSmallest:
                solution.append(temp[0][0] + 1)
                solution.append(temp[0][1] + 1)
            else:
                solution.append(temp[len(temp)-1][0] + 1)
                solution.append(temp[len(temp)-1][1] + 1)
        # print(temp[0])
        # print(solution)
    # solution = np.array(solution).tostring()
    if 0 in solution:
        print(str(0))
    else:
        print(",".join(str(sol) for sol in solution))
    # print("---")
# print(word)
# print(cipher)
