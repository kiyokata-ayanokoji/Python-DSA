def BFS(alist,vertice):             #BFS using adjecency list 
    visited={}
    for i in alist:
        visited[i]=False

    q=[]

    visited[vertice]=True       #starting vertex
    q.append(vertice)

    
    level=0
    while(len(q)!=0):
        v=q.pop(0)
        for neighbour in alist[v]:
            #print("checking ",neighbour)
            if visited[neighbour]==False:
                visited[neighbour]=True
                q.append(neighbour)
                
        level=level+1
   

    visited_vertices=[]
    for i in visited:
        if visited[i]==True:
            visited_vertices.append(i)
    
    print("level = ",level)

    return visited_vertices
