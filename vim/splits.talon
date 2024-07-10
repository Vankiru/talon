title: /VIM/
-

split next:
  user.vim_normal_mode_key("super-w")

split last:
  user.vim_normal_mode_key("ctrl-w")
  key(shift-w)

split new:
  user.vim_command_mode("vsp")

split close:
  user.vim_command_mode("q")

split next close:
  user.vim_normal_mode_key("super-w")
  user.vim_command_mode("q")

split last close:
  user.vim_normal_mode_key("ctrl-w")
  key(shift-w)
  user.vim_command_mode("q")

split close next:
  user.vim_command_mode("q")

split close last:
  user.vim_command_mode("q")
  key(ctrl-w)
  key(shift-w)

