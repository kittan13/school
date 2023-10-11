import matplotlib.font_manager as fm

# インストールされているフォント一覧を表示
font_list = fm.findSystemFonts()
for font in font_list:
    print(font)

# 使用するフォントを指定
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # フォントファイルのパスを指定
font_prop = fm.FontProperties(fname=font_path)
