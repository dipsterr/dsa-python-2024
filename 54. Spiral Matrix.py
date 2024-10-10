class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        
        top, left= 0, 0
        bottom, right= n-1, m-1

        # Loop until all elements are not traversed
        while (top <= bottom and left <= right):

            # For moving left to right
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            # For moving top to bottom
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1

            # For moving right to left
            if (top <= bottom):
                for i in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom -=1

            # For moving bottom to top
            if (left <= right):
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left += 1
            
        return ans

if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(arr))
       