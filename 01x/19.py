# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
#
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

import itertools
from ortools.sat.python import cp_model


def min_cost(N, K, costs):
    model = cp_model.CpModel()

    house_colour_vars = list()
    for i in range(0, N):
        house_colour_vars.append(list())
        for j in range(0, K):
            house_colour_vars[i].append(
                model.NewIntVar(0, 1, str.format("{},{}", i, j))
            )

    for i in range(0, N - 1):
        for j in range(0, K):
            model.Add(house_colour_vars[i][j] + house_colour_vars[i + 1][j] < 2)

    for i in range(0, N):
        model.Add(sum(house_colour_vars[i]) == 1)

    model.Minimize(
        sum(
            house_colour_vars[i][j] * costs[i][j]
            for i, j in itertools.product(range(0, N), range(0, K))
        )
    )

    solver = cp_model.CpSolver()
    solver.Solve(model)
    return solver.ObjectiveValue()


# 5 9 2 4 5
# 2 6 1 3 6
# 4 3 9 1 0
costs_ = [[5, 2, 4], [9, 6, 3], [2, 1, 9], [4, 3, 1], [5, 6, 0]]
assert 10 == min_cost(5, 3, costs_)  # 2, 3, 2, 3, 0

# 5 9 2 4 5 3
# 2 6 1 3 6 3
# 4 3 9 1 0 0
costs_ = [[5, 2, 4], [9, 6, 3], [2, 1, 9], [4, 3, 1], [5, 6, 0], [3, 3, 0]]
assert 12 == min_cost(6, 3, costs_)  # 2, 3, 1, 1, 5, 0
