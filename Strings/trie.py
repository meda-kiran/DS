'''
Trie operations:

1. Add a string
2. Delete a string
3. Check membership of a string
4. check prefix match in the list of strings for a given prefix
'''

class TrieNode(object):
      def __init__(self):
          self.children={}
          self.end_of_word=False


class Trie(object):
      def __init__(self):
          self.root=TrieNode()
      
      def add(self,w):
          '''
          adding a given word w to the Trie
          '''
          currentNode=self.root
          for c in w:
              if c not in currentNode.children:
                 node=TrieNode()
                 currentNode.children[c]=node
              currentNode=currentNode.children[c]
          currentNode.end_of_word=True
 
      def traversal(self,node,list=[]):
          '''
          traverse the trie tree and dump the characters
          '''
          for char in node.children:
              list.append(char)
              self.traversal(node.children[char])
          return list     
     
      def isMember(self,w):
          '''
          given a word w, check if it is member of Trie
          '''
          currentNode=self.root
          for c in w:
              if c not in currentNode.children:
                 return False
              currentNode=currentNode.children[c]
          return currentNode.end_of_word

      def prefixMatch(self,p=''):
          '''
          For a given prefix, return all the strings that match in a Trie
          '''
          currentNode=self.root
          matchStrings=[]
          for c in p:
              if c not in currentNode.children:
                 return []
              currentNode=currentNode.children[c]
          path=list(p)
          output=[]
          self._collectStrings(currentNode,path,output)
          return output

      def _collectStrings(self,currentNode,path,output): 
          '''
          dump all the strings from given node
          '''
          if currentNode.end_of_word:
             output.append(''.join(path))
          for char,child in currentNode.children.iteritems():
              path.append(char)
              self._collectStrings(child,path,output)
              path.pop()
           

if __name__ == "__main__":
   words=["AB","ABC","BAT","CAT","CUP","CUT","ABCD"]
   t=Trie()
   for word in words:
       t.add(word)
   #print t.traversal(t.root)
   print "Pattern: AB: %s" %(t.prefixMatch('AB'))
   print "Pattern: CA: %s" %(t.prefixMatch('CA'))
   print "Pattern: CU: %s" %(t.prefixMatch('CU'))
