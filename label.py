import numpy as np


class label_func(object):
	"""
	Decorator: label_func
	---------------------
	- validates type of label 
	"""
	def __init__(self, valid_types=None):
		"""parses valid_types"""
		if not valid_types is None:
			if not type(valid_types) in [list, tuple]:
				valid_types = [valid_types]
		self.valid_types = valid_types

	def __call__(self, f):
		"""decorates"""

		def validate_label(label):
			"""raises assertion if label is incorrect type"""
			if self.valid_types is None:
				return
			elif not type(label) in self.valid_types:
				raise TypeError("Incompatible label type: %s" % str(type(label)))

		def f_decorated(event, label):
			validate_label(label)
			return f(event, label)

		return f_decorated



@label_func(valid_types=[type(None), bool])
def boolean_flip_label(event, label):
	"""boolean flip of label, including None"""
	return not label


@label_func(valid_types=int)
def increment_label(event, label):
	"""adds one to label"""
	return label + 1