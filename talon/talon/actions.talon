title: /\w*\.talon (.*) - VIM/
-

# Actions

format snake <user.text>:
  variable = user.formatted_text(text, "SNAKE_CASE")
  command = '{variable} = user.formatted_text(text, "SNAKE_CASE")'

  user.vim_insert_mode(command, "o")

user action <user.text>:
  method = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("user.{method}()", "o")

