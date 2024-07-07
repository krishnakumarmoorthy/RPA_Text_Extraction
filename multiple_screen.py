import pygetwindow as gw
import pyautogui
import time

def activate_window_by_index(title, index=0):
    try:
        # Get all windows with the specified title
        windows = gw.getWindowsWithTitle(title)
        if windows:
            # Activate the window by index
            window = windows[index]
            window.activate()
            time.sleep(1)  # Ensure the window is active
            return window
        else:
            print(f"No windows found with title: {title}")
            return None
    except IndexError:
        print(f"No window at index {index} for title: {title}")
        return None

def automate_window_actions(window_title, index, actions):
    # Activate the window using title and index
    window = activate_window_by_index(window_title, index)
    if window:
        for action_type, value in actions:
            if action_type == "click":
                pyautogui.click(window.left + value[0], window.top + value[1])
            elif action_type == "type":
                pyautogui.write(value)
            elif action_type == "press":
                pyautogui.press(value)
            time.sleep(0.5)
        print(f"Actions completed on window: {window_title} at index {index}")

# Define actions for each window
# actions = [("click", (100, 200)), ("type", "Hello, world!"), ("press", "enter")]
actions = [("click", (100, 200))]

# Title of the windows to manipulate
window_title = "teletype"

# Automate actions in each window, specifying the window by index
automate_window_actions(window_title, 0, actions)  # First window
time.sleep(4)
automate_window_actions(window_title, 1, actions)  # Second window
