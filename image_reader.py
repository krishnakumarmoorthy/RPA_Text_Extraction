import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Ensure that the Tesseract executable is in your PATH or specify its location:
# For example, on Windows you might need to set it like this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image file
# image_path = "/media/swetha/personal_files/rpa/images/WhatsApp Image 2024-06-21 at 00.08.55.jpeg"  #success
#image_path = "/media/swetha/personal_files/rpa/images/WhatsApp Image 2024-06-21 at 00.09.21.jpeg" #success
#image_path = "/media/swetha/personal_files/rpa/images/WhatsApp Image 2024-06-21 at 00.10.08.jpeg"   #success
#image_path = "/media/swetha/personal_files/rpa/images/WhatsApp Image 2024-06-21 at 00.21.09.jpeg"   #not success
image_path = "images/Screenshot 2024-07-04 171101_focussed.png"   #success

image = Image.open(image_path)

# Use pytesseract to do OCR on the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
