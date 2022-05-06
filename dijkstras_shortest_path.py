def dijkstras_shortest_path_algorithm(graph, start_vert):
    visited = {}
    d = {}       # dist
    p = {}       # prev
    for i in graph.vert_list:
        visited[graph.vert_list[i].id] = False
        d[graph.vert_list[i].id] = float('Inf')
        p[graph.vert_list[i].id] = None

    queue = [start_vert]
    visited[start_vert] = True
    d[start_vert] = 0
    while queue:
        temp = queue.pop(0)
        for i in graph.get_vertex(temp).connected_to:
            if not visited[i.id]:
                queue.append(i.id)
                visited[i.id] = True
            if d[i.id] > d[temp] + graph.get_vertex(temp).connected_to[i]:      # change if a shorter path was found
                d[i.id] = d[temp] + graph.get_vertex(temp).connected_to[i]
                p[i.id] = temp

    paths = {}
    for i in d.keys():
        path = [i]
        if i != start_vert:
            temp = i
            while temp != start_vert:    # adding all predecessors to the paths
                temp = p[temp]
                path.insert(0, temp)
            paths[i] = path
    return paths
