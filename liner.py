from pulp import *

Billboards = ['Billboard_1', 'Billboard_2', 'Billboard_3']

costs = {'Billboard_1': 123.9, 
         'Billboard_2': 111.3, 
         'Billboard_3': 87.5, 
         }


prob = LpProblem("The number of display problem", LpMaximize)
ingredient_vars = LpVariable.dicts("Ingr", Billboards, 200)
x1=LpVariable("Billboard_1", 2, 10, LpInteger)
x2=LpVariable("Billboard_2", 2, 8, LpInteger)
x3=LpVariable("Billboard_3", 2, 20, LpInteger)

proteinPercent = {"Billboard_1": 1.0,
"Billboard_2": 0.0,
"Billboard_3": 0.0}

fatPercent= {"Billboard_1": 0.0,
"Billboard_2": 1.0,
"Billboard_3": 0.0}

fibrePercent = {"Billboard_1": 0.0,
"Billboard_2": 0.0,
"Billboard_3": 1.0}



prob = lpSum([costs[i]*ingredient_vars[i] for i in Billboards])
prob += lpSum([proteinPercent[i] * ingredient_vars[i] for i in Billboards]) <= 10.0
prob += lpSum([fatPercent[i] * ingredient_vars[i] for i in Billboards]) <= 8.0
prob += lpSum([fibrePercent[i] * ingredient_vars[i] for i in Billboards]) <= 20.0

# The problem data is written to an .lp file
prob.writeLP("The number of display problem.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen


# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen    
print (value(prob.objective))