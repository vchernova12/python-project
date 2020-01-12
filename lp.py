import pulp as p
import numpy as np
import math


def constrain_matrix(billboards):
    constrain_matrix = np.mat(np.eye(len(billboards)))
    billboard_constrain = np.split(np.array(constrain_matrix), len(billboards))
    return (billboard_constrain)


def avg_number_of_display(budget, billboards_costs):
    sum_costs = 0
    for cost in billboards_costs:
        sum_costs += cost
    avg_display = budget/sum_costs
    return (avg_display)


def billboards_with_minimal_stock(avg_display, in_stock):
    index_bb_with_minimal_stock = []
    for index, residium in enumerate(in_stock):
        if residium < avg_display:
            index_bb_with_minimal_stock.append(index)
    return(index_bb_with_minimal_stock)


def lp_bb_constrains(billboard_constrain, index_bb_with_minimal_stock, billboards):
    new_billboard_constrain = {}
    for index, constraint in enumerate(billboard_constrain):
        if index not in index_bb_with_minimal_stock:
            new_billboard_constrain.update({f'{billboards[index]}': constraint})
    return(new_billboard_constrain)


def lp_upper_bound(new_billboard_constrain, billboards, in_stock):
    upper_bound = []
    for bb in new_billboard_constrain:
        upper_bound.append(f'prob += p.lpSum({new_billboard_constrain[bb]}) for i in billboards]) <= {in_stock[billboards.index(bb)]}')
    return (upper_bound)

def lp_budget(index_bb_with_minimal_stock, budget, billboards_costs, in_stock):
    budget_for_minimals = 0
    for i in index_bb_with_minimal_stock:
        budget_for_minimals += (billboards_costs[i])*(in_stock[i])
    new_budget = float(budget) - budget_for_minimals
    return (new_budget)


def lp_low_bound(new_billboard_constrain, billboards_costs, in_stock, budget_for_lp, avg_display, billboards):
    lp_bb_costs = 0.0
    for bb in new_billboard_constrain:
        lp_bb_costs += billboards_costs[billboards.index(bb)]
    lp_avg_display = math.floor(budget_for_lp/lp_bb_costs)
    low_bound = []
    low_bound = []
    for bb in new_billboard_constrain:
        if in_stock[billboards.index(bb)] > lp_avg_display:
            low_bound.append(f'prob += p.lpSum({new_billboard_constrain[bb]}) for i in billboards]) => {lp_avg_display}')
        else:
            low_bound.append(f'prob += p.lpSum({new_billboard_constrain[bb]}) for i in billboards]) => {avg_display}')
        return(low_bound)

def lp_budget_constrain(lp_budget):
    max_budget_constrain = (f'prob += p.lpSum([billboards_cost[i]*ingredient_vars[i] for i in billboards]) >= {lp_budget*1.05}')
    min_budget_constrain = (f'prob += p.lpSum([costs[i]*ingredient_vars[i] for i in billboards]) <= {lp_budget*0.95}')
    return (max_budget_constrain, min_budget_constrain)


def lp_constrains_constractor(budget, billboards, in_stock, billboards_costs):
    billboard_constrain = constrain_matrix(billboards)
    avg_display = avg_number_of_display(budget, billboards_costs)
    index_bb_with_minimal_stock = billboards_with_minimal_stock(avg_display, in_stock)
    new_billboard_constrain = lp_bb_constrains(billboard_constrain, index_bb_with_minimal_stock, billboards)
    upper_bound = lp_upper_bound(new_billboard_constrain, billboards, in_stock)
    budget_for_lp = lp_budget(index_bb_with_minimal_stock, budget, billboards_costs, in_stock)
    low_bound = lp_low_bound(new_billboard_constrain, billboards_costs, in_stock, budget_for_lp, avg_display, billboards)
    budget_constrain = lp_budget_constrain(budget_for_lp)
    return (upper_bound, low_bound, budget_constrain)
if __name__ == "__main__":
    #billboards = ['BB1', 'BB2', 'SS1', 'SS2', 'SS3']
    #in_stock = [4.0, 10.3, 18.1, 18.1, 4.0]
    #billboards_costs = [126.19, 102.54, 316.60, 388.62, 359.34]
    #budget = 7170
    print(lp_constrains_constractor(7170, ['BB1', 'BB2', 'SS1', 'SS2', 'SS3'] , [4.0, 10.3, 18.1, 18.1, 4.0], [126.19, 102.54, 316.60, 388.62, 359.34]))