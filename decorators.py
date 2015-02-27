class TypeValidatingDecorator(object):
	"""
	Decorator: TypeValidatingDecorator
	----------------------------------
	accepts valid_types as a list or single entry
	"""
	def __init__(self, valid_types):
		"""sets self.valid_types"""
		if not valid_types is None:
			if not type(valid_types) in [list, tuple]:
				valid_types = [valid_types]
		self.valid_types = valid_types


	def validate_type(self, x):
			"""raises assertion if x is not in valid_types"""
			if self.valid_types is None:
				return
			elif not type(x) in self.valid_types:
				raise TypeError("Incompatible label type: %s" % str(type(x)))


	def __call__(self, f):
		"""override"""
		raise NotImplementedError
