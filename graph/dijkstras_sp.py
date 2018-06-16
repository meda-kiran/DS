'''
Python program for Dijkstra's single 
source shortest path algorithm. The program is 
or adjacency matrix representation of the graph

algorithm is given below with Time complexity of O(V^2). 
There are also some time-efficient Algorithms: 
Graph represented using adjacency list can be reduced to O(E log V) with the help of binary heap (TBD)
'''


# Library for INT_MAX
import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
 
    def printSolution(self, dist):
        print "Vertex tDistance from Source"
        for node in range(self.V):
            print node,"t",dist[node]

    def find_min(self,dist,spfset):
        min=(sys.maxint)
        min_index=-1
        for v in range(self.V):
            if dist[v]<min and spfset[v]==False:
               min_index=v
               min=dist[v]
        return min_index

    def dj(self,src):
        '''
        spfset will store vertices selected to be part of shortent path so far
        dist will store short distance from src to given vertex so far
        initialize distance from src to src to zero
        adjacencies can be found by checking graph[i][j]>0
        '''
        dist=[sys.maxint]*self.V
        spfset=[False]*self.V
        dist[src]=0
        # loop exactly for # of vertices
        for currV in range(self.V):
            minv=self.find_min(dist,spfset)
            spfset[minv]=True
            for v in range(self.V):
                if self.graph[minv][v]>0 and spfset[v]==False and dist[v]>(dist[minv]+self.graph[minv][v]):
                    dist[v]=dist[minv]+self.graph[minv][v] 
        self.printSolution(dist)     
              

if __name__=='__main__':
	g  = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		   [4, 0, 8, 0, 0, 0, 0, 11, 0],
		   [0, 8, 0, 7, 0, 4, 0, 0, 2],
		   [0, 0, 7, 0, 9, 14, 0, 0, 0],
		   [0, 0, 0, 9, 0, 10, 0, 0, 0],
		   [0, 0, 4, 14, 10, 0, 2, 0, 0],
		   [0, 0, 0, 0, 0, 2, 0, 1, 6],
		   [8, 11, 0, 0, 0, 0, 1, 0, 7],
		   [0, 0, 2, 0, 0, 0, 6, 7, 0]
		  ];
	 
	g.dj(0);
