import pulp as p
#from p import *

Billboards = ['BB1', 'BB2', 'SS1', 'SS2', 'SS3']

costs = {'BB1': 126.19,
         'BB2': 102.54, 
         'SS1': 316.60,
         'SS2': 388.62,
         'SS3': 359.34
         }
contacts = {'BB1': 1967,
            'BB2': 1599,
            'SS1': 3290,
            'SS2': 4039,
            'SS3': 3735
            }
# Create a variable
x1 = p.LpVariable("BB1", lowBound=4, upBound=4, cat=p.LpInteger)   
x2 = p.LpVariable("BB2", lowBound=4, upBound=10, cat=p.LpInteger) 
y1 = p.LpVariable("SS1", lowBound=4, upBound=18, cat=p.LpInteger)    
y2 = p.LpVariable("SS2", lowBound=4, upBound=18, cat=p.LpInteger)  
y3 = p.LpVariable("SS3", lowBound=4, upBound=4, cat=p.LpInteger)    

Difference_constraint_BB1_BB2 = {"BB1": -1.0,
                                 "BB2": 1.0,
                                 "SS1": 0.0,
                                 "SS2": 0.0,
                                 "SS3": 0.0
                                 }
Difference_constraint_BB1_SS1 = {"BB1": -1.0,
                                 "BB2": 0.0,
                                 "SS1": 1.0,
                                 "SS2": 0.0,
                                 "SS3": 0.0
                                 }
Difference_constraint_BB1_SS2 = {"BB1": -1.0,
                                 "BB2": 0.0,
                                 "SS1": 0.0,
                                 "SS2": 1.0,
                                 "SS3": 0.0
                                 }
Difference_constraint_BB1_SS3 = {"BB1": -1.0,
                                 "BB2": 0.0,
                                 "SS1": 0.0,
                                 "SS2": 0.0,
                                 "SS3": 1.0
                                 }    
Difference_constraint_BB2_SS1 = {"BB1": 0.0,
                                 "BB2": -1.0,
                                 "SS1": 1.0,
                                 "SS2": 0.0,
                                 "SS3": 0.0
                                 }                        
Difference_constraint_BB2_SS2 = {"BB1": 0.0,
                                 "BB2": -1.0,
                                 "SS1": 0.0,
                                 "SS2": 1.0,
                                 "SS3": 0.0
                                 }             
Difference_constraint_BB2_SS3 = {"BB1": 0.0,
                                 "BB2": 1.0,
                                 "SS1": 0.0,
                                 "SS2": 0.0,
                                 "SS3": -1.0
                                 }             
Difference_constraint_SS1_SS2 = {"BB1": 0.0,
                                 "BB2": 0.0,
                                 "SS1": 1.0,
                                 "SS2": -1.0,
                                 "SS3": 0.0
                                 }         

Difference_constraint_SS1_SS3 = {"BB1": 0.0,
                                 "BB2": 0.0,
                                 "SS1": 1.0,
                                 "SS2": 0.0,
                                 "SS3": -1.0
                                 }         
Difference_constraint_SS2_SS3 = {"BB1": 0.0,
                                 "BB2": 0.0,
                                 "SS1": 0.0,
                                 "SS2": 1.0,
                                 "SS3": -1.0
                                 } 
prob = p.LpProblem("The number of display problem", p.LpMaximize)
ingredient_vars = p.LpVariable.dicts("Ingr", Billboards, 2, cat=p.LpInteger)
# Objective Function
prob += p.lpSum([costs[i]*ingredient_vars[i] for i in Billboards])
# Constraints: 
prob += p.lpSum([Difference_constraint_BB1_BB2[i] * ingredient_vars[i] for i in Billboards]) <= 6
prob += p.lpSum([Difference_constraint_BB1_SS1[i] * ingredient_vars[i] for i in Billboards]) <= 14
prob += p.lpSum([Difference_constraint_BB1_SS2[i] * ingredient_vars[i] for i in Billboards]) <= 14
#prob += p.lpSum([Difference_constraint_BB1_SS3[i] * ingredient_vars[i] for i in Billboards]) <= 0
prob += p.lpSum([Difference_constraint_BB2_SS1[i] * ingredient_vars[i] for i in Billboards]) <= 8
prob += p.lpSum([Difference_constraint_BB2_SS2[i] * ingredient_vars[i] for i in Billboards]) <= 8
prob += p.lpSum([Difference_constraint_BB2_SS3[i] * ingredient_vars[i] for i in Billboards]) <= 6
#prob += p.lpSum([Difference_constraint_SS1_SS2[i] * ingredient_vars[i] for i in Billboards]) <= 0
prob += p.lpSum([Difference_constraint_SS1_SS3[i] * ingredient_vars[i] for i in Billboards]) <= 14
prob += p.lpSum([Difference_constraint_SS2_SS3[i] * ingredient_vars[i] for i in Billboards]) <= 14
prob += p.lpSum([contacts[i]*ingredient_vars[i] for i in Billboards]) <= 81848.85
# The problem data is written to an .lp file
prob.writeLP("The number of display problem.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", p.LpStatus[prob.status])


# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)


# The optimised objective function value is printed to the screen    
print(p.value(prob.objective))