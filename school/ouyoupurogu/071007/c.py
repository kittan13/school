# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import numpy as np

def readDEM(mesh, debug=False):
    file_path = f"FG-GML-{mesh}-DEM5A"  # Construct file path

    if debug:
        print(f"Debug Mode: Reading file {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract 'gml:tupleList' tag data (assuming namespace is defined)
    alt_tag = "{http://www.opengis.net/gml/3.2}tupleList"

    alt_list = []
    for elem in root.iter(alt_tag):
        # Each line contains '地表面,' followed by the altitude value
        alt_values = elem.text.strip().split("\n")
        for value in alt_values:
            # Remove '地表面,' prefix and convert the altitude to float
            alt = float(value.replace('地表面,', ''))
            alt_list.append(alt)

    alt = np.array(alt_list)
    # Assuming idx is a range of indices from 0 to len(alt) - 1
    idx = np.arange(len(alt))

    return alt, idx
