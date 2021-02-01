from fpdf import FPDF
from os import listdir, getcwd, path
from PIL import Image
from cv2 import imread
from pytesseract import image_to_string

current_dir = path.basename(getcwd())
pdf_name = current_dir + '.pdf'

pdf = FPDF()

for file in listdir('.'):
	if file.endswith('.jpg'):
		# make pdf from picture
		print(file)
		img = Image.open(file)
		width, height = img.size
		portrait = width > height
		if portrait :
			pdf.add_page(orientation="Landscape")
		else:
			pdf.add_page()
		pdf.image(file, x=0, y=0, w=pdf.w, h=pdf.h)
		
		# OCR picture
		txt_name = ''
		for elem in file.split('.')[:-1]:
			txt_name += elem + '.'
		txt_name += 'txt'
		opencv_img = imread(file)
		page_content_str = image_to_string(opencv_img, lang='jpn_vert')
		with open(txt_name, 'w') as txt_file:
			txt_file.write(page_content_str)
		

print('outputting to pdf, it can take a few mins')
pdf.output(pdf_name, 'F')