import  numpy as np

x=int(input('size of matrix : '))

print('identity matrix with numpy : \n' ,np.identity(x),'\n')

print('identity matrix without numpy : \n')
for i in range(0,x):
    for j in range(0,x):
        if(i==j):
            print(1,end=' ')
        else:
            print(0 ,end=' ')
    print('')



