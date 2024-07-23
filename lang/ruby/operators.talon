title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_operators

compare:
  user.vim_insert_mode(" <=> ", "a")

test equal:
  user.vim_insert_mode(" === ", "a")

text (add | also | and):
  user.vim_insert_mode(" and ", "a")

text (or | either):
  user.vim_insert_mode(" or ", "a")

text not:
  user.vim_insert_mode(" not ", "a")

inside:
  user.vim_insert_mode(" in ", "a")

match:
  user.vim_insert_mode(" => ", "a")
