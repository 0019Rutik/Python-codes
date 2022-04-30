import turtle

turtle.bgcolor("black")
seurat = turtle.Turtle()

width=5
height = 7

dot_distance = 25
seurat.setpos(-250,250)


def spiralT(m,n):
    k=0
    l=0
    f = 0
    seurat.color("white")

    while(k < m and l < n):
        if(f == 1):
            seurat.right(90)
          #the first row from the remmaining row
        for i in range(l , n): 
            seurat.forward(dot_distance) 

             #print(a[k][i],end =" ")
        # row index increase
        k+=1
        f=1
        seurat.right(90)
         #printing the last colum from thr remaining coilumn
        for i in range(k,m):
             #print(a[i][n-1] , end=" ")
            seurat.forward(dot_distance)


        n-=1
        #col decrease
        seurat.right(90)


        if(k< n):
          #printingg the last row           
            for i in range(n-1, l-1,-1):

               # print(a[m-1][i] , end=" ")
                seurat.forward(dot_distance)
            #row minus
            m-=1
        seurat.right(90)
        if(l<n):
            #printing the last column
            for i in range (m-1, k-1,-1):
                 #print(a[i][l] , end=" ")
                seurat.forward(dot_distance)
            #col index increase
            l+=1
# # a = []
# count =1
# for i in range(4):
#     l = []
#     for j in  range(4):
#         l.append(count)
#         count+=1
#     a.append(l)
spiralT(20,20)
turtle.done()