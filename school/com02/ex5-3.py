#ボタンクリックイベント
def btn_click():
    gold = float(entry.get())
    if gold >= 5000 and gold < 10000:
        canvas.delete("illust")
        canvas.create_image(320, 220, image=img2, tag="illust")
        serihu_text["text"] ="勇者「よーし、私に任せなさい！」"
    else:
        serihu_text["text"] = "志願者は誰も来ませんでした。"
    sys_text.destroy()
    button["state"] = "disabled"
    entry["state"] = "disabled"