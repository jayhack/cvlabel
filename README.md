# cvlabel
Jay Hack (jhack@stanford.edu), Winter 2015


## Overview
This python module allows one to easily and intuitively mark images via OpenCV's image display interface. Merely define how to extract objects from an image, how to draw them on the image and how to assign labels.


## Setup
You will need to install OpenCV with Python bindings; this is not covered in setup.py.
```
	~$: git clone git@github.com:jayhack/cvlabel.git
	~$: python setup.py install
```

## Example Usage

(Note that all of the below functions are already implemented for you)

```
	import numpy as np
	import cv2

	def get_random_points(image, n=4):
		"""returns a list of n random (x,y) coordinates"""
		xtop, ytop, nchannels = image.shape
		xs = np.random.randint(0, xtop, (n,1))
		ys = np.random.randint(0, ytop, (n,1))
		return [(int(xs[i]), int(ys[i])) for i in range(n)]

	def draw_circle(image, obj, color, radius=3, thickness=2):
		"""draws a circle around obj, assuming obj is a (x,y) coordinate"""
		disp_image = image.copy()
		cv2.circle(disp_image, obj, radius, color=color, thickness=thickness)
		return disp_image

	def euclidean_distance(obj, x, y):
		"""distance from obj to x, y, assuming obj is a (x,y) coordinate"""
		return (obj[0]-x)**2 + (obj[1]-y)**2

	def boolean_flip_label(event, label):
		"""{None, False} -> True; True -> False"""
		return not label 

	labeler = CVLabeler(get_random_points, draw_circle, euclidean_distance, boolean_flip_label)
	labeler.label(cv2.imread('test.jpg'))
```