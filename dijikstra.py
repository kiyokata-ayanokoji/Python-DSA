def dijkstra(Wlist,s):
    
    infinity=max([d for u in Wlist.keys() for (v,d) in Wlist[u] ])*len(Wlist.keys()) +1

    print(infinity)
    
    #initialization of vertices and distances
    (visited,distance,parent)=({},{},{})

    for i in Wlist.keys():
        (visited[i],distance[i])=(False,infinity)
    

    distance[s]=0

    for u in Wlist.keys():
        nextd=min([distance[v] for v in Wlist.keys() if visited[v]==False])                         #selecting the minimum distance
        nextvlist = [v for v in Wlist.keys() if (visited[v]==False) and distance[v]==nextd]         #selecting the list of vertices that have the minimum distance

        if nextvlist==[]:
            break

        nextv=min(nextvlist)                                                                        #selecting the vertex in the list (smallest number vertex)

        visited[nextv]=True                                                                         #setting it as visited

        for (v,d) in Wlist[nextv]:
            if not visited[v]:
                distance[v]=min(distance[v],distance[nextv]+d)                                      #updating the next distances connecting through the vertex
                
                if distance[v]==distance[nextv]+d:
                    parent[v]=nextv

    return(distance,parent)
