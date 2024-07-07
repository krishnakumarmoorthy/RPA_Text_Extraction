from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Ensure that Tesseract-OCR is installed and the path is set correctly
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Uncomment and set this path if needed

def find_text_in_image(image_path, search_text):
    # Open the image file
    image = Image.open(image_path)

    # Use pytesseract to get OCR data with bounding box information
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Iterate through the data to find the text
    j = 0
    print(data)
    for i, text in enumerate(data['text']):
        if text.strip().lower() == search_text.lower():
            if j == 0:
                j+=1
                continue

            # Get the bounding box coordinates
            x = data['left'][i]
            y = data['top'][i]
            width = data['width'][i]
            height = data['height'][i]
            print(f"Found '{search_text}' at (X: {x}, Y: {y}, Width: {width}, Height: {height})")
            center_x = x + (width/2)
            center_y = y + (height/2)
            print (center_x,center_y)
            return True
    print(f"'{search_text}' not found in the image.")
    return None

# Path to your image file
image_path = "images/WhatsApp Image 2024-06-28 at 12.58.59.jpeg"

# Text to search for
search_text = 'REFRESH'

# Find the text in the image
find_text_in_image(image_path, search_text)


