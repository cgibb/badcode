#!/usr/bin/env python2
'''
driver, just call Michael's parser from within here
'''

import sys, pygame
from PIL import Image
from pygame.locals import *
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
	data = [Node('hi', 10, 100), Node('hey', 5, 10)]
	data[0].children.append(data[1])
	maxCalls = 10
	maxSteps = 100

	graph = Graph(maxCalls, maxSteps, data)
	frame = Frame(graph)

class Graph():
	def __init__(self, maxCalls, maxSteps, data):
		self.graph = pgv.AGraph(directed=True)
		self.maxCalls = maxCalls
		self.maxSteps = maxSteps
		self.maxSize = 100

		self.processed = []

		self.file = '.tmpfileforbadCODEEDEDE.png'

		self.make(data)

		self.graph.layout()
		self.graph.draw(self.file, 'png')

	# data better be an array of nodes
	def make(self, data):
		if data is None:
			raise Exception('fuck you data is None')
		for node in data:
			self.createNode(node)

	# recursively call so that we can make directed edges
	def createNode(self, node):
		if node.name in self.processed:
			pass
		
		self.processed.append(node.name)
		
		size = self.maxSize * (node.calls // self.maxCalls)
		color = 255 * (node.steps // self.maxSteps)

		self.graph.add_node(node.name)

		for child in node.children:
			self.createNode(child)
			self.graph.add_edge(node.name, child.name)

# node in our graph is just a function call and its stats
# we also track who a node calls, but we do not care about its parent
class Node():
	def __init__(self, name, calls, steps):
		self.name = name
		self.calls = calls
		self.steps = steps
		self.children = []

# actual pygame frame, for now let's just have it wrapped in a class
class Frame():
	def __init__(self, graph):
		pygame.init()
		self.graph = graph
		self.bg = pygame.image.load(graph.file)	

		width, height = getPNGSize(self.graph.file)

		self.bg = pygame.transform.scale(self.bg, (2*width, 2*height))
	
		bgRect = self.bg.get_rect()
		self.size = width, height = bgRect.width, bgRect.height
		self.screen = pygame.display.set_mode(self.size)
		self.screen.blit(self.bg, bgRect)

		pygame.display.update()	

		while True:
			pass

def getPNGSize(img):
	im = Image.open(img)
	size = im.size
	return size[0], size[1]

if __name__ == "__main__":
	sys.exit(main())
