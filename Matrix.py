matrix =[[0,4,3],[1,2,4], [7,8,9]]

    

def zeroMatrix(matrix, n, m):
    r0 = n
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if (j==0):
                    r0 =0
                else: 
                    matrix[0][j]=0
    
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if (matrix[0][0]==0):
            for i in range(n):
                matrix[0][j]=0
    if (r0==0):
            for j in range(m):
                matrix[j][0]=0


    # for j in range(m):
    #     if matrix[0][j]==0:
    #         matrix[0][j]=0



    return matrix

    # for i in range(m):


    # a, b = find(0, matrix)
    # for i in range(n):
    #     for j in range(m):
    #         if(i == a):
    #             matrix[a][j]=0
    #         if (j==b):
    #             matrix[i][b]=0
    # return(matrix)
            

print(zeroMatrix(matrix, 3, 3))