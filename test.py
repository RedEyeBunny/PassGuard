from pynput import keyboard

def launch_password_manager():
    print("Launching Password Manager...")
    # Add your actual password manager launch code here
    # For example: os.system('python3 path_to_your_password_manager.py')

# Define the hotkey combination
COMBINATION = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='q')}
current_keys = set()

def on_press(key):
    try:
        if key in COMBINATION:
            current_keys.add(key)
            if all(k in current_keys for k in COMBINATION):
                launch_password_manager()
    except Exception as e:
        print(f"Error in on_press: {e}")

def on_release(key):
    try:
        if key in current_keys:
            current_keys.remove(key)
    except Exception as e:
        print(f"Error in on_release: {e}")

# Listener for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Hotkey listener is running. Press Ctrl+Shift+Q to launch the password manager.")
    listener.join()
