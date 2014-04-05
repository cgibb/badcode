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
	# and then create the tree...


	# and then it just boils down to drawing the darn thing
	tree = None

	frame = Frame()
	frame.create(tree)

# node in our graph is just a function call and its stats
# we also track who a node calls, but we do not care about its parent
class Node():
	def __init__(self, name, calls, steps):
		self.name = name
		self.calls = call
		self.steps = steps
		self.children = []

# actual pygame frame, for now let's just have it wrapped in a class
class Frame():
	def __init__(self):
		pygame.init()

if __name__ == "__main__":
	sys.exit(main())
