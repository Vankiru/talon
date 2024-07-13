title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_data_types

doc string <user.text>:
  user.vim_insert_mode("<<~DOC\n{text}\nDOC", "a")

doc string:
  user.vim_insert_mode("<<~DOC\nDOC", "a")
  insert("O")

(sim | seem) <user.text>:
  user.vim_insert_mode(":{text}", "a")

(sim | seem):
  user.vim_insert_mode(":", "a")
  insert("i")

string list:
  user.vim_insert_mode("%w[]", "a")

(sim | seem) list:
  user.vim_insert_mode("%i[]", "a")

string key <user.text> [to]:
  name = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode('"{name}": ', "a")

object key <user.text> [to]:
  name = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("{name} => ", "a")
