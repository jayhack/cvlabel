import numpy as np
import cv2
from CVLabeler import CVLabeler

if __name__ == '__main__':

	def get_objects(image, npoints=4):
		"""returns 'npoints' random (x,y) coordinates"""
		xtop, ytop = image.shape
		xs = np.random.randint(0, xtop, (npoints,1))
		ys = np.random.randint(0, ytop, (npoints,1))
		return [(int(xs[i]), int(ys[i])) for i in range(npoints)]

	def draw_object(image, obj):
		"""draws a small circle around obj"""
		disp_img = image.copy()
		cv2.circle(disp_img, obj, 2, color=255, thickness=1)
		return disp_img

	images = [np.zeros((400, 400)).astype(np.uint8) for i in range(3)]

	labeler = CVLabeler(get_objects, draw_object)
	for image in images:
		labeler.label(image)

