tag: user.code_arguments
-

arts:
  user.vim_insert_mode("()", "a")
  insert("h")

left art:
  user.vim_insert_mode("(", "a")

right art:
  user.vim_insert_mode(")", "a")

(comma | coma):
  user.vim_insert_mode(", ", "a")

line (comma | coma):
  user.vim_insert_mode(",\n", "a")

default <user.variable_name> [to]:
  user.code_arguments_default(variable_name)

default to:
  user.code_arguments_default_sign()

list art <user.variable_name>:
  user.vim_insert_mode("*{variable_name}", "a")

list art:
  user.vim_insert_mode("*", "a")

hash art <user.variable_name>:
  user.vim_insert_mode("**{variable_name}", "a")

hash art:
  user.vim_insert_mode("**", "a")
