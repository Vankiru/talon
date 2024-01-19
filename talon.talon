title: /vim/
-

# #######################
# Commands for .talon files

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

# #######################
# Commands for .py files

talon code escape:
  user.vim_insert_mode("actions.key(\"escape\")", "o")

talon code (inter | enter):
  user.vim_insert_mode("actions.key(\"enter\")", "o")

talon code key <user.letters>:
  user.vim_insert_mode("actions.key(\"{letters}\")", "o")

talon code key <user.word>:
  user.vim_insert_mode("actions.key(\"{word}\")", "o")

talon code key:
  user.vim_insert_mode("actions.key()", "o")
  insert("i")

talon code insert:
  user.vim_insert_mode("actions.insert(\"\")", "o")
  insert("hi")

# #######################
# Vim talon commands

vim normal <user.letters>:
  command = "user.vim_normal_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim normal:
  command = "user.vim_normal_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim key <user.letters>:
  command = "user.vim_normal_mode_key(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim key:
  command = "user.vim_normal_mode_key(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim insert <user.word>:
  command = "user.vim_insert_mode({word})"
  user.vim_insert_mode(command, "o")

vim insert:
  command = "user.vim_insert_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim visual <user.letters>:
  command = "user.vim_visual_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim visual:
  command = "user.vim_visual_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim vertical <user.letters>:
  command = "user.vim_visual_mode_vertical(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim vertical:
  command = "user.vim_visual_mode_vertical(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim (comment | command) <user.letters>:
  command = "user.vim_command_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim (comment | command):
  command = "user.vim_command_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")
