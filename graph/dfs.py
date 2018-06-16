from collections import defaultdict
import collections

class Graph:
    '''
    class for initializing Graph DS
    '''
    def __init__(self):
        self.graph=defaultdict(list)

    '''
    build Adjacency List
    ''' 
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    '''
    Make sure to append the queue and update visited at one shot
    both are atomic operations
    '''
    def bfs(self, vertex):
        visited=[]
        queue=collections.deque()
        queue.append(vertex)
        visited.append(vertex)
        final=[]
        while(queue):
           vertex=queue.popleft()
           visited.append(vertex)
           final.append(vertex)
           for adjv in self.graph[vertex]:
               if adjv not in visited:
	           visited.append(adjv)
	           queue.append(adjv)
        print final


if __name__=="__main__":
	GRAPH1=Graph()
	GRAPH1.add_edge(0,1)
	GRAPH1.add_edge(0,2)
	GRAPH1.add_edge(1,0)
	GRAPH1.add_edge(2,0)
	GRAPH1.add_edge(1,3)
	GRAPH1.add_edge(2,3)
	GRAPH1.add_edge(3,1)
	GRAPH1.add_edge(3,2)
	GRAPH1.add_edge(3,4)
	GRAPH1.add_edge(3,5)
	GRAPH1.add_edge(4,3)
	GRAPH1.add_edge(5,3)
	GRAPH1.add_edge(4,6)
	GRAPH1.add_edge(5,6)
	GRAPH1.add_edge(6,4)
	GRAPH1.add_edge(6,5)
	GRAPH1.bfs(0)

	GRAPH2 = Graph()
	GRAPH2.add_edge(0, 1)
	GRAPH2.add_edge(0, 2)
	GRAPH2.add_edge(1, 2)
	GRAPH2.add_edge(2, 0)
	GRAPH2.add_edge(2, 3)
	GRAPH2.add_edge(3, 3)
	GRAPH2.bfs(0)
