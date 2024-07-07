import cv2
import numpy as np
from PIL import Image, ImageEnhance
import pytesseract

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def remove_lines(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path, 0)  # Read in grayscale mode

    # Use thresholding to extract the structure of the image
    _, thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Use morphological transformations to remove horizontal and vertical lines
    kernel = np.ones((3,3), np.uint8)
    img_eroded = cv2.erode(thresh, kernel, iterations=1)
    img_dilated = cv2.dilate(img_eroded, kernel, iterations=1)

    # Detect and remove lines
    edges = cv2.Canny(img_dilated, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=160, minLineLength=100, maxLineGap=10)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (255, 255, 255), 2)

    # Convert back to PIL Image
    final_image = Image.fromarray(image)
    return final_image

def enhance_image(image):
    # Convert image to grayscale
    image = image.convert('L')
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    # Save the enhanced image (for debugging purposes)
    image.save('enhanced_image.png')
    
    return image

image_path = 'images/Screenshot 2024-07-04 171101_focussed.png'
image = remove_lines(image_path)
enhanced_image = enhance_image(image)

# OCR with Tesseract
custom_config = r'--oem 3 --psm 6'
data = pytesseract.image_to_data(enhanced_image, config=custom_config, output_type=pytesseract.Output.DICT)

# Print OCR results
for text in data['text']:
    if text.strip():
        print(text)
