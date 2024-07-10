title: /VIM/
-

# Take

take line:
  user.vim_normal_mode("v")

take <user.number_string> (line | lines):
  user.vim_select_lines(number_string)

# Indent

indent line:
  user.vim_normal_mode("v")
  key(shift->)

indent <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  key(shift->)

# Dedent

dedent line:
  user.vim_normal_mode("v")
  key(shift-<)

dedent <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  key(shift-<)

# Comment

comment line:
  user.vim_normal_mode("v,ci")

comment <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  insert(",ci")

