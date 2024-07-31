title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_methods

(met bank) | mukbang <user.method_name>:
  user.vim_insert_mode("def {method_name}!\nend", "o")
  insert("k$")

met plight <user.method_name>:
  user.vim_insert_mode("def {method_name}?\nend", "o")
  insert("k$")

(safe | save) (call | cold) <user.method_name>:
  user.vim_insert_mode("&.{method_name}", "a")

(safe | save) (call | cold):
  user.vim_insert_mode("&.", "a")
  insert("a")

(call | cold) (bang | bank) <user.method_name>:
  user.vim_insert_mode(".{method_name}!", "a")

(call | cold) plight <user.method_name>:
  user.vim_insert_mode(".{method_name}?", "a")

parent:
  user.vim_insert_mode("super ", "o")

yield:
  user.vim_insert_mode("yield ", "o")

yield self:
  user.vim_insert_mode("yield self", "o")

