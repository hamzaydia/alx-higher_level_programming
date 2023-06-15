#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    total_weight = 0
    weighted_sum = 0

    for value, weight in my_list:
        weighted_sum += value * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return weighted_sum / total_weight
