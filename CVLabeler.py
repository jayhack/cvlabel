import cv
import cv2

class CVLabeler(object):

	window_name = 'DISPLAY'
	# window_size = (640, 480)

	def __init__(self, get_objects, draw_object):
		"""
			get_objects: image -> objects  
			draw_object: (image, objects) -> drawn image
		"""
		self.labels = None
		self.objs = None

		self.get_objects = get_objects
		self.draw_object = draw_object

		self.create_display()


	def __del__(self):
		"""tears down display"""
		self.teardown_display()


	def create_display(self):
		"""creates window and attaches callback"""
		cv2.namedWindow(self.window_name)
		# cv2.resizeWindow(self.window_name, self.window_size[0], self.window_size[1])
		# cv2.setMouseCallback(self.window_name, self.mouse_callback)


	def teardown_display(self):
		"""tears down display"""
		cv2.destroyWindow(self.window_name)


	def get_closest_obj(self, x, y):
		"""returns closest x,y"""
		raise NotImplementedError()


	def mouse_callback(self, event, x, y, flags, param):
		"""handles mouse input"""
		if event == cv2.EVENT_LBUTTONDBLCLK:
			print "BUTTON CLICK: (%d, %d)" % (x, y)


	def annotate_image(self, image, objs):
		"""updates image based on current labels""" 
		disp_img = image.copy()
		for obj in objs:
			disp_img = self.draw_object(disp_img, obj)
		return disp_img


	def label(self, image):
		"""
			allows one to label the supplied image
		"""
		objs = self.get_objects(image)

		while True:
			disp_img = self.annotate_image(image, objs)
			cv2.imshow(self.window_name, disp_img)

			if cv2.waitKey(20) & 0xFF == 27:
				break



