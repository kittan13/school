l = ["Mon","tue","Wed","Thu","Fri","sat","Sun"]

def change_words(words,func):
    for word in words:
        print(func(word))

#def sample_func(word):
#    return word.capitalize()


sample_func = lambda word: word.capitalize()

#change_words(l,sample_func )

change_words(l,lambda word:word.capitalize())
change_words(l,lambda word:word.lower())


"""
chage_wordsにlとsample_funcが引数として入る。
change_wordsが実行される。
    1個めは"Mon"は入力される。
    printでfuncがよびだされる。
    ここでfuncはsample_funcなので、sample_funcが実行される。
        sample_funcには引数wordが入る。
        今、wordには"Mon"が入っている。
        returnで大文字変換された"Mon"がはいる。

それを繰り返す。
"""