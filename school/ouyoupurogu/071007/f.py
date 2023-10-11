# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET
import numpy as np

def readDEM(mesh, debug=False):
    folder_path = f"FG-GML-{mesh}-DEM5A"  # フォルダパスを作成する

    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):  # XMLファイルのみを対象とする
            file_path = os.path.join(folder_path, filename)
            # 実際のデータの読み込みや処理
            tree = ET.parse(file_path)
            root = tree.getroot()

            if debug:
                print("Debug Mode:", file_path)

    # Extract 'gml:tupleList' tag data (assuming namespace is defined)
    alt_tag = "{http://www.opengis.net/gml/3.2}tupleList"

    alt_list = []
    for elem in root.iter(alt_tag):
        # Each line contains '地表面,' followed by the altitude value
        alt_values = elem.text.strip().split("\n")
        for value in alt_values:
            if '地表面,' in value:
                # Remove '地表面,' prefix and try converting the altitude to float
                try:
                    alt = float(value.replace('地表面,', ''))
                except ValueError:  # If the conversion fails, assign NaN
                    alt = np.nan
                alt_list.append(alt)

    # Now we need to reshape this into a 2D array
    # We can extract the shape from the 'gml:high' tag
    high_tag = "{http://www.opengis.net/gml/3.2}high"
    for elem in root.iter(high_tag):
        grid_shape = tuple(map(int, elem.text.split()))
    
    # Reshape the alt array into the grid shape
    alt = np.array(alt_list).reshape(grid_shape)

    # The idx will now be a pair of coordinate grids
    idx = np.indices(grid_shape)

    return alt, idx
