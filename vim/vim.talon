title: /vim/
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
  key(escape)
  key(super-p)

file toggle:
  user.vim_normal_mode("zi")

split next:
  key(escape)
  key(super-w)

split last:
  key(escape)
  key(ctrl-w)
  key(shift-w)

split new:
  user.vim_command_mode("vsp")

split close:
  user.vim_command_mode("q")

split next close:
  key(escape)
  key(super-w)
  insert(":q")
  key(enter)

split last close:
  key(escape)
  key(ctrl-w)
  key(shift-w)
  insert(":q")
  key(enter)

split close next:
  key(escape)
  insert(":q")
  key(enter)

split close last:
  key(escape)
  insert(":q")
  key(enter)
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
  key(escape)
  key(ctrl-r)

go way up:
  user.vim_normal_mode("gg")

go way down:
  key(escape)
  key(shift-g)
  
scroll down:
  key(escape)
  key(ctrl-d)

scroll up:
  key(escape)
  key(ctrl-u)

search <user.text>:
  key(escape)
  insert("/")
  user.insert_formatted(text, "SNAKE_CASE")
  key(enter)

search drop:
  user.vim_command_mode("noh")
  
search next:
  user.vim_normal_mode("n")

search last:
  key(escape)
  key(shift-n)

take <user.number_string> (line | lines):
  user.vim_select_lines(number_string)

take line:
  key(escape)
  insert("v")

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
