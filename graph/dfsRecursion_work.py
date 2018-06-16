from collections import defaultdict
class Graph:
  def __init__(self):
      self.graph=defaultdict(list)
  
  def addEdge(self,src,dest):
      self.graph[src].append(dest)
      print self.graph

  def dfsUtil(self):
      visited=[False]*20
      dfsQueue=[]
      for v in self.graph.keys():
          if not visited[v]:
             self.dfs(v,visited,dfsQueue)
      print dfsQueue
  
  def dfs(self,v,visited,dfsQueue):
      dfsQueue.append(v)
      visited[v]=True
      for tmpv in self.graph[v]:
          if not visited[tmpv]:
             self.dfs(tmpv,visited,dfsQueue)
      
      


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
g.dfsUtil()


g2 = Graph()
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(1, 2)
g2.addEdge(2, 0)
g2.addEdge(2, 3)
g2.addEdge(3, 3)
g2.dfsUtil()
