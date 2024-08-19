import time
import pyperclip
import json
from datetime import datetime

def monitor_clipboard():
    last_content = pyperclip.paste()
    print("Monitoring clipboard. Press Ctrl+C to stop.")
    
    try:
        while True:
            current_content = pyperclip.paste()
            if current_content != last_content:
                print("Clipboard content changed. Appending to file.")
                append_to_json(current_content)
                last_content = current_content
            time.sleep(0.5)  # Sleep for 500ms
    except KeyboardInterrupt:
        print("Monitoring stopped.")

def append_to_json(content):
    try:
        with open('app/clipboard_history.json', 'r+') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    timestamp = datetime.now().isoformat()
    new_entry = {"timestamp": timestamp, "content": content}
    data.append(new_entry)

    with open('app/clipboard_history.json', 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    monitor_clipboard()