title: /\w*\.talon (.*) - VIM/
-

# Talon keys

talon escape:
  user.vim_insert_mode("key(escape)", "o")

talon (inter | enter):
  user.vim_insert_mode("key(enter)", "o")

talon key <user.letters>:
  user.vim_insert_mode("key({letters})", "o")

talon key <user.word>:
  user.vim_insert_mode("key({word})", "o")

talon key:
  user.vim_insert_mode("key()", "o")
  insert("i")

talon insert:
  user.vim_insert_mode("insert(\"\")", "o")
  insert("hi")
