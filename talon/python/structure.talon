title: /\w*\.py (.*) - VIM/
-

# Import commands

talon import:
  user.vim_insert_mode("from talon import Context, Module, actions")

talon import (module | model):
  user.vim_insert_mode("from talon import Module")

talon import context:
  user.vim_insert_mode("from talon import Context, actions")

# Module & Context

talon new (module | model):
  user.vim_insert_mode("mod = Module()", "o")

talon new context:
  user.vim_insert_mode("ctx = Context()", "o")

talon context match:
  user.vim_insert_mode('ctx.matches = ""', "o")
  insert("i")

talon context vim:
  user.vim_insert_mode('ctx.matches = "title: /VIM/"', "o")
  insert("i")

talon context ruby:
  user.vim_insert_mode('ctx.matches = "title: /\w*\.rb (.*) - VIM/"', "o")
  insert("i")

talon context python:
  user.vim_insert_mode('ctx.matches = "title: /\w*\.py (.*) - VIM/"', "o")
  insert("i")

# Actions

talon (module | model) actions:
  command = """
  @mod.action_class
  class Actions:
      pass
  """

  user.vim_insert_mode(command)

talon <user.text> actions:
  class_name = user.formatted_text(text, "PRIVATE_CAMEL_CASE")

  command = """
  @ctx.action_class("user")
  class {class_name}Actions:
      pass
  """

  user.vim_insert_mode(command)
