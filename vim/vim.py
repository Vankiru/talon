from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = "title: /VIM/"

@mod.action_class
class Actions:
    def vim_normal_mode(command: str):
        """Execute in normal mode"""

    def vim_normal_mode_key(command: str):
        """Execute key combination in normal mode"""

    def vim_insert_mode(command: str, key: str = "i"):
        """Execute in insert mode"""

    def vim_visual_mode(command: str):
        """Execute in visual mode"""

    def vim_vertical_visual_mode(command: str):
        """Execute in vertical visual mode"""

    def vim_command_mode(command: str):
        """Execute in command mode"""

    def vim_select_lines(number_string: str):
        """Select multiple lines"""

@ctx.action_class("user")
class VimActions:
    def vim_normal_mode(command: str):
        """Execute in normal mode"""
        actions.key("escape")
        actions.insert(command)

    def vim_normal_mode_key(command: str):
        """Execute key combination in normal mode"""
        actions.key("escape")
        actions.key(command)

    def vim_insert_mode(command: str, key: str = "i"):
        """Execute in insert mode"""
        actions.key("escape")
        actions.key(key)
        actions.insert(command)
        actions.key("escape")

    def vim_visual_mode(command: str):
        """Execute in visual mode"""
        actions.key("escape")
        actions.insert(f"v{command}")

    def vim_vertical_visual_mode(command: str):
        """Execute in vertical visual mode"""
        actions.key("escape")
        actions.key(ctrl-v)
        actions.insert(command)

    def vim_command_mode(command: str):
        """Execute in command mode"""
        actions.key("escape")
        actions.insert(f":{command}")
        actions.key("enter")

    def vim_select_lines(number_string: str):
        """Select multiple lines"""
        number = int(number_string) - 1
        actions.key("escape")
        actions.insert(f"v{number}j")
