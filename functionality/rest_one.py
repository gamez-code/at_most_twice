
def rest_one(Array, idx):
    if Array[idx]:
        # Si el numero de Array[idx] es distinto a cero entra, ya que 0 - 1 es negativo.
        if Array[idx]==1 and not idx:
            # Si Array[idx] es igual a 1 y idx es igual a cero.
            # Quiere decir que es el primer numero al restar se elimina.
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
        # Si el idx es distinto a cero entra, cambia Array[idx] por 9 y resta al siguiente.
        Array[idx] = 9
        return rest_one(Array, idx - 1)
