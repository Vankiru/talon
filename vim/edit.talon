title: /VIM/
-

in <user.text>:
  user.vim_insert_mode(text)

in space <user.text>:
  user.vim_insert_mode(" {text}")

line below:
  user.vim_normal_mode("o")
  key(escape)

line above:
  user.vim_normal_mode("O")
  key(escape)

capital:
  user.vim_normal_mode("vgU")

swap words:
  user.vim_normal_mode("dwea ")
  user.vim_normal_mode("px")

