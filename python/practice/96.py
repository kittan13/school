##########################################
####          テンプレート作成       #####
##########################################

#文章を考えるときにテンプレートで外枠を作っておいて、中に変数として外から入れ込むことができるようにする。

#まず import string 
import string

#ドルマークで指定したところが変数として外から入れ込むことができる。
s ="""\
Hi $name

$contents

Hane good day
"""

#テンプレートにすることで、テンプレ部分は変更されない。
t = string.Template(s)
contents = t.substitute(name = "Mike", contents ="How are you?")
print(contents)
