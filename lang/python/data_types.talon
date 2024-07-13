title: /\w*\.py (.*) - VIM/
-

tag(): user.code_data_types

format string <user.text>:
  user.vim_insert_mode('f"{text}"', "a")

format string:
  user.vim_insert_mode('f""', "a")
  insert("i")

tuple:
  user.vim_insert_mode("()", "a")

multi tuple:
  user.vim_insert_mode("(\n)", "a")

object tuple:
  user.vim_insert_mode("tuple()", "a")
