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

def find_text_in_image(image_path, search_text):
    # Enhance the image
    image = enhance_image(image_path)
    
    # Use pytesseract to get OCR data with bounding box information
    custom_config = r'--oem 3 --psm 6'
    data = pytesseract.image_to_data(image, config=custom_config, output_type=pytesseract.Output.DICT)
    print(data['text'])
    # Iterate through the data to find the text
    found_texts = []
    j = 0
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
            found_texts.append((x, y, width, height))
            print(f"Found '{search_text}' at (X: {x}, Y: {y}, Width: {width}, Height: {height})")
            center_x = x + (width/2)
            center_y = y + (height/2)
            print (center_x,center_y)
            return True

    if not found_texts:
        print(f"'{search_text}' not found in the image.")
    return found_texts

# Path to your image file
image_path = 'images\Screenshot 2024-07-04 171133_foc.png'  # Replace with the path to your image

# Text to search for
search_text = 'REFRESH'

# Find the text in the image
found_texts = find_text_in_image(image_path, search_text)
