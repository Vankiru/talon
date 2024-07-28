title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_classes

self class:
  user.vim_insert_mode("class << self\nend", "o")
  insert("k$")
