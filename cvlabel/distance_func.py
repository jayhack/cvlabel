import numpy as np
import cv
import cv2

from decorators import TypeValidatingDecorator

class distance_func(TypeValidatingDecorator):
	"""
	Decorator: distance_func
	------------------------
	- validates types
	"""
	def __init__(self, valid_types=None):
		"""parses valid types"""
		super(distance_func, self).__init__(valid_types)

	def __call__(self, f):
		"""decorates"""

		def f_decorated(obj, x, y):
			self.validate_type(obj)
			return f(obj, x, y)

		return f_decorated


@distance_func(valid_types=tuple)
def euclidean_distance(obj, x, y):
	"""distance from obj to x, y, assuming obj is a (x,y) coordinate"""
	return (obj[0]-x)**2 + (obj[1]-y)**2


@distance_func(valid_types=np.ndarray)
def contour_distance(obj, x, y):
	"""projection of (x,y) onto obj, assuming obj is a contour"""
	contour = obj[:, 0, :]
	c = np.array([x, y])
	dists = np.sum((contour - c)**2, axis=1)
	return np.min(dists)


