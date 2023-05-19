def refPositiveAngle(angle):
    if angle >= 180:
        return (angle % 360) % 180
    else:
        return angle


def refNegativeAngle(angle):
    if abs(angle) > 180:
        return (angle % 360) % 180
    else:
        return 180 + angle


for N in range(int(input())):
    a = list(map(int, input().split(' ')))
    b = []
    if len(a) == 1:
        print(1)
    else:
        for i in range(1, len(a)):
            angle = a[i]
            # print("1", angle)
            if angle >= 0:
                angle = refPositiveAngle(angle)
            else:
                angle = refNegativeAngle(angle)
            # print("2", angle)
            b.append(angle)
        b = set(b)
        # print(b)
        if len(b) > 1:
            print(len(b) * 2)
        else:
            print(2)






