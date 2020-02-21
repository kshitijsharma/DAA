from MinHeap import minheap
from Tree import tree

class huffman(object):
	__slots__ = ['_symbol','_probability','_root']

	def __init__(self,symbol,probability,treeNode=None):
		self._symbol = symbol
		self._probability = probability
		
		if treeNode is None:		
			self._root = tree()
		else:
			self._root= treeNode
	
	def __lt__(self,obj):
		if self._probability < obj.getProb():
			return True
		return False

	def __gt__(self,obj):
		if self._probability > obj.getProb():
			return True
		return False
 	
	def getProb(self):
		return self._probability

	def getTree(self):
		return self._root

	def getSym(self):
		return self._symbol

input = [huffman('a',0.40),huffman('b',0.16),huffman('c',0.15),huffman('d',0.19),huffman('e',0.040)]

heap = minheap(huffman('*',0.00))

for sym in input:
	heap.insert(sym)

while len(heap) > 1:
	h1 = heap.delete()
	h2 = heap.delete()

	newTree = tree()
	newTree.setLeft(h1)
	newTree.setRight(h2)

	#Star Represents Combined Symbols
	newSym = huffman('*',h1.getProb() + h2.getProb(),newTree)

	heap.insert(newSym)
	

ansTree = heap.delete()


def printCode(string,treeNode):
	if treeNode is None:
		return
	if treeNode.getTree().getLeft()is not None:
		printCode(string+'1',treeNode.getTree().getLeft())
	if treeNode.getSym() != '*':
		print('| %-6s | %-11.2f | %-7s |' %(treeNode.getSym(),treeNode.getProb(),string))
	
	if treeNode.getTree().getRight() is not None:
		printCode(string+'0',treeNode.getTree().getRight())


print('| Symbol | Probability |   Code  |')

printCode('',ansTree)
		
