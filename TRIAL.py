def find_group_id(PFR):
    group_id = 0
    n = len(PFR)
    group_id = 0

    for i in range(n):
        score = 15  # Assume the score is 15 initially

        # Check if there's a student behind with a higher PFR
        for j in range(i+1, n):
            if PFR[j] > PFR[i]:
                score = 10  # Found a student with higher PFR
                # Check if there's a student behind this student with a smaller PFR
                for k in range(j+1, n):
                    if PFR[k] < PFR[j]:
                        score = 5  # Found a student with a smaller PFR
                        break
                break

        group_id += score

    return group_id

# Example usage
pfrs = [13,9,1,3,7,4,2,12,6,5]
print(find_group_id(pfrs))  # Output: The group ID based on the PFRs
