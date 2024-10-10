class Solution:
    def countPrimes(self, n: int) :
        primes = [1 for i in range(n)]

        i = 2
        while (i*i<n):
            if primes[i]:
                for j in range (i*i, n, i):
                    primes[j]=0
            i+=1
        
        return sum(primes)-2




if __name__ == "__main__":
    num = 10
    print(Solution().countPrimes(num))
        