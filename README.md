# Word Cloud Project

A Python project that generates word clouds from text using custom masks.

## Features

- Generate word clouds with custom mask shapes
- SVG output with transparent background
- Custom font support
- Includes decorative cross SVG designs

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install numpy pillow wordcloud
```

## Usage

Run the word cloud generator:
```bash
python wdcloud.py
```

This will read text from `bsh.txt`, apply the mask from `mask_2.png`, and generate `wordcloud_masked.svg`.

## Files

- `wdcloud.py` - Main word cloud generator script
- `bsh.txt` - Input text file
- `mask_2.png` - Mask image for word cloud shape
- `rough_cross.svg` - Decorative cross design with textured strokes
- Various output SVG files
