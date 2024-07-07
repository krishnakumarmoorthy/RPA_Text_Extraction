import cv2
import pytesseract
from PIL import Image

# Path to Tesseract in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Gaussian blur to reduce noise
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # Increase contrast by adjusting the image histogram
    img = cv2.equalizeHist(img)

    # Apply adaptive thresholding to create a clear binary image
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                cv2.THRESH_BINARY, 11, 2)

    # Save the processed image temporarily to open with PIL
    temp_filename = 'temp_processed.png'
    cv2.imwrite(temp_filename, img)
    return temp_filename

def extract_text_from_image(image_path):
    processed_image_path = preprocess_image(image_path)
    
    # Load the processed image with PIL
    pil_img = Image.open(processed_image_path)

    # Configuration for tesseract
    custom_config = r'--oem 3 --psm 6'
    # Extract text
    text = pytesseract.image_to_string(pil_img, config=custom_config)
    
    # Clean up: remove the temporary file if desired
    # os.remove(temp_filename)

    return text

# Replace 'path_to_your_image.png' with the path to the image file you want to process
image_path = 'images\Screenshot 2024-07-04 171111_foc.png'
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:", extracted_text)
