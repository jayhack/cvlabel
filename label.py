import numpy as np

from decorators import TypeValidatingDecorator

class label_func(TypeValidatingDecorator):
	"""
	Decorator: label_func
	---------------------
	- validates type of label
	"""
	def __init__(self, valid_types=None):
		"""parses valid_types"""
		super(label_func, self).__init__(valid_types)


	def __call__(self, f):
		"""decorates"""

		def f_decorated(event, label):
			self.validate_type(label)
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
