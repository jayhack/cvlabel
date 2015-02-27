import numpy as np
import cv
import cv2

class draw_func(object):
	"""
	Decorator: draw_func
	--------------------
	- copys image to disp_image
	- finds color from color_map and label 
	"""
	default_color_map = {
							#Green
							None:(0,0,255), 
							False:(0,0,255), 
							0: (0, 0, 255),

							#Red
							True:(0,255,0),
							1: (0, 255, 0)
						}

	def __init__(self, color_map=None):
		if color_map is None:
			color_map = self.default_color_map
		self.color_map = color_map


	def __call__(self, f):
		"""decorates"""

		def is_color(color):
			"""returns true if c is an int or a triplet of ints"""
			if not type(color) == int:
				return True
			elif type(color) == tuple and len(color) == 3:
				return True
			else:
				return False

		def parse_color(color_map, label):
			"""dict color map -> color"""
			if color_map is None:
				return (0, 0, 255)
			if not type(color_map) == dict:
				raise TypeError("color_map must be a dict. you used %s" % str(type(color_map)))
			if not all([is_color(k) for k in color_map.values()]):
				raise TypeError("color_map values must all be colors (int or triplet of ints)")
			if not label in color_map:
				raise KeyError("No such color in color_map: %s" % str(label))
			return color_map[label]

		def f_decorated(image, obj, label):
			disp_image = image.copy()
			color = parse_color(self.color_map, label)
			f(disp_image, obj, color)
			return disp_image

		return f_decorated

@draw_func()
def draw_circle(disp_image, obj, color, radius=3, thickness=2):
	"""draws a circle around obj, assuming obj is a (x,y) coordinate"""
	cv2.circle(disp_image, obj, radius, color=color, thickness=thickness)


@draw_func()
def draw_contour(disp_image, obj, label, color_map=None, thickness=2):
	"""draws a circle around obj, assuming obj is a (x,y) coordinate"""
	cv2.circle(disp_image, obj, 5, color=color, thickness=thickness)

