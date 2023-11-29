from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = "title: /vim/"

@mod.action_class
class Actions:
    def vim_select_lines(number_string: str):
        """Select multiple lines"""

@ctx.action_class("user")
class VimActions:
    def vim_select_lines(number_string: str):
        """Select multiple lines"""
        number = int(number_string) - 1
        actions.key("escape")
        actions.insert("v{}j".format(number))
