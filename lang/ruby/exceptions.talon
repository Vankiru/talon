title: /.*\.rb (.*) - VIM/
-

tag(): user.code_exceptions

begin:
  user.vim_insert_mode("begin\nend", "o")
  insert("k$")

rescue:
  user.vim_insert_mode("rescue", "o")

rescue <user.class_name>:
  user.vim_insert_mode("rescue {class_name}", "o")

rescue as <user.variable_name>:
  user.vim_insert_mode("rescue => {variable_name}", "o")

rescue <user.class_name> as <user.variable_name>:
  user.vim_insert_mode("rescue {class_name} => {variable_name}", "o")

(ensure | insure):
  user.vim_insert_mode("ensure", "o")

retry:
  user.vim_insert_mode("retry", "o")

(raise | rise):
  user.vim_insert_mode("raise ", "o")
