def printArray(a):
    for i in range(len(a)):
        print("".join(a[i]))

def flip(a, fd):
    # flip hand row 0
    right_hand = fd[a[0][0]]
    left_hand = fd[a[0][2]]
    a[0][0] = left_hand
    a[0][2] = right_hand
    # flip hand row 1
    right_hand = fd[a[1][0]]
    left_hand = fd[a[1][2]]
    a[1][0] = left_hand
    a[1][2] = right_hand
    # flip leg
    right_leg = fd[a[2][0]]
    left_leg = fd[a[2][2]]
    a[2][0] = left_leg
    a[2][2] = right_leg

def right_hand(a,s):
    if "head" in s:
        a[1][0] = " "
        a[0][0] = dict[s]
    else:
        a[0][0] = " "
        a[1][0] = dict[s]
    return a

def left_hand(a,s):
    if "head" in s:
        a[1][2] = " "
        a[0][2] = dict[s]
    else:
        a[0][2] = " "
        a[1][2] = dict[s]
    return a

def right_leg(a,s):
    a[2][0] = dict[s]
    return a

def left_leg(a,s):
    a[2][2] = dict[s]
    return a

def myfunc(s, a):
    if "left hand" in s:
        return left_hand(a,s)
    if "right hand" in s:
        return right_hand(a,s)
    if "left leg" in s:
        return left_leg(a,s)
    if "right leg" in s:
        return right_leg(a,s)

dict = {
    "left hand to head": ")",
    "left hand to hip": ">",
    "left hand to start": "\\",
    "left leg in": ">",
    "left leg out": "\\",
    "right hand to head": "(",
    "right hand to hip": "<",
    "right hand to start": "/",
    "right leg in": "<",
    "right leg out": "/"
}

flipdict = {
    "(": ")",
    ")": "(",
    ">": "<",
    "<": ">",
    "/": "\\",
    "\\": "/",
    " ": " "
}

for N in range(int(input())):
    a = []
    a.append([" ", "o", " "])
    a.append(["/","|","\\"])
    a.append(["/"," ","\\"])
    # printArray(a)
    isForward = True
    for i in range(int(input())):
        s = input()
        if "say" in s:
            print(s[4:len(s)])
        elif "turn" in s:
            if isForward == True:
                isForward = False
            else:
                isForward = True
            flip(a, flipdict)
            printArray(a)
        else:
            if isForward:
                # normal flip
                myfunc(s, a)
                printArray(a)
            else:
                # left => right
                if "left" in s:
                    s.replace("left", "right")
                    myfunc(s, a)
                else:
                    s.replace("right", "left")
                    myfunc(s, a)
                printArray(a)





