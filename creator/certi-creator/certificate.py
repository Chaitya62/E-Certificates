from PIL import Image, ImageFont, ImageDraw


class Certificate():

	def __init__(self, name, event, path):

		# path to certificate template
		self.path = path
		self.name = name
		self.type = 'participation'
		self.event = event
		self.no_of_signature = 3
		self.certificate = None
		self.signatures = None
		self.font = None
		self.fontColor = (0, 0, 0)


		# array of tuples [(w, h), ...]
		self.signature_coordinates = []

		# array of absolute path 
		self.signature_location = []

	def load_signature(self):
		self.signatures = []

		for path in self.signature_location:
			self.signatures.push(Image.open(path))

	def load_certificate(self):
		self.certificate = Image.open(self.path)

	def load_font(self, font_path. font_size):
		font = ImageFont.truetype(font_path, font_size)
		self.font = font

	def write(self, x, y, text):
		# load font first
		draw_certificate = ImageDraw.Draw(self.certificate)
		draw_certificate.text((x, y),text, self.fontColor, font=self.font)


	def save(self):
		self.certificate.save('out.png')

	



