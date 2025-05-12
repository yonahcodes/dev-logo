# PNG Logo Overlay Automation

I created this to customize banners for my university course repositories. It provides scripts to overlay `PNG` logo images onto a background PNG image, using a `Bash` script for `SVG` to PNG conversion (via `Inkscape`) and a `Python` script (using `Pillow`) for adjustable logo overlay.

![Udem C++](img/overlay/udem_cpp.png)

## Key Features

* **SVG to PNG Conversion:** Automates the conversion of multiple SVG logo files to PNG format using `Inkscape` via a `Bash` script.
* **PNG Overlay:** Overlays `PNG` logo images onto a background PNG with precise control over size and position using a Python script.
* **Customizable Placement:** The Python script allows for easy adjustment of the logo's size and position on the background image.
* **Efficient Batch Processing:** The Bash script enables quick conversion of multiple SVG files, streamlining the workflow.

## Requirements

* `Python 3.x`
* `Pillow` library (Python)
* `Inkscape`

## Directory Structure

* `img/svg/`: Contains the original SVG logo files.
* `img/png/`: Stores the PNG files generated from the SVG files by the conversion script.
* `img/overlay/`: Will contain the final PNG images with the logos overlaid onto the background.
* `scripts/`: Contains the executable scripts (`overlay.py` and `convert_svgs.sh`).

## Setup and Usage

### 1. SVG to PNG Conversion

If you need to convert SVG files to PNG before overlaying:

1. **Install Inkscape:**
    ```bash
    brew install inkscape
    ```
2. **Ensure the output directory exists:**
    ```bash
    mkdir img/png
    ```
3. **Use the provided Bash script (`scripts/convert_svgs.sh`):**
    ```bash
    #!/bin/bash
    for file in img/svg/*.svg; do
        filename=$(basename "$file" .svg)
        output_png="img/png/${filename}.png"
        inkscape "$file" --export-filename="$output_png"
        echo "Converted $file to $output_png"
    done
    ```
    * Make the script executable:

        ```bash
        chmod +x scripts/convert_svgs.sh
        ```
    * Run the script from the `scripts/` directory:
        ```bash
        cd scripts
        ./convert_svgs.sh
        ```

### 2. PNG Overlay

To overlay PNG logo images onto a background image:

1. **Navigate to the project directory.**

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```
3. **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
4. **Install the Pillow library:**
    ```bash
    pip install pillow
    ```
5. **Run the Python script (`scripts/overlay.py`):**
    ```bash
    python scripts/overlay.py
    ```

## Customizing Logo Overlay

The `scripts/overlay.py` script provides the following key variables for customizing the logo overlay:

* `background_path`: Path to the background PNG image. *(Default: "../img/png/udem.png")*
* `logo_path`: Path to the logo PNG image you want to overlay. *(Default: "../img/png/csharp.png")*
* `target_logo_height_pct`: Logo height as a percentage of the background image height.
* `x_position_pct`: Horizontal position of the logo's left edge as a percentage of the background image width (0.0 = left, 1.0 = right).
* `y_position_pct`: Vertical position of the logo's top edge as a percentage of the background image height (0.0 = top, 1.0 = bottom).

To overlay a different logo or adjust its placement, modify these variables directly within the `scripts/overlay.py` file.

**Example:**
```py
# Configuration
background_path = "../img/png/udem.png"
logo_path = "../img/png/python-original-wordmark.png"
output_path = f"../img/overlay/udem_python.png"

target_logo_height_pct = 0.25
x_position_pct = 0.68
y_position_pct = 0.50
```
