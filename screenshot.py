import pyautogui
# Specify the region (left, top, width, height)
region = (0, 0, 300, 400)
screenshot = pyautogui.screenshot(region=region)
screenshot.save('region_screenshot.png')
