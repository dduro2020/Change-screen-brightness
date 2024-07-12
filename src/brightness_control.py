#!/usr/bin/env python3

import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_current_brightness():
    """Gets the current screen brightness."""
    try:
        # Detect the active display output
        output = subprocess.check_output("xrandr --listmonitors | grep '*' | awk '{print $NF}'", shell=True).decode().strip()
        # Get the current brightness
        current_brightness = subprocess.check_output(f"xrandr --verbose | grep -i brightness | awk '{{print $2}}'", shell=True).decode().strip()
        return output, float(current_brightness)
    except Exception as e:
        print(f"Error obtaining brightness: {e}")
        return None, None

def set_brightness(value):
    """Sets the screen brightness."""
    try:
        # Detect the active display output
        output, _ = get_current_brightness()
        # Set the new brightness using xrandr
        subprocess.run(f"xrandr --output {output} --brightness {value}", shell=True)
        # Display the new brightness value in the label
        brightness_percentage = round(value * 100, 2)
        label_brightness.config(text=f"Brightness: {brightness_percentage}%")
    except Exception as e:
        print(f"Error changing brightness: {e}")

# Create the main window
root = tk.Tk()
root.title("Adjust Brightness")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Path to the brightness icon file URL
icon_url = "https://github.com/dduro2020/Change-screen-brightness/raw/main/imgs/sun.png"  # Direct URL to the image

# Set the window icon
try:
    response = requests.get(icon_url)
    icon = Image.open(BytesIO(response.content))
    icon = icon.resize((48, 48), Image.LANCZOS)  # Resize the icon
    icon_photo = ImageTk.PhotoImage(icon)
    root.tk.call('wm', 'iconphoto', root._w, icon_photo)
except Exception as e:
    print(f"Error loading the icon: {e}")

# Create a frame for the content
frame_content = tk.Frame(root, bg="#f0f0f0")
frame_content.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Get the current brightness
output, current_brightness = get_current_brightness()

if current_brightness is None:
    root.destroy()
    raise SystemExit("Current brightness could not be obtained.")

# Create a label to show the current brightness
label_brightness = tk.Label(frame_content, text=f"Brightness: {round(current_brightness * 100, 2)}%", font=("Arial", 12), bg="#f0f0f0")
label_brightness.pack(pady=10)

# Create a scale to adjust the brightness
brightness_scale = tk.Scale(frame_content, from_=0.1, to_=1.0, resolution=0.01, orient=tk.HORIZONTAL, command=lambda val: set_brightness(float(val)), bg="#e0e0e0", troughcolor="#d0d0d0", highlightthickness=0, sliderlength=30)
brightness_scale.set(current_brightness)
brightness_scale.pack(pady=10, fill=tk.X, expand=True)

# Initialize the current brightness on the scale
set_brightness(current_brightness)

# Run the main event loop
root.mainloop()
