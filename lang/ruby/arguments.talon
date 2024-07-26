title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_arguments

key art <user.variable_name>:
  user.vim_insert_mode("{variable_name}:", "a")

key art:
  user.vim_insert_mode(":", "a")

block art <user.variable_name>:
  user.vim_insert_mode("&{variable_name}", "a")

block art:
  user.vim_insert_mode("&", "a")

forward art:
  user.vim_insert_mode("...", "a")

barbs:
  user.vim_insert_mode(" ||", "a")
  insert("h")
