title: /\w*\.talon (.*) - VIM/
-

# Vim commands for .talon files

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

vim insert after <user.word>:
  command = 'user.vim_insert_mode({word}, "a")'
  user.vim_insert_mode(command, "o")

vim insert after:
  command = 'user.vim_insert_mode("", "a")'
  user.vim_insert_mode(command, "o")
  insert("6hi")

vim visual <user.letters>:
  command = "user.vim_visual_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim visual:
  command = "user.vim_visual_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim vertical <user.letters>:
  command = "user.vim_vertical_visual_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim vertical:
  command = "user.vim_vertical_visual_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim (comment | command) <user.letters>:
  command = "user.vim_command_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim (comment | command):
  command = "user.vim_command_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")
