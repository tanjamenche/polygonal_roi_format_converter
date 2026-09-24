# -*- coding: utf-8 -*-
"""
Polygonal ROI Format Converter - YAML file to TXT file

Converts YAML files with ROI vertices generated with the Picasso Software (https://github.com/jungmannlab/picasso) version v0.7.3 (Render -> Tools -> Tool Settings -> Shape: Polygon, -> Tools -> Pick) into TXT files with ROI vertices compatible with Fiji/ImageJ (https://imagej.net/) (open polygonal ROI in ROI Manager, then select File -> Import -> XY Coordinates). Processes all files within an input folder (root_folder) and its subfolders.

Author: Tanja Menche
Affiliation: Research group of Mike Heilemann, Goethe University Frankfurt am Main, Germany
Version: v1.0.0
Date: 2026-09-23

How to use:
-----------
1. Edit the "root_folder" and the "file_ending" at the end of this script
2. Run the script.
3. The script saves a TXT file for each YAML file with the defined file ending that it finds in the `root_folder` and its subfolders. Each TXT file is saved in the same folder as its corresponding YAML file, using the same file name with a `.txt` extension.
"""

import yaml
import os

def yaml_to_imagej_txt(input_yaml):
    """
    Convert a single YAML file with polygon coordinates to an ImageJ-readable text file.
    The output .txt file is saved in the same folder with the same name.
    """
    output_txt = os.path.splitext(input_yaml)[0] + ".txt"

    # Load YAML data
    with open(input_yaml, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Extract vertices
    vertices = yaml_data.get("Vertices", [])
    if len(vertices) == 1 and isinstance(vertices[0][0], list):
        vertices = vertices[0]

    # Remove duplicate closing vertex (ImageJ closes polygon automatically)
    if vertices and vertices[0] == vertices[-1]:
        vertices = vertices[:-1]

    # Write ImageJ-readable TXT
    with open(output_txt, 'w') as file:
        file.write("X\tY\n")
        for x, y in vertices:
            file.write(f"{x:.3f}\t{y:.3f}\n")

    print(f"✅ Converted: {input_yaml} → {output_txt}")


def batch_convert_yaml_to_txt(root_folder, yaml_suffix=".yaml"):
    """
    Recursively find and convert all YAML files with the given suffix in a folder and its subfolders.
    :param root_folder: Path to the folder to search through
    :param yaml_suffix: File ending of YAML files to convert (e.g. '_ROI.yaml')
    """
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(yaml_suffix):
                yaml_path = os.path.join(dirpath, filename)
                try:
                    yaml_to_imagej_txt(yaml_path)
                except Exception as e:
                    print(f"❌ Error processing {yaml_path}: {e}")


if __name__ == "__main__":
    # 🔧 User inputs
    root_folder = r"C:\polygonal_roi_format_converter\example_data\yaml" # <-- change this
    yaml_suffix = "_ROI_picks.yaml"  # <-- change this (or set just ".yaml" to convert all YAML files in the root folder and subfolders)

    batch_convert_yaml_to_txt(root_folder, yaml_suffix)
