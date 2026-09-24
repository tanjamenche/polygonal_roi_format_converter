"""
Polygonal ROI Format Converter - TXT file to YAML file

Converts TXT files with ROI vertices generated with Fiji/ImageJ (https://imagej.net/) (open polygonal ROI in ROI Manager, then select File -> Save As -> XY Coordinates) into YAML files with ROI vertices compatible with the Picasso Software (https://github.com/jungmannlab/picasso) version v0.7.3 (Render -> File -> Loaded pick regions). Processes all files within an input folder (root_folder) and its subfolders.

Author: Tanja Menche
Affiliation: Research group of Mike Heilemann, Goethe University Frankfurt am Main, Germany
Version: v1.0.0
Date: 2026-09-23

How to use:
-----------
1. Edit the "root_folder" and the "file_ending" at the end of this script
2. Run the script.
3. The script saves a YAML file for each TXT file with the defined file ending that it finds in the `root_folder` and its subfolders. Each YAML file is saved in the same folder as its corresponding TXT file, using the same file name with a `.yaml` extension.
"""

import yaml
import os


def parse_line(line):
    """
    Parse a line into x, y coordinates.
    Supports:
    - tab-separated
    - space-separated
    - comma-separated
    """
    parts = line.strip().replace(',', ' ').split()
    if len(parts) < 2:
        return None
    try:
        return float(parts[0]), float(parts[1])
    except ValueError:
        return None


def txt_to_yaml(input_file):
    """
    Convert a text file with polygon coordinates to a YAML file.
    Output file will be saved with same name but .yaml extension.
    """
    vertices = []

    with open(input_file, 'r') as file:
        for line in file:
            parsed = parse_line(line)

            # Skip invalid lines (e.g. headers or empty lines)
            if parsed is None:
                continue

            x, y = parsed
            vertices.append([x, y])

    # Close polygon
    if vertices:
        vertices.append(vertices[0])

    yaml_data = {
        "Shape": "Polygon",
        "Vertices": [vertices]
    }

    # Custom dumper to avoid YAML anchors
    class NoAnchorDumper(yaml.Dumper):
        def ignore_aliases(self, data):
            return True

    output_file = os.path.splitext(input_file)[0] + ".yaml"

    with open(output_file, 'w') as file:
        yaml.dump(yaml_data, file, Dumper=NoAnchorDumper, default_flow_style=False)

    print(f"Converted: {input_file} -> {output_file}")


def batch_process(root_folder, file_ending=".txt"):
    """
    Recursively process all files with given ending in folder and subfolders.
    """
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(file_ending.lower()):
                input_path = os.path.join(dirpath, filename)
                try:
                    txt_to_yaml(input_path)
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")


if __name__ == "__main__":
    root_folder = r"C:\polygonal_roi_format_converter\example_data\txt"   # <-- change this
    file_ending = "_ROI_picks.txt"          # <-- change this (or set just ".txt" to convert all TXT files in the root folder and subfolders)

    batch_process(root_folder, file_ending)