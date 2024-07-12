#!/bin/bash

# Detectar la salida de pantalla activa
OUTPUT=$(xrandr --listmonitors | grep '*' | awk '{print $NF}')

# Obtener el brillo actual
current_brightness=$(xrandr --verbose | grep -i brightness | cut -f2 -d ' ')

# Aumentar el brillo en un 10%
new_brightness=$(echo "$current_brightness + 0.1" | bc)

# Asegurarse de que el nuevo brillo no supere 1.0
if (( $(echo "$new_brightness > 1.0" | bc -l) )); then
    new_brightness=1.0
fi

# Aplicar el nuevo valor de brillo
xrandr --output $OUTPUT --brightness $new_brightness

brightness_percentage=$(echo "$new_brightness * 100" | bc)

# Mostrar el nuevo valor de brillo
echo "Brightness: $brightness_percentage%"
