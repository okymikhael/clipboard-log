# Clipboard Monitor

This Python script monitors the clipboard for any changes and logs the clipboard content along with a timestamp to a JSON file.

## Requirements

- Python 3.x
- `pyperclip` library
- `scrcpy` (for Android device screen mirroring)

You can install the required library using pip:

```bash
pip install pyperclip
```

You can install `scrcpy` by following the instructions on the [scrcpy GitHub page](https://github.com/Genymobile/scrcpy).

## Usage

1. **Run the script**:
    ```bash
    python app/main.py
    ```

2. **Monitor the clipboard**:
    - The script will start monitoring the clipboard for any changes.
    - When the clipboard content changes, it will append the new content along with a timestamp to `app/clipboard_history.json`.

3. **Stop the script**:
    - Press `Ctrl+C` to stop monitoring.

## File Structure

- `app/main.py`: The main script that monitors the clipboard and logs changes.
- `app/clipboard_history.json`: The JSON file where clipboard history is stored.

## Functions

### `monitor_clipboard()`

- Monitors the clipboard for changes.
- If the clipboard content changes, it calls `append_to_json()` to log the new content.
- Runs indefinitely until interrupted by `Ctrl+C`.

### `append_to_json(content)`

- Appends the given content along with a timestamp to `app/clipboard_history.json`.
- If the file does not exist or is empty, it creates a new JSON array.

## Example

Here is an example of what the `app/clipboard_history.json` file might look like after running the script:

```json
[
  {
    "timestamp": "2023-10-01T12:34:56.789123",
    "content": "First clipboard content"
  },
  {
    "timestamp": "2023-10-01T12:35:10.123456",
    "content": "Second clipboard content"
  }
]
```

## Notes

- The script checks the clipboard every 500 milliseconds.
- Ensure you have write permissions to the `app/clipboard_history.json` file or the directory where it is located.

## License

This project is licensed under the MIT License.