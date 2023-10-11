import os
import xml.etree.ElementTree as ET
import numpy as np

def readDEM(mesh, num_rows=1500, num_cols=1826, debug=False):
    folder_path = f"FG-GML-{mesh}-DEM5A"  # フォルダパスを作成する

    # フォルダ内の.xmlファイルリストを作成し、ソートする
    xml_files = sorted([filename for filename in os.listdir(folder_path) if filename.endswith('.xml')])

    total_alt_list = []  # to store all altitude values from all files

    for filename in xml_files:  # ここで、ソートされたリストを使ってファイルを読み込む
        file_path = os.path.join(folder_path, filename)
        
        # 実際のデータの読み込みや処理
        tree = ET.parse(file_path)
        root = tree.getroot()

        if debug:
            print("reading:", file_path)

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
        
        total_alt_list.extend(alt_list)  # add altitude values of current file to the total list

    num_missing = num_rows * num_cols - len(total_alt_list)
    total_alt_list += [np.nan] * num_missing  # fill missing data with NaN

    alt = np.array(total_alt_list).reshape(num_rows, num_cols)

    return alt
