title: /\w*\.py (.*) - VIM/
-

# Vim commands for .py files

vim normal <user.letters>:
  command = "actions.user.vim_normal_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim normal:
  command = "actions.user.vim_normal_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim key <user.letters>:
  command = "actions.user.vim_normal_mode_key(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim key:
  command = "actions.user.vim_normal_mode_key(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim insert:
  command = "actions.user.vim_insert_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim insert after:
  command = 'actions.user.vim_insert_mode("", "a")'
  user.vim_insert_mode(command, "o")
  insert("6hi")

vim insert below:
  command = 'actions.user.vim_insert_mode("", "o")'
  user.vim_insert_mode(command, "o")
  insert("6hi")

vim insert above:
  command = 'actions.user.vim_insert_mode("", "O")'
  user.vim_insert_mode(command, "o")
  insert("6hi")

vim visual <user.letters>:
  command = "actions.user.vim_visual_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim visual:
  command = "actions.user.vim_visual_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim vertical <user.letters>:
  command = "actions.user.vim_vertical_visual_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim vertical:
  command = "actions.user.vim_vertical_visual_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

vim (comment | command) <user.letters>:
  command = "actions.user.vim_command_mode(\"{letters}\")"
  user.vim_insert_mode(command, "o")

vim (comment | command):
  command = "actions.user.vim_command_mode(\"\")"
  user.vim_insert_mode(command, "o")
  insert("hi")

