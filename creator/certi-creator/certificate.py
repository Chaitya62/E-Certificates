from PIL import Image, ImageFont, ImageDraw

"""
Name : (516,930)  Dimentions : 1023 x 72

Signatures

Faculty advisor
1)Computer : (264, 1368)    Dimentions : 180 x  65
2)IT : (1005, 1368)  Dimentions : 219 x 65

HOD
1) Computer: (1002, 1383)   Dimentions : 200 x 65
2) IT: (1341, 1368)      Dimentions : 200 x 65

Committee Head 
(1698, 1428)  Dimentions : 380 x 60

"""



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

	def load_font(self, font_path, font_size):
		font = ImageFont.truetype(font_path, font_size)
		self.font = font

	def put_image(self, img, x, y):
		self.certificate.paste(img, (x, y))

	def write(self, x, y, text):
		# load font first
		draw_certificate = ImageDraw.Draw(self.certificate)
		draw_certificate.text((x, y),text, self.fontColor, font=self.font)





	def save(self):
		self.certificate.save('out.png')



cer = Certificate('Chaitya Shah', 'Intro to CP', './certificate.jpg')

cer.load_certificate()


cer.load_font('font.ttf', 70)
img = Image.new('RGBA', (200, 100), (255,255,2, 255))


cer.write(516,930, 'Chaitya Shah')
cer.write(1716, 930, 'TY IT B')
cer.write(786, 1060, 'Introduction to Competitive Programming')
cer.write(1400, 1190, '10-08-17')


cer.load_font('font.ttf', 30)
cer.write(516, 1615, 'authenticate at: http://localhost:8000/event/testing/ae2b1fca515949e5d54fb22b8ed95575/')

# Faculty advisor comps
cer.put_image(img, 264, 1323)

# Faculty advisor IT
cer.put_image(img, 605, 1323)

# HOD COMPS
cer.put_image(img, 1002, 1323)

# HOD IT
cer.put_image(img, 1341, 1323)

# Committee HEAD 1
cer.put_image(img, 1698, 1323)

# Committee HEAD 2
cer.put_image(img, 1938, 1323)
cer.save()


	



