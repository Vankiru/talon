title: /\w*\.rb (.*) - VIM/
-

(module | model) <user.class_name>:
  user.vim_insert_mode("module {class_name}\nend", "o")
  insert("k$")

(module | model):
  user.vim_insert_mode("module \nend", "o")
  insert("k$")

refine <user.class_name>:
  user.vim_insert_mode("refine {class_name}\nend", "o")
  insert("k$")

refine:
  user.vim_insert_mode("refine \nend", "o")
  insert("k$")

include <user.class_name>:
  user.vim_insert_mode("include {class_name}", "o")

include:
  user.vim_insert_mode("include ", "o")

extend <user.class_name>:
  user.vim_insert_mode("extend {class_name}", "o")

extend:
  user.vim_insert_mode("extend ", "o")

using <user.class_name>:
  user.vim_insert_mode("using {class_name}", "o")

using:
  user.vim_insert_mode("using ", "o")
