title: /\w*\.rb (.*) - VIM/
-

block:
  user.vim_insert_mode(" do\nend", "a")
  insert("k$")

line block:
  user.vim_insert_mode(" {  }", "a")
  insert("3h")
