title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_arguments

key art <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("{variable}:", "a")

key art:
  user.vim_insert_mode(":", "a")

block art <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("&{variable}", "a")

block art:
  user.vim_insert_mode("&", "a")

forward art:
  user.vim_insert_mode("...", "a")
