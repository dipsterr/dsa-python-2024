n = 5

def pascal(numRows):

    for i in range(numRows):
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i-j) // (j+1)
        
        print()

            






print(pascal(n))