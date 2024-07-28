title: /\w*\.talon (.*) - VIM/
-

# Code languages

code talon:
  user.vim_insert_mode("title: /.*\.talon (.*) - VIM/")

code python:
  user.vim_insert_mode("title: /.*\.py (.*) - VIM/")

code ruby:
  user.vim_insert_mode("title: /.*\.rb (.*) - VIM/")

# Tags

context tag <user.text>:
  tag = user.formatted_text(text, "SNAKE_CASE")
  user.vim_insert_mode("tag: user.{tag}")

# Context headers end

(header | body):
  user.vim_insert_mode("-\n", "o")

