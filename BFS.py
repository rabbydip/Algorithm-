graph= {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start,explored):
   # keep track of all visited nodes

   # keep track of nodes to be checked
   queue = [start]

   # keep looping until there are nodes still to be checked
   while queue:
       # pop shallowest node (first node) from queue
       node = queue.pop(0)
       if node not in explored:
           # add node to list of checked nodes
           explored.append(node)
           neighbours = graph[node]

           # add neighbours of node to queue
           for neighbour in neighbours:
               queue.append(neighbour)
   return explored

explored=bfs_connected_component(graph,'A',[])
print(explored)
# returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']