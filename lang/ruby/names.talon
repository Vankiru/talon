title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_names

(class | type) instance <user.text>:
  name = user.code_snake_case(text)
  user.vim_insert_mode("@@{name}", "a")

pack <user.text>:
  name = user.code_camel_case(text)
  user.vim_insert_mode("::{name}", "a")

global <user.text>:
  name = user.code_snake_case(text)
  user.vim_insert_mode("${name}", "a")
