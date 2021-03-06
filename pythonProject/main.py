class Node:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None
		self.parent = None


class Binary_search_tree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.value:
			if cur_node.left_child is None:
				cur_node.left_child = Node(value)
				cur_node.left_child.parent = cur_node
			else:
				self._insert(value, cur_node.left_child)
		elif value > cur_node.value:
			if cur_node.right_child is None:
				cur_node.right_child = Node(value)
				cur_node.right_child.parent = cur_node
			else:
				self._insert(value, cur_node.right_child)
		else:
			print("Value already in tree!")

	def print_tree(self):
		if self.root != None:
			self._print_tree(self.root)

	def _print_tree(self,cur_node):
		if cur_node != None:
			self._print_tree(cur_node.left_child)
			print(str(cur_node.value))
			self._print_tree(cur_node.right_child)


# main программа
binary_tree = Binary_search_tree()
binary_tree.insert(50)
binary_tree.insert(55)
binary_tree.insert(45)
binary_tree.insert(45)
binary_tree.print_tree()