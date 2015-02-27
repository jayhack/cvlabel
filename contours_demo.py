import numpy as np
import cv2

from CVLabeler import CVLabeler
from distance import contour_distance
from draw import draw_contour
from label import boolean_flip_label

if __name__ == '__main__':

	def get_contours(image):
		"""returns contours from image (list of np.ndarray)"""
		imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		ret, thresh = cv2.threshold(imgray,127,255,0)
		contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		return [c for c in contours if len(c) > 200]


	labeler = CVLabeler(get_contours, draw_contour, contour_distance, boolean_flip_label)
	image = cv2.imread('lena.bmp')
	labeler.label(image)

