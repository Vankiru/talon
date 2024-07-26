title: /\w*\.py (.*) - VIM/
-

tag(): user.code_classes

class (met | meth) <user.method_name>:
  user.vim_insert_mode("def {method_name}(self):", "o")
  insert("2h")
