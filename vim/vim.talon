title: /VIM/
-

drop:
  key(escape)

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

swap words:
  user.vim_normal_mode("dwea ")
  user.vim_normal_mode("px")

(tree | three) open:
  user.vim_command_mode("NERDTree")

undo:
  user.vim_normal_mode("u")

redo:
  user.vim_normal_mode_key("ctrl-r")

go way up:
  user.vim_normal_mode("gg")

go way down:
  user.vim_normal_mode_key("shift-g")
  
scroll down:
  user.vim_normal_mode_key("ctrl-d")

scroll up:
  user.vim_normal_mode_key("ctrl-u")

search <user.text>:
  text = user.formatted_text(text, "SNAKE_CASE")
  user.vim_normal_mode("/{text}")
  key(enter)

search drop:
  user.vim_command_mode("noh")
  
search next:
  user.vim_normal_mode("n")

search last:
  user.vim_normal_mode_key("shift-n")

take <user.number_string> (line | lines):
  user.vim_select_lines(number_string)

take line:
  user.vim_normal_mode("v")

indent <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  key(shift->)

indent line:
  user.vim_normal_mode("v")
  key(shift->)

dedent <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  key(shift-<)

dedent line:
  user.vim_normal_mode("v")
  key(shift-<)

comment (line | lines):
  user.vim_normal_mode("v,ci")

comment <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  insert(",ci")

scroll middle:
  user.vim_normal_mode("zz")

scroll top:
  user.vim_normal_mode("zt")

scroll bottom:
  user.vim_normal_mode("zb")

capital:
  user.vim_normal_mode("vgU")

<user.number_string> up:
  user.vim_normal_mode("{user.number_string}k")

<user.number_string> down:
  user.vim_normal_mode("{user.number_string}j")
  
up:
  user.vim_normal_mode("k")
  
down:
  user.vim_normal_mode("j")
