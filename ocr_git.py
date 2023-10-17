#OCR pdf reader with pytesseract, Great for unreadable pdfs

# pip install pytesseract
# pip install Pillow
#https://github.com/UB-Mannheim/tesseract/wiki to download manually

import fitz 
import pytesseract
from PIL import Image
import os
import pandas as pd

#Tesseract location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_file = r''  #path
pdf_document = fitz.open(pdf_file)
temp_dir = r''#temporary folder for screenshots
page = pdf_document[0]
output_excel = r''#output .xlsx file

# Find location of Pixels = x / (size of paint) * length of pdf

# left,top,width,height of screenshot
screenshot = [
    (100, 100, 100, 100),#location 0
    (200, 200, 200, 100),#location 1
    (300, 300, 300, 100),#location 2
    (400, 400, 400, 100),#location 3
]
text_data = {'File Name': [os.path.basename(pdf_file)]}

#Opens file, screenshots the mentioned locations and reads to excel
for i, (left, top, width, height) in enumerate(screenshot):
    x0, y0 = left, top
    x1, y1 = x0 + width, y0 + height

    matrix = fitz.Matrix(1, 1).prescale(3, 3) #Adjust prescale if needed
    pix = page.get_pixmap(matrix=matrix, clip=[x0, y0, x1, y1])
    
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    image_path = os.path.join(temp_dir, f"screenshot_{i}.png")
    image.save(image_path)

    extracted_text = pytesseract.image_to_string(image_path)
    text_data[f'Screenshot {i}'] = [extracted_text]

print(f"File Name: {text_data['File Name'][0]}")

df = pd.DataFrame(text_data)
df.to_excel(output_excel, index=False)
print(f"Data saved to {output_excel}")

# cropping tool to extract data

