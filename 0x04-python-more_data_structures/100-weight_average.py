#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        mult_elem = 0
        sum_weight = 0
        for score, weight in my_list:
            mult_elem = mult_elem + (score * weight)
            sum_weight += weight
        return (mult_elem / sum_weight)
    return (0)
