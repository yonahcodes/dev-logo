#!/bin/bash
for file in img/svg/*.svg; do
    filename=$(basename "$file" .svg)
    output_png="img/png/${filename}.png"
    inkscape "$file" --export-filename="$output_png"
    echo "Converted $file to $output_png"
done