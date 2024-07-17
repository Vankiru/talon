title: /\w*\.talon (.*) - VIM/
-

# Rules

rule <user.text>:
  user.vim_insert_mode("{text}:", "o")

user call <user.text>:
  method = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("user.{method}()", "o")

