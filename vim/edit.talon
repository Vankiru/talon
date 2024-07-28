title: /VIM/
-

in <user.text>:
  user.vim_insert_mode(text)

in space <user.text>:
  user.vim_insert_mode(" {text}")

below:
  insert("o ")
  key(backspace)
  key(escape)

above:
  insert("O ")
  key(backspace)
  key(escape)

(line | empty) (below | down):
  user.vim_normal_mode("o")
  key(escape)

(line | empty) (above | up):
  user.vim_normal_mode("O")
  key(escape)

capital:
  user.vim_normal_mode("vgU")

swap words:
  user.vim_normal_mode("dwea ")
  user.vim_normal_mode("px")

