'''
Given Graph input in adjacency list format, do topological sort

toposort works on direct acyclic Graph
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, 
vertex u comes before v in the ordering.

In DFS, we print a vertex and then recursively call DFS for its adjacent vertices. 
In topological sorting, we need to print a vertex before its adjacent vertices.

In DFS, we start from a vertex, we first print it and then recursively call DFS for its adjacent vertices. 
In topological sorting, we use a temporary stack. 
We dont print the vertex immediately, we first recursively call topological sorting for all its adjacent vertices, then push it to a stack. 
Finally, print contents of stack. 
Note that a vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on) are already in stack.
https://www.geeksforgeeks.org/topological-sorting/

'''

from collections import defaultdict
import collections

class Graph:
  def __init__(self,numVertex):
      self.graph=defaultdict(list)
      self.vertex=numVertex

  def addEdge(self,src,dest):
      self.graph[src].append(dest)
 
  def printGraph(self):
      for v in self.graph.keys():
          print "%s -- %s" %(v,self.graph[v])


  def topoSortHelper(self):
       visited=[False]*(self.vertex+1)
       stack=[]
       for v in self.graph.keys():
	   if not visited[v]:
	      self.topoSort(v,visited,stack)

       #Print reverse of stack..why?
       #Because we entered the veritices in reverse order
       #alternative could have been stack.insert(0,v) in topoSort and then print stack as it 

       print stack[::-1]

       ''' 
       #Even below approach is also right
       while(stack):
	   print stack.pop()
       '''

  def topoSort(self,v,visited,stack):
        visited[v]=True
        #Now lets visit all its adjacent neighbors
        for tmpV in self.graph[v]:
            if not visited[tmpV]:
               self.topoSort(tmpV,visited,stack)

        #Add an element into stack after all the adjacent elements are visited
        stack.append(v)


if __name__=="__main__":
	g1 = Graph(9)
	g1.addEdge(2, 3)
	g1.addEdge(1, 3)
	g1.addEdge(2, 4)
	g1.addEdge(3, 5)
	g1.addEdge(4, 6)
	g1.addEdge(5, 6)
	g1.addEdge(6, 7)
	g1.addEdge(7, 9)
	g1.addEdge(8, 9)
	g1.printGraph()
	g1.topoSortHelper()

	#Answer for above should be [8, 2, 4, 1, 3, 5, 6, 7, 9]
