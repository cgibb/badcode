#!/usr/bin/env python2
'''
driver, just call Michael's parser from within here
'''

import sys, pygame
import pygraphviz as pgv

def main(argv=None):
	if argv is None:
		sys.argv
	
	######
	# TODO call Michael's stuff herezzzzzz
	######

	# TODO
	# we could just directly create our graph,
	# or we could be modular and have a parser
	# and then create the the data structure we want...

	# a simple array should do just fine since order may not matter
	data = None
	maxCalls = 10
	maxSteps = 100

	graph = Graph(maxCalls, maxSteps)
	graph.make(data)

	frame = Frame(graph)

class Graph():
	def __init__(self, maxCalls, maxSteps):
		self.graph = pgv.AGraph(directed=True))
		self.maxCalls = maxCalls
		self.maxSteps = maxSteps
	
		self.graph.layout()

	# data better be an array of nodes
	def make(self, data):
		if data is None:
			raise Exception('fuck you data is None')

# node in our graph is just a function call and its stats
# we also track who a node calls, but we do not care about its parent
class Node():
	def __init__(self, name, calls, steps):
		self.name = name
		self.calls = calls
		self.steps = steps
		self.children = []
		self.parents = []

# actual pygame frame, for now let's just have it wrapped in a class
class Frame():
	def __init__(self, graph):
		pygame.init()
		self.graph
		self.file = '.tmpfileforbadCODEEDEDE.png'

		self.graph.draw(self.file, 'png')
		

if __name__ == "__main__":
	sys.exit(main())
