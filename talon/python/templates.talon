title: /.*\.py (.*) - VIM/
-

# File templates

talon vim file:
  command = """from talon import Context, Module, actions

  mod = Module()
  ctx = Context()
  ctx.matches = "title: /VIM/"

  @mod.action_class
  class Actions:
      pass

  @ctx.action_class("user")
  class VimActions:
      pass
  """

  user.vim_insert_mode(command)

talon ruby file:
  command = """from talon import Context, actions

  ctx = Context()
  ctx.matches = "title: /.*\.rb (.*) - VIM/"

  @ctx.action_class("user")
  class CodeActions:
      pass
  """

  user.vim_insert_mode(command)

talon python file:
  command = """from talon import Context, actions

  ctx = Context()
  ctx.matches = "title: /.*\.py (.*) - VIM/"

  @ctx.action_class("user")
  class CodeActions:
      pass
  """

  user.vim_insert_mode(command)

talon term file:
  command = """from talon import Context, actions

  ctx = Context()
  ctx.matches = "title: /zsh/"

  @ctx.action_class("user")
  class ConsoleActions:
      pass
  """

  user.vim_insert_mode(command)

talon tag file <user.text>:
  tag = user.code_snake_case(text)
  command = """from talon import Module

  mod = Module()
  mod.tag("{tag}", desc="")

  @mod.action_class
  class Actions:
      pass
  """

  user.vim_insert_mode(command)

