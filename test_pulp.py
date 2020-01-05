import pulp as p 
  
# Create a LP Maximize problem 
Lp_prob = p.LpProblem('Display problem', p.LpMaximize)  
  
# Create problem Variables  
x1 = p.LpVariable("x1", lowBound = 2,upBound= 10, cat= p.LpInteger)   # Create a variable x1 >= 2
x2 = p.LpVariable("x2", lowBound = 2, upBound= 8, cat= p.LpInteger)   # Create a variable x2 >= 2 
x3 = p.LpVariable("x3", lowBound = 2, upBound= 20, cat= p.LpInteger)   # Create a variable x3 >= 2  
# Objective Function 
Lp_prob += 123.9 * x1 + 111.3* x2 + 87.1 *x3
  
# Constraints: 
#Lp_prob += x1 <= 10
#Lp_prob += x2 <= 8
#Lp_prob += x3 <= 20
Lp_prob += 1239*x1+1113*x2+ 871*x3 <= 20000
  
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
print(p.value(x1), p.value(x2),p.value(x3), p.value(Lp_prob.objective))   
