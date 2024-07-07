import cv2
import numpy as np
from PIL import Image
import pytesseract

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_for_ocr(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise Exception("Image not loaded.")

    # Apply Gaussian blur and then use Otsu's threshold to binarize the image
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours and fill them which might help in connecting fragmented parts
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thresh, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Morphological operation to close small holes inside the foreground
    kernel = np.ones((2, 2), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Convert to PIL Image for compatibility with Tesseract
    final_image = Image.fromarray(cv2.bitwise_not(closing))
    final_image.save('final_processed_image.png')
    return final_image

def perform_ocr(image):
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

image_path = 'images\Screenshot 2024-07-04 171101_focussed.png'
preprocessed_image = preprocess_for_ocr(image_path)
extracted_text = perform_ocr(preprocessed_image)
print(extracted_text)
