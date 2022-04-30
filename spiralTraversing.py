
def spiral(m, n, a):
    # spiral(row, col , matrix)
    K=0 
    l=0

    '''
    k - index of starting row
    l - index of starting column    -*/
    '''

    while(K < n and l < n):
    #printing  the fiirst row ffrom the remaining row..
    

        
    # 4 printing the first column from the reaminung columns
            for i in range (m-1, K-1,-1):
                print(a[i][l] , end=" ")
            l+=1

a = []
count = 1
for i in range(4):
    l = []
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
spiral(4,4,a)
