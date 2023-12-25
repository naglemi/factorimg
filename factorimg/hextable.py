import os
import pandas as pd
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class HexTable:
    def __init__(self):
        self.color_dict = {}

    def process_image(self, image_path):
        """
        Process an image and update the color dictionary.

        Args:
            image_path (str): The path to the image file.
        """
        img = Image.open(image_path)
        img_data = img.getdata()

        for color in img_data:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
            if hex_color in self.color_dict:
                self.color_dict[hex_color]['count'] += 1
                #self.color_dict[hex_color]['image_paths'].append(image_path)
            else:
                self.color_dict[hex_color] = {'r': color[0], 'g': color[1], 'b': color[2], 'count': 1}

    def process_folder(self, folder_path):
        """
        Process a folder of images and update the color dictionary.

        Args:
            folder_path (str): The path to the folder containing image files.
        """
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(folder_path, filename)
                self.process_image(image_path)

    def save(self, csv_path):
        """
        Save the color dictionary as a CSV file.

        Args:
            csv_path (str): The path to save the CSV file.
        """
        df = pd.DataFrame.from_dict(self.color_dict, orient='index')
        df.to_csv(csv_path)

    def create_legend(self, legend_path, view=False):
        """
        Create a legend image with color information.

        Args:
            legend_path (str): The path to save the legend image.
        """
        legend_height = len(self.color_dict) * 30
        legend_width = 400

        legend_image = Image.new('RGB', (legend_width, legend_height), (255, 255, 255))
        draw = ImageDraw.Draw(legend_image)

        y = 10
        for hex_color, color_info in self.color_dict.items():
            r, g, b = color_info['r'], color_info['g'], color_info['b']
            draw.rectangle([(10, y), (40, y + 20)], fill=hex_color)
            draw.text((50, y), hex_color, fill=(0, 0, 0))
            draw.text((150, y), f"R: {r}", fill=(0, 0, 0))
            draw.text((250, y), f"G: {g}", fill=(0, 0, 0))
            draw.text((350, y), f"B: {b}", fill=(0, 0, 0))
            y += 30
            
        if view:
            legend_image.show()
        
        legend_image.save(legend_path)
        
    def create_barplot(self, plot_path, view=False):
        """
        Create a bar plot with color information.

        Args:
            plot_path (str): The path to save the bar plot.
        """
        # Create a DataFrame from the color dictionary
        df = pd.DataFrame.from_dict(self.color_dict, orient='index')

        # Create a bar plot with hex colors as x-values and log of counts as y-values
        plt.figure(figsize=(10, 6))
        plt.bar(df.index, np.log(df['count']), color=df.index)

        # Set plot title and labels
        plt.title('Color distribution')
        plt.xlabel('Hex code')
        plt.ylabel('Pixel count (log scale)')
        if view:
            plt.show()

        # Save the plot
        plt.savefig(plot_path)

def create_csv(image_path, csv_path):
    """
    Create a CSV file containing color information of an image or a folder of images.

    Args:
        image_path (str): The path to the image file or folder.
        csv_path (str): The path to save the CSV file.
    """
    hex_table = HexTable()

    if os.path.isfile(image_path):
        hex_table.process_image(image_path)
    elif os.path.isdir(image_path):
        hex_table.process_folder(image_path)
    else:
        raise ValueError("Invalid image path or folder path.")

    hex_table.save(csv_path)