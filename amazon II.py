def find_dependent_days_sum(n):
    total_sum = 0

    for x in range(n + 1):
        lower_bound = n // (x + 1) + 1
        if x!=0:
            upper_bound = n // x 
        else:
            upper_bound = 0
        if lower_bound <= upper_bound:
            total_sum += x

    return total_sum


n = 13
print(find_dependent_days_sum(n))
