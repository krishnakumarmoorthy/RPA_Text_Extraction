import cv2
import pytesseract
from pytesseract import Output

# Specify the path to the tesseract executable if needed (for Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Load the image
image_path = 'images/Screenshot 2024-07-04 171111.png'
image = cv2.imread(image_path)

# Define the bounding box coordinates for the region of interest (ROI)
# (x, y, w, h) -> x, y are the top-left coordinates; w, h are the width and height
x, y, w, h =1435 , 279, 409, 162  # Example coordinates, adjust as needed

# Highlight the ROI on the image (optional, for visualization)
roi_image = image.copy()
cv2.rectangle(roi_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Use Tesseract to read text from the specified ROI
roi = image[y:y + h, x:x + w]
text = pytesseract.image_to_string(roi, config='--psm 12 --oem 1')


# Save the highlighted image (optional, for visualization)
# highlighted_image_path = 'highlighted_image.png'
# cv2.imwrite(highlighted_image_path, roi_image)

# Save the extracted text to a file
text_output_path = 'extracted_text.txt'
with open(text_output_path, 'w') as text_file:
    text_file.write(text)

print(f"Extracted text: {text}")
print(f"Extracted text saved to {text_output_path}")
# print(f"Highlighted image saved to {highlighted_image_path}")

# Optionally, display the images
# cv2.imshow('Original Image', image)
# cv2.imshow('Highlighted Image', roi_image)
# cv2.imshow('ROI', roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
