import pulp as p
import numpy as np
import math


def constrain_matrix(billboards):
    constrain_matrix = np.mat(np.eye(len(billboards)))
    constrain = np.split(np.array(constrain_matrix), len(billboards))
    billboard_constrain = {}
    for index, billboard in enumerate(billboards):
        billboard_constrain.update({f'{billboard}': constrain[index]})
    return billboard_constrain


def avg_number_of_display(budget, billboards_costs):
    avg_display = budget/sum(billboards_costs.values())
    return avg_display 


def billboards_with_minimal_stock(avg_display, in_stock):
    bb_with_minimal_stock = {}
    for bb in in_stock:
        if in_stock[bb] < avg_display:
            bb_with_minimal_stock.update({f'{bb}': in_stock[bb]})
    return bb_with_minimal_stock


def lp_bb_constrains(billboard_constrain, bb_with_minimal_stock, billboards):
    new_billboard_constrain = {}
    for bb  in billboard_constrain:
        if bb not in bb_with_minimal_stock.keys():
            new_billboard_constrain.update({f'{bb}': billboard_constrain[bb]})
    return new_billboard_constrain 


def lp_upper_bound(new_billboard_constrain, billboards, in_stock):
    upper_bound = []
    for bb in new_billboard_constrain:
        upper_bound.append(f'prob += p.lpSum({new_billboard_constrain[bb]}) for i in billboards]) <= {in_stock[bb]}')
    return upper_bound

def lp_budget(bb_with_minimal_stock, budget, billboards_costs, in_stock):
    budget_for_minimals = 0
    for bb in bb_with_minimal_stock:
        budget_for_minimals += (billboards_costs[bb])*(in_stock[bb])
    new_budget = float(budget) - budget_for_minimals
    return new_budget


def lp_low_bound(new_billboard_constrain, billboards_costs, in_stock, budget_for_lp, avg_display, billboards):
    lp_bb_costs = 0.0
    for bb in new_billboard_constrain:
        lp_bb_costs += billboards_costs[bb]
    lp_avg_display = math.floor(budget_for_lp/lp_bb_costs)
    low_bound = []
    for bb in new_billboard_constrain:
        if in_stock[bb] > lp_avg_display:
        low_bound.append(f'prob += p.lpSum({new_billboard_constrain[bb]}) for i in billboards]) => {lp_avg_display}')
        else:
            low_bound.append(f'prob += p.lpSum({new_billboard_constrain[bb]}) for i in billboards]) => {avg_display}')
        return low_bound

def lp_budget_constrain(lp_budget):
    max_budget_constrain = (f'prob += p.lpSum([billboards_cost[i]*ingredient_vars[i] for i in billboards]) >= {lp_budget*1.05}')
    min_budget_constrain = (f'prob += p.lpSum([costs[i]*ingredient_vars[i] for i in billboards]) <= {lp_budget*0.95}')
    return max_budget_constrain, min_budget_constrain


def lp_constrains_constractor(budget, billboards, in_stock, billboards_costs):
    billboard_constrain = constrain_matrix(billboards)
    avg_display = avg_number_of_display(budget, billboards_costs)
    bb_with_minimal_stock = billboards_with_minimal_stock(avg_display, in_stock)
    new_billboard_constrain = lp_bb_constrains(billboard_constrain, bb_with_minimal_stock, billboards)
    upper_bound = lp_upper_bound(new_billboard_constrain, billboards, in_stock)
    budget_for_lp = lp_budget(bb_with_minimal_stock, budget, billboards_costs, in_stock)
    low_bound = lp_low_bound(new_billboard_constrain, billboards_costs, in_stock, budget_for_lp, avg_display, billboards)
    budget_constrain = lp_budget_constrain(budget_for_lp)
    return (upper_bound, low_bound, budget_constrain)


if __name__ == "__main__":
    #billboards = ['BB1', 'BB2', 'SS1', 'SS2', 'SS3']
    #in_stock = [4.0, 10.3, 18.1, 18.1, 4.0]
    #billboards_costs = [126.19, 102.54, 316.60, 388.62, 359.34]
    #budget = 7170
    print(lp_constrains_constractor(7170, ['BB1', 'BB2', 'SS1', 'SS2', 'SS3'], 
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