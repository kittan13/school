# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET
import numpy as np

def readDEM(mesh, debug=False):
    folder_path = f"FG-GML-{mesh}-DEM5A"  # フォルダパスを作成する

    # These lists will contain all the altitude and index data
    alt_list = []
    idx_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):  # XMLファイルのみを対象とする
            file_path = os.path.join(folder_path, filename)
            # 実際のデータの読み込みや処理
            tree = ET.parse(file_path)
            root = tree.getroot()
            #tag_name = root.tag

            if debug:
                print("Debug Mode:", file_path)

            # Extract 'gml:tupleList' tag data (assuming namespace is defined)
            alt_tag = "{http://www.opengis.net/gml/3.2}tupleList"

            # Each file will have its own grid, so these lists will contain the altitude and index data for each file
            file_alt_list = []
            file_idx_list = []
            
            for elem in root.iter(alt_tag):
                # Each line contains '地表面,' followed by the altitude value
                alt_values = elem.text.strip().split("\n")
                for value in alt_values:
                    # Remove '地表面,' prefix and convert the altitude to float
                    if "地表面" in value:
                        alt = float(value.replace('地表面,', ''))
                        file_alt_list.append(alt)
                    elif "データなし" in value:
                        idx = -9999
                        file_idx_list.append(idx)

            alt_list.append(np.array(file_alt_list))
            idx_list.append(np.array(file_idx_list))

    # Combine the data from all the files
    alt = np.concatenate(alt_list).reshape(-1, 2250)  # reshape to desired shape
    idx = np.concatenate(idx_list).reshape(-1, 2250)  # reshape to desired shape

    return alt, idx

if __name__ == "__main__":
    mesh = '5235-37'
    alt, idx = readDEM(mesh, debug=True)
    print("標高値", type(alt), alt.shape)
    print(alt)
    print("標高モデル", type(idx), idx.shape)
    print(idx)
