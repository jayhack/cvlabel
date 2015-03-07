import numpy as np
import cv2

from cvlabel import ClickLabeler
from cvlabel import draw_circle
from cvlabel import euclidean_distance
from cvlabel import boolean_flip_label


if __name__ == '__main__':


	def get_random_points(image, n=4):
		"""returns a list of n random (x,y) coordinates"""
		xtop, ytop, nchannels = image.shape
		xs = np.random.randint(0, xtop, (n,1))
		ys = np.random.randint(0, ytop, (n,1))
		return [(int(xs[i]), int(ys[i])) for i in range(n)]

	labeler = ClickLabeler(get_random_points, draw_circle, euclidean_distance, boolean_flip_label)

	for i in range(5):
		image = np.zeros((400, 400, 3)).astype(np.uint8)
		objs, labels = labeler.label(image)
		print 'Final labels: ', labels

