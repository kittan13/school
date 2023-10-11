import os
import xml.etree.ElementTree as ET
import numpy as np


def readDEM(mesh, debug=False):
    folder_path = f"FG-GML-{mesh}-DEM5A"

    xml_files = sorted([filename for filename in os.listdir(folder_path) if filename.endswith('.xml')])

    total_alt_list = []
    total_idx_list = []

    for filename in xml_files:
        file_path = os.path.join(folder_path, filename)
        
        tree = ET.parse(file_path)
        root = tree.getroot()

        if debug:
            print("reading:", file_path)

        alt_tag = "{http://www.opengis.net/gml/3.2}tupleList"

        alt_list = []
        for elem in root.iter(alt_tag):
            alt_values = elem.text.strip().split("\n")
            for value in alt_values:
                if '地表面,' in value:
                    try:
                        alt = float(value.replace('地表面,', ''))
                    except ValueError:
                        alt = np.nan
                    alt_list.append(alt)
        
        total_alt_list.extend(alt_list)
        total_idx_list.extend(np.arange(len(alt_list)))

    num_rows = 1500
    num_cols = 2250

    alt = np.array(total_alt_list).reshape(num_rows, num_cols)
    idx = np.array(total_idx_list).reshape(num_rows, num_cols)

    return alt, idx
