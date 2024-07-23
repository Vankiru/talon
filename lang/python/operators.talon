title: /\w*\.py (.*) - VIM/
-

tag(): user.code_operators

floor divide:
  user.vim_insert_mode(" // ", "a")

floor divide equal:
  user.vim_insert_mode(" //= ", "a")

bit and equal:
  user.vim_insert_mode(" &= ", "a")

bit or equal:
  user.vim_insert_mode(" |= ", "a")

bit ex equal:
  user.vim_insert_mode(" ^= ", "a")

bit left equal:
  user.vim_insert_mode(" <<= ", "a")

bit right equal:
  user.vim_insert_mode(" >>= ", "a")

is:
  user.vim_insert_mode(" is ", "a")

is not:
  user.vim_insert_mode(" is not ", "a")

inside:
  user.vim_insert_mode(" in ", "a")

not (in | inside):
  user.vim_insert_mode(" not in ", "a")
