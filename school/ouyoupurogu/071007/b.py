import numpy as np

def readDEM(mesh, debug=0):
    # メッシュ番号を使用して標高値と標高モデルを仮の値として生成する
    alt = np.random.rand(10, 10)  # 10x10のランダムな標高値配列
    idx = np.random.randint(0, 10, (10, 10))  # 10x10のランダムな標高モデル配列

    # 実際のデータの読み込みなどの処理をここに追加する

    if debug == 2:
        print("Debug Mode 2")

    return alt, idx
