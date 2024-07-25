title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_methods

parent:
  user.vim_insert_mode("super ", "o")

yield:
  user.vim_insert_mode("yield ", "o")

yield self:
  user.vim_insert_mode("yield self", "o")

(safe | save) (call | cold) <user.text>:
  name = user.code_snake_case(text)
  user.vim_insert_mode("&.{name}", "a")

(safe | save) (call | cold):
  user.vim_insert_mode("&.", "a")
  insert("a")

block:
  user.vim_insert_mode(" do\nend", "a")
  insert("k$")

line block:
  user.vim_insert_mode(" { }", "a")
  insert("2h")
