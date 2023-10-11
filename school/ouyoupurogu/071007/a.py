import xml.etree.ElementTree as ET

def readDEM(mesh, debug=False):
    file_path = f"FG-GML-{mesh}-DEM5A"  # ファイルパスを作成する（例としてファイル名を指定）

    # 実際のデータの読み込みや処理
    # ここでは、XMLファイルのルート要素のタグ名を表示しています
    tree = ET.parse(file_path)
    root = tree.getroot()
    tag_name = root.tag

    if debug:
        print("Debug Mode")

    return tag_name
