tag: user.code_arguments
-

arts:
  user.vim_insert_mode("()", "a")

left art:
  user.vim_insert_mode("(", "a")

right art:
  user.vim_insert_mode(")", "a")

(comma | coma):
  user.vim_insert_mode(", ", "a")

line (comma | coma):
  user.vim_insert_mode(",\n", "a")

default <user.text> [to]:
  user.code_arguments_default(text)

default to:
  user.code_arguments_default_sign()

list art <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("*{variable}", "a")

list art:
  user.vim_insert_mode("*", "a")

hash art <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("**{variable}", "a")

hash art:
  user.vim_insert_mode("**", "a")
