title: /\w*\.talon (.*) - VIM/
-

# Tags

body tag <user.text>:
  tag = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("tag(): user.{tag}")

# Rules

rule <user.text>:
  user.vim_insert_mode("{text}:", "o")
