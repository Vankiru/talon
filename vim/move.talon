title: /VIM/
-

# Up/down

up:
  user.vim_normal_mode("k")
  
down:
  user.vim_normal_mode("j")

<user.number_string> up:
  user.vim_normal_mode("{user.number_string}k")

<user.number_string> down:
  user.vim_normal_mode("{user.number_string}j")
  
# Begin/end

go way up:
  user.vim_normal_mode("gg")

go way down:
  user.vim_normal_mode_key("shift-g")
  
# Scroll

scroll down:
  user.vim_normal_mode_key("ctrl-d")

scroll up:
  user.vim_normal_mode_key("ctrl-u")

scroll middle:
  user.vim_normal_mode("zz")

scroll top:
  user.vim_normal_mode("zt")

scroll bottom:
  user.vim_normal_mode("zb")

