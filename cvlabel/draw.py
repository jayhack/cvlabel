import numpy as np
import cv
import cv2

from decorators import TypeValidatingDecorator


class draw_func(TypeValidatingDecorator):
	"""
	Decorator: draw_func
	--------------------
	- copys image to disp_image
	- finds color from color_map and label 
	"""
	def __init__(self, valid_types=None, color_map=None):
		"""sets self.valid_types, self.color_map"""
		super(draw_func, self).__init__(valid_types)

		if color_map is None:
			color_map = self.default_color_map()
	
		self.color_map = color_map
		if not type(self.color_map) == dict:
			raise TypeError("color_map must be a dict. you used %s" % str(type(self.color_map)))
		if not all([self.is_color(k) for k in self.color_map.values()]):
			raise TypeError("color_map values must all be colors (int or triplet of ints)")


	def default_color_map(self):
		"""constructs and returns a default color map"""
		falses = [None, False, 0, 0.0]
		trues = [True, 1, 1.0]
		pure_colors = {
						'blue':(255, 0, 0),
						'red':(0, 0, 255),
						'green':(0, 255,0)
						}
		return dict(
						{k:pure_colors['red'] for k in falses}.items() +
						{k:pure_colors['green'] for k in trues}.items()
					)


	def is_color(self, color):
		"""returns true if c is an int or a triplet of ints"""
		if type(color) == int:
			return True
		elif type(color) == tuple and len(color) == 3:
			return True
		return False


	def parse_color(self, label):
		"""dict color map -> color"""
		if not label in self.color_map:
			raise KeyError("No such color in color_map: %s" % str(label))
		return self.color_map[label]


	def __call__(self, f):
		"""decorates"""

		def f_decorated(image, obj, label):
			self.validate_type(obj)
			disp_image = image.copy()
			color = self.parse_color(label)
			f(disp_image, obj, color)
			return disp_image

		return f_decorated


@draw_func(valid_types=[tuple])
def draw_circle(disp_image, obj, color, radius=3, thickness=2):
	"""draws a circle around obj, assuming obj is a (x,y) coordinate"""
	cv2.circle(disp_image, obj, radius, color=color, thickness=thickness)


@draw_func(valid_types=np.ndarray)
def draw_contour(disp_image, obj, color, thickness=2):
	"""draws contour"""
	cv2.drawContours(disp_image, [obj], -1, color, thickness)

