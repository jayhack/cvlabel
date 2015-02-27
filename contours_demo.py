import numpy as np
import cv2
from CVLabeler import CVLabeler

if __name__ == '__main__':

	def get_objects(image, npoints=4):
		"""returns 'npoints' random (x,y) coordinates"""
		xtop, ytop, nchannels = image.shape
		xs = np.random.randint(0, xtop, (npoints,1))
		ys = np.random.randint(0, ytop, (npoints,1))
		return [(int(xs[i]), int(ys[i])) for i in range(npoints)]


	def draw_object(image, obj, label):
		"""draws a small circle around obj"""
		disp_img = image.copy()
		colors = {
					None:(0, 0, 255),
					False:(0, 0, 255),
					True:(0, 255, 0)
				}
		cv2.circle(disp_img, obj, 5, color=colors[label], thickness=3)
		return disp_img


	def get_distance(obj, x, y):
		"""returns distance from object to x, y"""
		return (obj[0]-x)**2 + (obj[1]-y)**2


	def update_object(event, label):
		"""flips label (works with None as well)"""
		return not label


	images = [np.zeros((400, 400, 3)).astype(np.uint8) for i in range(3)]

	labeler = CVLabeler(get_objects, draw_object, get_distance, update_object)
	for image in images:
		labeler.label(image)

