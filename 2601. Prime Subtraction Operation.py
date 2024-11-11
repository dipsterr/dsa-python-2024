from math import sqrt
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(n):
            for i in range(2, int(sqrt(n))+1):
                if n%i == 0:
                    return False
            return True

        prev = 0
        for n in nums:
            upperBound = n - prev
            largestPrime = 0
            for i in reversed(range(2, upperBound)):
                if isPrime(i):
                    largestPrime = i
                    break
            if n-largestPrime <= prev:
                return False
            prev = n - largestPrime
        return True
        
if __name__ == "__main__":
   nums = [4,9,6,10]
   print(Solution().primeSubOperation(nums))

# for i in reversed(range(2, 9)):
#     print(i)

# for i in range(9,2,-1):
#     print(i)