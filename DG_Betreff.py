import pyperclip
import pyautogui
import time
import keyboard

class ClipboardHistory:
    def __init__(self, max_entries=3):
        self.history = []  # To store clipboard entries
        self.max_entries = max_entries  # Number of entries to track

    def add_to_history(self, clipboard_content):
        # Add new clipboard content if it's not already in history
        if clipboard_content not in self.history:
            self.history.append(clipboard_content)
            # Keep only the last 'max_entries' entries
            if len(self.history) > self.max_entries:
                self.history.pop(0)

    def get_history(self):
        return self.history

def main():
    clipboard_history = ClipboardHistory()

    print("Monitoring clipboard. Press Ctrl+C to stop.")
    last_checked = ""  # To track the last clipboard content (to detect changes)

    try:
        while True:
            # Get current clipboard content
            current_content = pyperclip.paste()

            # If clipboard content has changed, update the history
            if current_content != last_checked:
                clipboard_history.add_to_history(current_content)
                last_checked = current_content

            # Listen for the custom key combination: Ctrl + M
            if keyboard.is_pressed('ctrl+m'):
                # When the combination is pressed, prepare the clipboard history text
                result = " // ".join(clipboard_history.get_history()) + " // "
                print("Preparing to paste:", result)

                # Set the result to the clipboard
                pyperclip.copy(result)  # Copy the result to the clipboard

                # Simulate pressing Ctrl+V (to paste the clipboard content)
                pyautogui.hotkey('ctrl', 'v')  # This will paste the text into the focused window
                

            time.sleep(0.1)  # Sleep for 0.1 second to reduce CPU usage

    except KeyboardInterrupt:
        print("\nStopped monitoring clipboard.")

if __name__ == "__main__":
    main()
