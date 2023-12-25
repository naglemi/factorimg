
# FactorImg: Image Color Analysis for Semantic Segmentation

FactorImg is a Python package designed to analyze and quantify the color distribution in images. It is particularly useful for measuring areas of classes from semantic segmentation, allowing you to quantify the area covered by each class in the segmentation mask.

Why make this a Python package instead of just a basic script? Well, now that VScode has Copilot X with GPT4 integration, I wanted to play around with it. Most of this was drafted/written by Copilot.

## Features

- Analyze individual images or entire directories.
- Generate a CSV file with color information (RGB values and pixel count).
- Create a color legend image.
- Create a bar plot of color distribution.

## Installation

This package requires Python 3.7 or later. Clone the repository and install the dependencies:

```sh
git clone https://github.com/yourusername/factorimg.git
cd factorimg
pip install -r requirements.txt
```

## Usage

The main functionality of `factorimg` is provided by the `HexTable` class.

Here's a basic example of how to use FactorImg:

```python
from factorimg.hextable import HexTable, create_csv

# Create a HexTable instance
hex_table = HexTable()

# Process an image or a folder of images
hex_table.process_image('path/to/image.png')
# or
hex_table.process_folder('path/to/folder')

# Save the color information to a CSV file
hex_table.save('path/to/output.csv')

# Create a color legend image
hex_table.create_legend('path/to/legend.png')

# Create a bar plot of color distribution
hex_table.create_barplot('path/to/plot.png')
```

You can also use the `create_csv` function to process an image or a folder of images and save the color information to a CSV file in one step:

```python
from factorimg.hextable import create_csv

create_csv('path/to/image_or_folder', 'path/to/output.csv')
```

## Semantic Segmentation Use Case

When dealing with semantic segmentation masks, FactorImg can be used to measure the area of each class. Each unique color in the segmentation mask corresponds to a different class. By analyzing the color distribution, you can quantify the area covered by each class. This can be useful for understanding the distribution of classes in your dataset, or for evaluating the output of a segmentation algorithm.

## License

This project is licensed under the BSD 3-Clause License. See the LICENSE.txt file for details.
