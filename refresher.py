import pyautogui
import time
import pytesseract
from PIL import Image, ImageEnhance

# Set the path to the Tesseract-OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_screen():
    image_name = "screenshot.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(image_name)
    return image_name

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
            center_x = x + (width/2)
            center_y = y + (height/2)
            print (center_x,center_y)
            return (center_x,center_y)

    if not found_texts:
        print(f"'{search_text}' not found in the image.")
    return (0,0)

def click_refresh(x,y):
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
def move_around(x,y):
    pyautogui.moveTo(x+200, y+200, duration=1)
time.sleep(5)
while(True):
    x,y = find_text_in_image(capture_screen(),"REFRESH")
    if x==0 and y==0:
        break
    click_refresh(x,y)
    move_around(x,y)
print("page loaded")