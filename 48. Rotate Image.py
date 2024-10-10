class Solution(object):
    def rotate(self, matrix):
        # Brute Force
        # n = len(matrix)
        # rotated =  [[0 for i in range(n)] for i in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n-i-1]= matrix [i][j]
        # return rotated

        # optimal approach

        n = len(matrix)
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i]
        
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(arr)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()

