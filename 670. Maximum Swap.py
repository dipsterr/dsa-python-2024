class Solution:
    def maximumSwap(self, num: int) -> int:
        if sorted(str(num),reverse=True) == list(str(num)):
            return num
        num=list(str(num))
        for i in range(len(num)):
            arr=num[i+1:]
            maxNum = max(arr)

            if num[i]<maxNum:
                num[i], num[i+1+arr.index(maxNum)] = num[i+1+arr.index(maxNum)], num[i]
                break
        return int("".join([i for i in num]))

    
if __name__=="__main__":
    num = 1234
    print(Solution().maximumSwap(num))