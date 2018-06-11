from collections import defaultdict
import collections

class Graph:
  def __init__(self):
      self.graph=defaultdict(list)
  
  def addEdge(self,src,dest):
      self.graph[src].append(dest)
      print self.graph

  def DFS(self,v):
      visited=[False]*(len(self.graph))
      q=collections.deque()
      self.prev={}
      q.append(v)
      visited[v]=True
      self.prev[v]=0
      while q:
          node=q.pop()
          print "popped node:%s" %node
          for tmpNode in self.graph[node]:
              if not visited[tmpNode]:
                 self.prev[tmpNode]=node
                 q.append(tmpNode)
                 visited[tmpNode]=True
  def path(self,a,b):
      if not self.prev:
         print "Prev dict is not set"
         return
      else:
         path=[]
         path.append(b)
         next=b
         while(next!=a):
            next=self.prev[next]
            path.append(next)
         print path
               
   

  def BFS(self,v):
      visited=[False]*(len(self.graph))
      q=collections.deque()
      q.append(v)
      visited[v]=True
      while q:
          node=q.popleft()
          print "popped node:%s" %node
          for tmpNode in self.graph[node]:
              if not visited[tmpNode]:
                 q.append(tmpNode)
                 visited[tmpNode]=True  

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
g.DFS(0)
g.path(2,6)

g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.addEdge(2, 3)
g2.addEdge(3, 3)
g2.DFS(0)
