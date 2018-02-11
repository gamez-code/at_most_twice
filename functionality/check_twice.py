from functionality.rest_one import rest_one

def check_twice(Array):
    for a in Array:
        if Array.count(a) > 2:
            idx = len(Array) - Array[::-1].index(a) - 1
            return rest_one(Array, idx)
    else:
        return Array
