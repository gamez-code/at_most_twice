def check_one(Array, NUMBER, idx):
    for i in range(idx,len(Array)):
        if Array[i] != 9:
            aArray = Array[i::]
            Array[i::] = [9]*(len(Array)-i)
            nArray = int("".join(map(str,Array)))
            if nArray >= NUMBER:
                Array[i::] = aArray
            else:
                return Array, i
    else:
        return Array, -1


def rest_one(Array, idx):
    if Array[idx]:
        if Array[idx]==1 and not idx:
            Array.pop(idx)
            return Array
        else:
            Array[idx] -= 1
            if len(Array) - 1 == idx:
                return Array
            else:
                Array[idx + 1::] = [9] * (len(Array) - (idx + 1))
                return Array
    elif idx:
        Array[idx] = 9
        return rest_one(Array, idx - 1)


def check_twice(Array):
    for a in Array:
        if Array.count(a) > 2:
            idx = len(Array) - Array[::-1].index(a) - 1
            return rest_one(Array, idx)
    else:
        return Array

def check_number(Array, NUMBER, idx=0):
    Aux = []
    while Array != Aux:
        Aux = Array.copy()
        Array = check_twice(Array)
    else:
        Array, nIdx = check_one(Array, NUMBER, idx)

        if nIdx!=idx:
            return check_number(Array, NUMBER, nIdx)
        else:
            return Aux

def solve_problem(string_number):
    NUMBER = int(string_number)
    Array = list(map(int,string_number))
    Array = check_number(Array, NUMBER)
    solve = "".join(map(str,Array))
    return solve

test = input()
while test!="":
    solve = solve_problem(test)
    print(solve)
    test = input()
