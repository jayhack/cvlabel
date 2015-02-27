import numpy as np
import cv
import cv2


def euclidean_distance(obj, x, y):
	"""distance from obj to x, y, assuming obj is a (x,y) coordinate"""
	if not ((type(obj) == tuple) or (type(obj) == list)) and len(obj) == 2:
		raise TypeError("euclidean_distance is for objects represented as (x,y); you used %s" % str(type(obj)))
	return (obj[0]-x)**2 + (obj[1]-y)**2


def contour_distance(obj, x, y):
	"""projection of (x,y) onto obj, assuming obj is a contour"""
	raise NotImplementedError

