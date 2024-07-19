title: /\w*\.talon (.*) - VIM/
-

# Context headers end

(header | body):
  user.vim_insert_mode("-\n", "o")

# Code languages

code talon:
  user.vim_insert_mode("title: /\w*\.talon (.*) - VIM/")

code python:
  user.vim_insert_mode("title: /\w*\.py (.*) - VIM/")

code ruby:
  user.vim_insert_mode("title: /\w*\.rb (.*) - VIM/")

# Tags

user tag <user.text>:
  tag = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("tag: user.{tag}")
