from functionality.check_number import check_number
def solve_problem(string_number):
    NUMBER = int(string_number)
    Array = list(map(int,string_number))
    Array = check_number(Array, NUMBER)
    solve = "".join(map(str,Array))
    return solve