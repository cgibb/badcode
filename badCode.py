#!/usr/bin/env python2
'''
driver, just call Michael's parser from within here
'''

import sys, pygame

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

	# and then it just boils down to drawing the darn thing
	data = [Node("here", 10, 100)]

	# figure this out while parsing so that we can scale the images better
	maxCalls = 10
	maxSteps = 100

	frame = Frame(maxCalls, maxSteps)
	frame.create(data)

	# troll
	while True:
		pass

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
	def __init__(self, maxCalls, maxSteps):
		pygame.init()

		self.maxCalls = maxCalls
		self.maxSteps = maxSteps
		self.maxRadius = 100
		self.maxRed = 255

		self.processed = []	
		self.font = pygame.font.SysFont("monospace", 18)

	# MEESH, use a pmquad tree to organize the nodes in our grid nicely
	def create(self, data):
		if data is None:
			raise Exception('data is none')
		self.length = len(data)*2*self.maxRadius
		self.screen = pygame.display.set_mode((self.length, self.length))
		self.screen.fill((255, 255, 255))

		self.draw_node(data[0], 100, 100)

		pygame.display.update()
	# drawing idea, (x,y) found from data structure
	def draw_node(self, node, x, y):
		self.processed.append(node.name)
		
		radius = self.maxRadius * (self.maxCalls // node.calls)
		red = self.maxRed * (self.maxSteps / node.steps)
		pygame.draw.circle(self.screen, (red, 0, 0), (x, y), radius, 0)	
		
		label = self.font.render(node.name, 1, (255, 255, 255))
		self.screen.blit(label, (x, y))
		

if __name__ == "__main__":
	sys.exit(main())
