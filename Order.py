from time import time

def Next(baseNode, path, backtrack, end, timer):
	if time()-timer > 2:
		return path

	maxConnections = -1
	node = None
	for i, nextNode in enumerate(baseNode.neighbors): 
		con = nextNode.numConnections()
		if con > maxConnections:
			if nextNode.numValues() > 0 and nextNode not in path:
				maxConnections = con
				node = nextNode
			
	if node is not None:
		path.append(node)
		if len(node.neighbors) > 0:
			Next(node, path, backtrack, end, timer)
	elif len(path) >= end:
		return path
	else:
		for neighbor in path[len(path)-backtrack].neighbors:
			if neighbor not in path:
				Next(path[len(path)-backtrack], path, backtrack, end, timer)
			if path[len(path)-backtrack].neighbors.issubset(path):
				backtrack += 1
				if len(path)-backtrack > 0:
					Next(path[len(path)-backtrack], path, backtrack, end, timer)
				else:
					return path
	
	return path 

