title: /vim/
-

file save:
  key(escape)
  insert(": w")
  key(enter)

file close:
  key(escape)
  insert(":wq")
  key(enter)

file close bang:
  key(escape)
  insert(":q!")
  key(enter)
 
file open:
  key(escape)
  key(super-p)

file toggle:
  key(escape)
  insert("zi")

split next:
  key(escape)
  key(super-w)

split last:
  key(escape)
  key(ctrl-w)
  key(shift-w)

split new:
  key(escape)
  insert(":vsp")
  key(enter)

split close:
  key(escape)
  insert(": q")
  key(enter)

undo:
  key(escape)
  key(u)

redo:
  key(escape)
  key(ctrl-r)

go way up:
  key(escape)
  insert("gg")

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
  key(escape)
  insert(":noh")
  key(enter)
  
next:
  key(escape)
  key(n)

last:
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
  key(escape)
  insert("v")
  key(shift-<)

dedent <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  key(shift-<)

dedent line:
  key(escape)
  insert("v")
  key(shift-<)

comment (line | lines):
  insert("v,ci")

comment <user.number_string> (line | lines):
  user.vim_select_lines(number_string)
  insert(",ci")

go <user.number_string> down:
  insert("{number_string}j")

go <user.number_string> up:
  insert("{number_string}k")
