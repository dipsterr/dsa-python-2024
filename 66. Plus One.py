class Solution(object):
    def plusOne(self, digits):
        num = ""
        for i in digits:
            num = num+ str(i)
        
        num = int(num)+1

        digits = [int(n) for n in str(num)]

        return digits


if __name__ == "__main__":
    digits = [1,2,3]
    print(Solution().plusOne(digits))
