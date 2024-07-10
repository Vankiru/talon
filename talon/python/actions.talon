title: /\w*\.py (.*) - VIM/
-

# Commands for defining actions

# Separate commands

talon import:
  user.vim_insert_mode("from talon import Context, Module, actions")

talon (module | model) import:
  user.vim_insert_mode("from talon import Module")

talon new (module | model):
  user.vim_insert_mode("mod = Module()", "o")

talon new context:
  user.vim_insert_mode("ctx = Context()", "o")

# Blocks

talon head:
  command = """from talon import Context, Module, actions

  mod = Module()
  ctx = Context()
  ctx.matches = "title: /VIM/"
  """

  user.vim_insert_mode(command)

talon (model | module) actions:
  command = """
  @mod.action_class
  class Actions:
      pass
  """

  user.vim_insert_mode(command)

talon actions <user.text>:
  class_name = user.formatted_text(text, "PRIVATE_CAMEL_CASE")

  command = """
  @ctx.action_class("user")
  class {class_name}Actions:
      pass
  """

  user.vim_insert_mode(command)

# File templates

talon tag file:
  command = """from talon import Module

  mod = Module()
  mod.tag("", desc="")

  @mod.action_class
  class Actions:
      pass
  """

  user.vim_insert_mode(command)

