import pulp as p
import numpy as np
import math


def contraint_matrix(billboards):
    contraint_matrix = np.mat(np.eye(len(billboards)))
    contraint = np.split(np.array(contraint_matrix), len(billboards))
    billboard_contraint = {}
    for index, billboard in enumerate(billboards):
        billboard_contraint.update({f'{billboard}': contraint[index]})
    return billboard_contraint


def avg_number_of_display(budget, billboards_costs):
    avg_display = budget/sum(billboards_costs.values())
    return avg_display


def billboards_with_minimal_stock(avg_display, in_stock):
    bb_with_minimal_stock = {}
    for bb in in_stock:
        if in_stock[bb] < avg_display:
            bb_with_minimal_stock.update({f'{bb}': in_stock[bb]})
    return bb_with_minimal_stock


def lp_billboards(billboards, budget, billboards_costs, in_stock):
    avg_display = avg_number_of_display(budget, billboards_costs)
    bb_with_minimal_stock = billboards_with_minimal_stock(avg_display, in_stock)
    lp_billboards = []
    for bb in billboards:
        if bb not in bb_with_minimal_stock.keys():
            lp_billboards.append(bb)
    return lp_billboards


def lp_bb_contraints(billboard_contraint, bb_with_minimal_stock, billboards):
    new_billboard_contraint = {}
    
    for bb in billboard_contraint:
        if bb not in bb_with_minimal_stock.keys():
            new_billboard_contraint.update({f'{bb}': billboard_contraint[bb]})
            
    return new_billboard_contraint


def lp_upper_bound(new_billboard_contraint, in_stock, prob, ingredient_vars):
    for bb in new_billboard_contraint:
        prob += p.lpSum(new_billboard_contraint[bb]*ingredient_vars[bb]) <= in_stock[bb]
        print(f'for{bb} upper bound set to {in_stock[bb]}')
    return prob


def lp_budget(bb_with_minimal_stock, budget, billboards_costs, in_stock):
    budget_for_minimals = 0
    for bb in bb_with_minimal_stock:
        budget_for_minimals += (billboards_costs[bb])*(in_stock[bb])
    new_budget = float(budget) - budget_for_minimals
    return new_budget


def lp_lower_bound(new_billboard_contraint, billboards_costs, in_stock, budget_for_lp, avg_display, prob, ingredient_vars):
    lp_bb_costs = 0.0
    for bb in new_billboard_contraint:
       lp_bb_costs += billboards_costs[bb]
    lp_avg_display = math.floor(budget_for_lp/lp_bb_costs)
    for bb in new_billboard_contraint:
        if in_stock[bb] > lp_avg_display:
            prob += p.lpSum(new_billboard_contraint[bb] *ingredient_vars[bb]) >= lp_avg_display
            print(f'for{bb} lower bound set to {lp_avg_display}')
        else:
            prob += p.lpSum(new_billboard_contraint[bb] *ingredient_vars[bb]) >= avg_display
            print(f'for{bb} lower bound set to {avg_display}')
    return prob


def lp_budget_contraint(billboards_costs, new_billboards, budget_for_lp, prob, ingredient_vars ):
    max_budget = budget_for_lp*1.03
    min_budget = budget_for_lp*0.97
    prob += p.lpSum([billboards_costs[i]*ingredient_vars[i] for i in new_billboards]) >= min_budget
    prob += p.lpSum([billboards_costs[i]*ingredient_vars[i] for i in new_billboards]) <= max_budget
    return prob


def lp_contraints_constractor(budget, billboards, in_stock, billboards_costs, prob, ingredient_vars, new_billboards):
    billboard_contraint = contraint_matrix(billboards)
    avg_display = avg_number_of_display(budget, billboards_costs)
    bb_with_minimal_stock = billboards_with_minimal_stock(avg_display, in_stock)
    new_billboard_contraint = lp_bb_contraints(billboard_contraint, bb_with_minimal_stock, billboards)
    upper_bound = lp_upper_bound(new_billboard_contraint, in_stock, prob, ingredient_vars)
    budget_for_lp = lp_budget(bb_with_minimal_stock, budget, billboards_costs, in_stock)
    lower_bound = lp_lower_bound(new_billboard_contraint, billboards_costs, in_stock, budget_for_lp, avg_display, prob, ingredient_vars)
    budget_contraint = lp_budget_contraint(billboards_costs, new_billboards, budget_for_lp, prob, ingredient_vars )
    return upper_bound, lower_bound, budget_contraint

def lp_constractor(budget, billboards, in_stock, billboards_costs):
    prob = p.LpProblem("The number of display problem", p.LpMaximize)

    new_billboards = lp_billboards(billboards, budget, billboards_costs, in_stock)
    ingredient_vars = p.LpVariable.dicts("Ingr", new_billboards, 2, cat=p.LpInteger)
    # Objective Function

    prob += p.lpSum([billboards_costs[i]*ingredient_vars[i] for i in new_billboards])
    print(ingredient_vars)
    print(billboards_costs)
    print([billboards_costs[i]*ingredient_vars[i] for i in new_billboards])
    # Contraints: 
    upper_bound, lower_bound, budget_contraint = lp_contraints_constractor(budget, billboards, in_stock, billboards_costs, prob, ingredient_vars, new_billboards)
    print(prob)
    # The problem data is written to an .lp file
    #prob.writeLP("The number of display problem.lp")

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The status of the solution is printed to the screen
    print("Status:", p.LpStatus[prob.status])

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        if v.varValue > 0:
            print(v.name, "=", v.varValue)
    # The optimised objective function value is printed to the screen   
    #print(p.value(prob.objective))


if __name__ == "__main__":
    #billboards = ['BB1', 'BB2', 'SS1', 'SS2', 'SS3']
    #in_stock = [4.0, 10.3, 18.1, 18.1, 4.0]
    #billboards_costs = [126.19, 102.54, 316.60, 388.62, 359.34]
    #budget = 7170
    print(lp_constractor(7170, ['BB1', 'BB2', 'SS1', 'SS2', 'SS3'], 
                    {"BB1": 4.0,
                    "BB2": 10.0,
                    "SS1": 18.0,
                    "SS2": 18.0,
                    "SS3": 4.0}, 
                    {"BB1": 126.19,
                    "BB2": 102.54,
                    "SS1": 316.60,
                    "SS2": 388.62,
                    "SS3": 359.34}))

