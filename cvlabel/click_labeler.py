import cv
import cv2
from operator import itemgetter
from labeler import Labeler

class ClickLabeler(Labeler):
	"""
	Class: ClickLabeler
	===================
	Main class for labelling.

	Usage:
	------
		from cvlabel import CVLabeler, euclidean_dist
		labeler = CVLabeler(get_objects, draw_object, )
	"""

	window_name = 'DISPLAY'

	def __init__(self, get_objects, draw_object, get_distance, update_object):
		"""
			get_objects: image -> objects  
			draw_object: (image, objects) -> drawn image
			get_distance: (object, x, y) -> distance from (x, y)
			update_object: (event, label) -> new label
		"""
		super(ClickLabeler, self).__init__(get_objects, draw_object, get_distance, update_object)


	def label(self, image):
		"""has user label supplied image, returning (objs, labels)"""
		#=====[ Step 1: list support	]=====
		if type(image) == list:
			return map(self.labels, image)

		#=====[ Step 2: get objects	]=====
		self.reset_objs_labels(image)

		#=====[ Step 3: loop while annotating 	]=====
		while True:

			disp_img = self.annotate_image(image, self.objs, self.labels)
			self.show_image(disp_img)

			#=====[ Step 4: escape to move to next image	]=====
			key = cv2.waitKey(20)
			if key & 0xFF == 27:
				break

		return self.objs, self.labels














