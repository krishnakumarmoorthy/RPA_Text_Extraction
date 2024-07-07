import pytesseract
from PIL import Image, ImageEnhance

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def enhance_image(image_path):
    # Open the image file
    image = Image.open(image_path)
    
    # Convert image to grayscale
    image = image.convert('L')
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    # Save the enhanced image (for debugging purposes)
    image.save('enhanced_image.png')
    
    return image
image_path = 'images/Screenshot 2024-07-04 171101_focussed.png'
image = enhance_image(image_path)
custom_config = r'--oem 3 --psm 6'
data = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
print(data['text'])
