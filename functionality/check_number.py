from functionality.check_twice import check_twice

from functionality.check_one import check_one


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