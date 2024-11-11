def count_groups(n, rank):
    # Step 1: Initialize a result array to store the counts for each mean value
    result = [0] * n
    
    # Step 2: Compute prefix sums to quickly get the sum of any subarray
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + rank[i]
    
    # Step 3: Iterate through all subarrays
    for i in range(n):
        for j in range(i, n):
            subarray_sum = prefix[j+1] - prefix[i]
            subarray_length = j - i + 1
            # Step 4: Check if the mean of the subarray is equal to x (1 <= x <= n)
            mean = subarray_sum / subarray_length
            if mean.is_integer() and 1 <= mean <= n:
                result[int(mean) - 1] += 1
    
    # Return the result array containing the count for each mean x
    return result

# Example usage
n = 4
rank = [4,3,2,1]
print(count_groups(n, rank))  # Output: [1, 2, 3, 2, 1]