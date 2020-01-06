import pulp
from pulp import *

Billboards = ['Billboard1', 'Billboard2', 'Billboard3']

costs = {'Billboard1': 123.9, 
         'Billboard2': 111.3, 
         'Billboard3': 87.1
         }
contacts = {'Billboard1': 1239, 
            'Billboard2': 1113, 
            'Billboard3': 871
         }

Billboard1 = pulp.LpVariable("Billboard1", 2, 10, cat=pulp.LpInteger)
Billboard2 = pulp.LpVariable("Billboard2", 2, 8, cat=pulp.LpInteger)
Billboard3 = pulp.LpVariable("Billboard3", 2, 20, cat=pulp.LpInteger)

Difference_constaint_BB1_BB2 = {"Billboard1": 1.0,
                                "Billboard2": 1.0,
                                "Billboard3": 0.0}

Difference_constaint_BB1_BB3 = {"Billboard1": 1.0,
                                "Billboard2": 0.0,
                                "Billboard3": 1.0}

Difference_constaint_BB2_BB3 = {"Billboard1": 0.0,
                                "Billboard2": 1.0,
                                "Billboard3": 1.0}

prob = pulp.LpProblem("The number of display problem", pulp.LpMaximize)
ingredient_vars = pulp.LpVariable.dicts("Ingr", Billboards, 2, cat= pulp.LpInteger)
# Objective Function 
prob += pulp.lpSum([costs[i]*ingredient_vars[i] for i in Billboards])

#prob += pulp.lpSum([Difference_constaint_BB1_BB2[i] * ingredient_vars[i] for i in Billboards]) <= 2
prob += pulp.lpSum([Difference_constaint_BB1_BB3[i] * ingredient_vars[i] for i in Billboards]) <= 10
prob += pulp.lpSum([Difference_constaint_BB2_BB3[i] * ingredient_vars[i] for i in Billboards]) <= 12
prob += pulp.lpSum([contacts[i]*ingredient_vars[i] for i in Billboards]) <= 20000
# The problem data is written to an .lp file
prob.writeLP("The number of display problem.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", pulp.LpStatus[prob.status])


# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen    
print (value(prob.objective))