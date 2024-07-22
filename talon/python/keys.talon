title: /\w*\.py (.*) - VIM/
-

# Keys commands

talon escape:
  user.vim_insert_mode("actions.key(\"escape\")", "o")

talon (inter | enter):
  user.vim_insert_mode("actions.key(\"enter\")", "o")

talon key <user.letters>:
  user.vim_insert_mode("actions.key(\"{letters}\")", "o")

talon key <user.word>:
  user.vim_insert_mode("actions.key(\"{word}\")", "o")

talon key:
  user.vim_insert_mode("actions.key()", "o")
  insert("i")

talon insert:
  user.vim_insert_mode("actions.insert(\"\")", "o")
  insert("hi")
