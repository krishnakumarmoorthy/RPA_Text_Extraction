import pyautogui
import time

# Move the mouse to a specific position
# Replace x, y with the coordinates you want
time.sleep(5)
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

x, y = 1147.0, 695.5
pyautogui.moveTo(x, y, duration=1)

# Click at the specific position
pyautogui.click()

# Optional: Small delay to ensure the cursor has clicked and the application is ready for typing
time.sleep(0.5)

# Type a string
# text_to_type = "Hello, World!"
# pyautogui.write(text_to_type, interval=0.1)

# # Press 'Enter'
# pyautogui.press('enter')
