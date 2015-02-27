import cv
import cv2
from operator import itemgetter

class CVLabeler(object):
	"""
	Class: CVLabeler
	================
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
		self.labels = None
		self.objs = None

		self.get_objects = get_objects
		self.draw_object = draw_object
		self.get_distance = get_distance
		self.update_object = update_object

		self.create_display()


	def __del__(self):
		"""tears down display"""
		self.teardown_display()


	def create_display(self):
		"""creates window and attaches callback"""
		cv2.namedWindow(self.window_name)
		cv2.setMouseCallback(self.window_name, self.mouse_callback)


	def teardown_display(self):
		"""tears down display"""
		cv2.destroyWindow(self.window_name)


	def reset_objs_labels(self, image):
		"""resets self.objs and self.labels from image"""
		self.objs = self.get_objects(image)
		self.labels = [None for obj in self.objs]


	def get_closest_obj(self, objs, x, y):
		"""returns closest x,y"""
		distances = [self.get_distance(obj, x, y) for obj in objs]
		print (x, y)
		ix, dist = min(enumerate(distances), key=itemgetter(1))
		return ix, objs[ix]


	def mouse_callback(self, event, x, y, flags, param):
		"""handles mouse input"""
		if event == cv2.EVENT_LBUTTONDOWN:
			ix, obj = self.get_closest_obj(self.objs, x, y)
			self.labels[ix] = self.update_object(event, self.labels[ix])


	def annotate_image(self, image, objs, labels):
		"""updates image based on current labels""" 
		disp_img = image.copy()
		for obj, label in zip(objs, labels):
			disp_img = self.draw_object(disp_img, obj, label)
		return disp_img


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
			cv2.imshow(self.window_name, disp_img)

			#=====[ Step 4: escape to move to next image	]=====
			key = cv2.waitKey(20)
			if key & 0xFF == 27:
				break

		return self.objs, self.labels







