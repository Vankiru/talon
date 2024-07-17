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

