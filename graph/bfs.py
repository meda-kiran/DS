from collections import defaultdict
import collections

class Graph:
  def __init__(self):
      self.graph=defaultdict(list)

  '''
  build Adjacency List
  ''' 
  def addEdge(self,src,dest):
      self.graph[src].append(dest)

  '''
  Make sure to append the queue and update visited at one shot
  both are atomic operations
  '''
  def bfs(self,v):
      visited=[]
      q=collections.deque()
      q.append(v)
      visited.append(v)
      final=[]
      while(q):
         v=q.popleft()
         visited.append(v)
         final.append(v)
         for adjv in self.graph[v]:
             if adjv not in visited:
                visited.append(adjv)
                q.append(adjv)
      print final

if __name__=="__main__":
	g=Graph()
	g.addEdge(0,1)
	g.addEdge(0,2)
	g.addEdge(1,0)
	g.addEdge(2,0)
	g.addEdge(1,3)
	g.addEdge(2,3)
	g.addEdge(3,1)
	g.addEdge(3,2)
	g.addEdge(3,4)
	g.addEdge(3,5)
	g.addEdge(4,3)
	g.addEdge(5,3)
	g.addEdge(4,6)
	g.addEdge(5,6)
	g.addEdge(6,4)
	g.addEdge(6,5)
	g.bfs(0)

	g2 = Graph()
	g2.addEdge(0, 1)
	g2.addEdge(0, 2)
	g2.addEdge(1, 2)
	g2.addEdge(2, 0)
	g2.addEdge(2, 3)
	g2.addEdge(3, 3)
	g2.bfs(0)
