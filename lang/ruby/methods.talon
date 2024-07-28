title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_methods

met (is | if) <user.method_name>:
  user.vim_insert_mode("def {method_name}?\nend", "o")
  insert("k$")

met bank <user.method_name>:
  user.vim_insert_mode("def {method_name}!\nend", "o")
  insert("k$")

parent:
  user.vim_insert_mode("super ", "o")

yield:
  user.vim_insert_mode("yield ", "o")

yield self:
  user.vim_insert_mode("yield self", "o")

(safe | save) (call | cold) <user.method_name>:
  user.vim_insert_mode("&.{method_name}", "a")

(safe | save) (call | cold):
  user.vim_insert_mode("&.", "a")
  insert("a")

call (is | if) <user.method_name>:
  user.vim_insert_mode(".{method_name}?", "a")

call bank <user.method_name>:
  user.vim_insert_mode(".{method_name}!", "a")

block:
  user.vim_insert_mode(" do\nend", "a")
  insert("k$")

line block:
  user.vim_insert_mode(" { }", "a")
  insert("2h")
