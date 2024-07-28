title: /.*\.py (.*) - VIM/
-

tag(): user.code_controls

for <user.variable_name> in range <user.number_string>:
  user.vim_insert_mode("for {variable_name} in range({number_string}):", "o")

leaf:
  user.vim_insert_mode(" if ", "o")

# TODO: rename
line for <user.variable_name> in range <user.number_string>:
  user.vim_insert_mode("for {variable_name} in range({number_string})", "o")

(match | much):
  user.vim_insert_mode("match :", "o")
  insert("h")

case:
  user.vim_insert_mode("case :", "o")
  insert("h")

case (else | blank):
  user.vim_insert_mode("case _:", "o")

break:
  user.vim_insert_mode("break", "o")

continue:
  user.vim_insert_mode("continue", "o")

pass:
  user.vim_insert_mode("pass", "o")
