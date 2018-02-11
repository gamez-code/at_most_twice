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
