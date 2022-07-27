def DFS(alist,v):       #DFS with adjecency
    visited={}
    for i in alist:
        visited[i]=False

    s=[]

    s.append(v)

    vertex_to_be_explored=v

    path=[]

    while(len(s)!=0):
        j=s.pop()
        
        if j not in path:
            path.append(j)
        
        elif j in path:     #leaf node
            continue


        for k in alist[j]:  
                s.append(k)
        print("at j = ",j," path = ",path)


        

    return visited
