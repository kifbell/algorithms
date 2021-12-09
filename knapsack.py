def unbounded_knapsack(max_weight, n_items, weights, values):
    knapsack = [0 for _ in range(max_weight+1)]
    items = [list() for _ in range(max_weight + 1)]

    for knapsack_capacity in range(1, max_weight+1):
        knapsack[knapsack_capacity] = 0
        items[knapsack_capacity] = list()

        for item in range(n_items):
            item_weight = weights[item]
            item_value = values[item]

            # is item embeddable into the knapsack?
            if item_weight <= knapsack_capacity:
                if knapsack[knapsack_capacity - item_weight] + item_value > knapsack[knapsack_capacity]:
                    knapsack[knapsack_capacity] = knapsack[knapsack_capacity - item_weight] + item_value
                    # update the knapsack
                    items[knapsack_capacity] = items[knapsack_capacity - item_weight] + [(item_weight, item_value)]

    return knapsack, items


max_weight = 4
n_items = 3
weights = (1, 2, 3)
values = (1, 4, 6)

print(*zip(*unbounded_knapsack(max_weight, n_items, weights, values)), sep='\n')
