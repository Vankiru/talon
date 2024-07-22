title: /\w*\.talon (.*) - VIM/
-

# Actions

user action <user.text>:
  method = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("user.{method}()", "o")

format snake <user.text>:
  variable = user.code_snake_case(text)
  command = '{variable} = user.code_snake_case(text)'

  user.vim_insert_mode(command, "o")

format scream <user.text>:
  variable = user.code_snake_case(text)
  command = '{variable} = user.code_screaming_case(text)'

  user.vim_insert_mode(command, "o")

format camel <user.text>:
  variable = user.code_snake_case(text)
  command = '{variable} = user.code_camel_case(text)'

  user.vim_insert_mode(command, "o")

