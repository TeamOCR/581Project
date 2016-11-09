import pytesseract
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

SOME_PICTURE_OF_TEXT = "test.png"

def process_image(file_location):
	image = _get_image(file_location)
	image.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(image)
	image = enhancer.enhance(2)
	image.filter(ImageFilter.SHARPEN)
	image.filter(ImageFilter.EDGE_ENHANCE)
	print("results: %s\n" % pytesseract.image_to_string(image))
	return pytesseract.image_to_string(image)

def _get_image(file_location):
	return Image.open(file_location)

def _train_ocr():
	process_image(PRINTED_TEXT_TEST)
	process_image(HAND_WRITTEN_CORBAN)
	process_image(HAND_WRITTEN)

process_image(SOME_PICTURE_OF_TEXT)
