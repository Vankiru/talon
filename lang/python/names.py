from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_variable_name(name: str):
        actions.user.vim_insert_mode(f"{name}", "a")

    def code_instance_variable_name(name: str):
        actions.user.vim_insert_mode(f"_{name}", "a")

    def code_self_name(name: str):
        actions.user.vim_insert_mode(f"self.{name}", "a")

    def code_constant_name(name: str):
        actions.user.vim_insert_mode(f"{name}", "a")

    def code_class_name(name: str):
        actions.user.vim_insert_mode(f"{name}", "a")

