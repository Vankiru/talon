title: /.*\.py (.*) - VIM/
-

# Talon Lists

talon put list <user.text>:
  name = user.code_snake_case(text)
  command = 'mod.list("{name}", desc="")'

  user.vim_insert_mode(command)

talon list <user.text>:
  name = user.code_snake_case(text)
  command = """ctx.lists["user.{name}"] = {
  }"""

  user.vim_insert_mode(command)
