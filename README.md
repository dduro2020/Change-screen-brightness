# Change-screen-brightness

## Python script

You can launch the script without writting python3:
```bash
brightness_control.py
```

## Install dependencies

```bash
sudo apt update
sudo apt install python3 python3-tk
```

```bash
sudo apt install python3-pip
pip install pillow
pip install requests
```

## Creating icon app
```bash
nano ~/.local/share/applications/adjust_brightness.desktop
```

Edit with your paths:
```bash
[Desktop Entry]
Name=Adjust Brightness
Comment=Adjust the screen brightness
Exec=/path/to/your/script/adjust_brightness.py
Icon=/path/to/your/icon/sun.png
Terminal=false
Type=Application
Categories=Utility;
```
Give permissions:
```bash
chmod +x ~/.local/share/applications/adjust_brightness.desktop
```

## Contribute to update interface!!
