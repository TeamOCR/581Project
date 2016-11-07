import pytesseract
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

PRINTED_TEXT_TEST = "test.png"
HAND_WRITTEN = "test8.jpg"
HAND_WRITTEN_CORBAN = "test5.jpg"
TESTER = {"Corban":HAND_WRITTEN_CORBAN}

def process_image(file_location):
	image = _get_image(file_location)
	image.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(image)
	image = enhancer.enhance(2)
	image.filter(ImageFilter.SHARPEN)
	#image.filter(ImageFilter.FIND_EDGES)
	image.filter(ImageFilter.EDGE_ENHANCE)
	##image.filter(ImageFilter.GaussianBlur)
	image.show()
	print("results: %s\n" % pytesseract.image_to_string(image))
	print("\n#####################\n")
	return pytesseract.image_to_string(image)

def _get_image(file_location):
	return Image.open(file_location)

def _train_ocr():
	process_image(PRINTED_TEXT_TEST)
	process_image(HAND_WRITTEN_CORBAN)
	process_image(HAND_WRITTEN)
#file = raw_input("Enter an image name to parse: ")
#print("ImageFilter.SHARPEN\n####################\n\n")

_train_ocr()
print(process_image(HAND_WRITTEN_CORBAN))
