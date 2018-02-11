from functionality.solve_problem import solve_problem

test = open('txt_file/test.txt','r')
line_test = test.readlines()
dline_test = list(map(lambda x: x.replace('\n',''), line_test))
solve_text = open('txt_file/solve.txt','w')
for t in dline_test:
    solve = solve_problem(t)
    solve_text.write(solve + '\n')
solve_text.close()
test.close()
