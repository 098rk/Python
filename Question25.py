# 25: Write a program to add two matrices of size n x m

Matrix_1=[[1,2,3],
          [4,5,6]]

Matrix_2= [[9,8,7],
           [6,5,4]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(Matrix_1)):
    for j in range(len(Matrix_2)):
        result[i][j]=Matrix_1[i][j]+Matrix_2[i][j]

for r in result:
    print(r)


