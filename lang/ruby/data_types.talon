title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_data_types


# document string

doc string <user.text>:
  user.vim_insert_mode("<<~DOC\n{text}\nDOC", "a")

doc string:
  user.vim_insert_mode("<<~DOC\nDOC", "a")
  key("O")

# symbol

sim <user.text>:
  user.vim_insert_mode(":{text}", "a")

sim:
  user.vim_insert_mode(":", "a")
  key("i")

# array

string list:
  user.vim_insert_mode("%w[]", "a")

sim list:
  user.vim_insert_mode("%i[]", "a")

# key => value

string key <user.text> [to]:
  name = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode('"{name}": ', "a")

object key <user.text> [to]:
  name = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("{name} => ", "a")

# range

range <user.number_string> (to | by) <user.number_string>:
  user.vim_insert_mode("({number_string_1}..{number_string_2})", "a")

range <user.number_string> until <user.number_string>:
  user.vim_insert_mode("({number_string_1}...{number_string_2})", "a")

range <user.number_string>:
  user.vim_insert_mode("({number_string}..)", "a")

range (to | by) <user.number_string>:
  user.vim_insert_mode("(..{number_string})", "a")

range until <user.number_string>:
  user.vim_insert_mode("(...{number_string})", "a")

object range <user.number_string> (to | by) <user.number_string>:
  user.vim_insert_mode("Range.new({number_string_1}, {number_string_2})", "a")

object range <user.number_string> until <user.number_string>:
  user.vim_insert_mode("Range.new({number_string_1}, {number_string_2}, true)", "a")

# regexp

rig <user.text>:
  user.vim_insert_mode("/{text}/", "a")

rig:
  user.vim_insert_mode("//", "a")
  key("i")

# lambda

lambda:
  user.vim_insert_mode("-> { }", "a")
  key("h")
