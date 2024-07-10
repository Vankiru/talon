title: /VIM/
-

file save:
  user.vim_command_mode("w")

file close:
  user.vim_command_mode("wq")

file force close:
  user.vim_command_mode("q!")
 
file open:
  user.vim_normal_mode_key("ctrl-p")

file toggle:
  user.vim_normal_mode("zi")

