a=[[1,2,3],
   [4,5,6,],
   [7,8,9]]
b=[[2,4,5],
   [3,4,2],
   [4,3,1]]
r=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        r[i][j]=a[i][j]+b[i][j]
for n in r:
    print(n)
    

   
   
