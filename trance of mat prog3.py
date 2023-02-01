a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
x=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range (len(a)):
        x[j][i]=a[i][j]
for result in x:
    print(result)
