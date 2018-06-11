# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
         self.label = x
         self.neighbors = []

node1=UndirectedGraphNode('One')
node2=UndirectedGraphNode('two')
node3=UndirectedGraphNode('three')
node4=UndirectedGraphNode('four')
node5=UndirectedGraphNode('five')
node6=UndirectedGraphNode('six')
node7=UndirectedGraphNode('seven')

node1.neighbors.extend([node2,node3])
node2.neighbors.extend([node1,node4])
node3.neighbors.extend([node1,node4])
node4.neighbors.extend([node5,node6,node2,node3])
node5.neighbors.extend([node4,node7])
node6.neighbors.extend([node4,node7])
node7.neighbors.extend([node5,node6])

'''''
                            +--------+                                                     
                            |        |                                                     
            +---------------| Node1  |-----------------+                                   
            |               |        |                 |                                   
            |               +--------+                 |                                   
            |                                          |                                   
       +---------+                               +-----|----+                              
       |         |                               |          |                           -  
       | Node2   |                               |Node3     |                              
       |         |                               |          |                              
       |         |                               |          |                              
+      +---------+                               +------|---+                              
            |                                           |                                  
            |                                           |                                  
            |                                           |                                  
            |               +--------+                  |                                 +
            +---------------|        |------------------+                                  
                            | Node4  |                                                     
             +---------------        |-----------------++                                  
             |              +--------+                 |                                   
             |                                         |                                   
             |                                         |                                   
             |                                         |                                   
             |                                         |                                   
      +-----------+                               +----------+                             
      |           |                               | Node6    |                             
      | Node5     |                               |          |                             
      |           |                               +-----+----+                             
      +-----------+                                     |                                  
           +   |                                        |                                  
               |                                        |                                  
               |            +-----------+               |                                  
               ++------------ Node7     |---------------+                                  
                            |           |                                                  
                            +-----------+         


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
         self.label = x
         self.neighbors = []
'''''

import collections
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
           return None
        cNode=None
        q=collections.deque()
        q.append(node)    
        return clone_Graph(node,q,cNode,map={})


def clone_Graph(node,q,cNode,map):
    while q:
       tnode=q.popleft()
       if tnode not in map:
          cNode=UndirectedGraphNode(tnode.label)
          map[tnode]=cNode
       for n in tnode.neighbors:
           if n not in map:
              cNode=UndirectedGraphNode(n.label)       
              map[n]=cNode
              map[tnode].neighbors.append(cNode)
              q.append(n)
           else:
              map[tnode].neighbors.append(map[n])
    return map[node]


def bfsGraph(node):
    visited=[node]
    map={}
    q=collections.deque()
    q.append(node)
    while(q):
       tnode=q.popleft()
       if tnode.label not in map:
          map[tnode.label]=[]
       for n in tnode.neighbors:
           if n not in visited:
              map[n.label]=[]
              map[tnode.label].append(n.label)
              visited.append(n)
              q.append(n)
           else:
              map[tnode.label].append(n.label)
    for key in map:
        print "node %s : neighbors %s" %(key,map[key])
    for v in visited:
        print v.label
       

def dfsSearch(node):
    visited=[node]
    map={}
    q=[]
    q.append(node)
    while(q):
       tnode=q.pop()
       if tnode.label not in map:
          map[tnode.label]=[]
       for n in tnode.neighbors:
           if n not in visited:
              map[n.label]=[]
              map[tnode.label].append(n.label)
              visited.append(n)
              q.append(n)
           else:
              map[tnode.label].append(n.label)
    for key in map:
        print "node %s : neighbors %s" %(key,map[key])
    for v in visited:
        print v.label



s=Solution()
newG=s.cloneGraph(node1)
bfsGraph(newG)
