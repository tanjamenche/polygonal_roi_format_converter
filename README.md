# Polygon ROI Format Converter

There are two scripts: the YAML file to TXT file script and the TXT file to YAML file script.

## Polygonal ROI Format Converter - YAML file to TXT file

Converts YAML files with ROI vertices generated with the [Picasso Software](https://github.com/jungmannlab/picasso) version v0.7.3 (Render -> Tools -> Tool Settings -> 
Shape: Polygon, -> Tools -> Pick) into TXT files with ROI vertices compatible with [Fiji/ImageJ] (https://imagej.net/) (open polygonal ROI in ROI Manager, then select File -> Import -> XY Coordinates). 
Processes all files within an input folder (root_folder) and its subfolders.

## Polygonal ROI Format Converter - TXT file to YAML file

Converts TXT files with ROI vertices generated with [Fiji/ImageJ] (https://imagej.net/) (open polygonal ROI in ROI Manager, then select File -> Save As -> XY Coordinates) into YAML files with ROI vertices compatible with 
the [Picasso Software](https://github.com/jungmannlab/picasso) version v0.7.3 (Render -> File -> Loaded pick regions). Processes all files within an input folder (root_folder) and its subfolders.

## Note

The ROI vertices are given in the pixel coordinates of the original camera image used for the single-molecule microscopy (SMLM) acquisition. These coordinates refer to the camera's acquisition pixels and may therefore not 
correspond directly to the pixels of the exported SMLM reconstruction, which is often rendered with a different display pixel size.


## Requirements

* Python **3.11**
* PyYAML **6.0.1**

## Installation
```PowerShell
conda create --name polygon_roi_format_converter python=3.11
conda activate polygon_roi_format_converter
cd filepath\polygon_roi_format_converter
conda install --file requirements.txt
```


## How to use
1. Edit the "root_folder" and the "file_ending" at the end of this script
2. Run the script.
	Open environment:
	```PowerShell
	conda activate polygon_roi_format_converter
	```
	Navigate to the file path, where polygon_roi_format_converter.py is stored:
	```PowerShell
	cd filepath\polygon_roi_format_converter
	```
	Run:
	Polygonal ROI Format Converter - YAML file to TXT file
	```PowerShell
	python polygon_roi_yaml_to_txt.py
	```
	Polygonal ROI Format Converter - TXT file to YAML file
	```PowerShell
	python polygon_roi_txt_to_yaml.py
	```	

3. Polygonal ROI Format Converter - YAML file to TXT file
	The script saves a TXT file for each YAML file with the defined file ending that it finds in the `root_folder` and its subfolders. 
	Each TXT file is saved in the same folder as its corresponding YAML file, using the same file name with a `.txt` extension.
   Polygonal ROI Format Converter - TXT file to YAML file
	The script saves a YAML file for each TXT file with the defined file ending that it finds in the `root_folder` and its subfolders. 
	Each YAML file is saved in the same folder as its corresponding TXT file, using the same file name with a `.yaml` extension.