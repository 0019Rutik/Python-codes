import turtle

height=5
width = 7
seurat = turtle.Turtle
turtle.setpos(-250,250)
dot_distance =25
turtle.bgcolor="black"



def spiral(m,n):
    k=0 # row first number m , n

    l=0 # column first number k, l
    f =0

    while(k<m and l<n):
        if(f == 1):
            seurat.right(90)
        for i in range(l,n):
            seurat.forward(dot_distance)
        k+=1
        f=1
        seurat.right(90)
        for i in range(k,m):
            seurat.forward(dot_distance)
        n-=1
        seurat.right(90)

        if(k<n):
            for i in range(n -1,l-1,-1):
                seurat.forward(dot_distance)
            m-=1
        seurat.right(90)
        if(l<n):
            for i in range(m-1,k-1,-1):
                seurat.forward(dot_distance)
            l+=1
        
spiral(20,20)

turtle.done()
            

