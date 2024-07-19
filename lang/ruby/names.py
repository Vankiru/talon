from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_variable_name(text: str):
        name = actions.user.code_snake_case(text)
        actions.user.vim_insert_mode(f"{name}", "a")

    def code_instance_variable_name(text: str):
        name = actions.user.code_snake_case(text)
        actions.user.vim_insert_mode(f"@{name}", "a")

    def code_self_name(text: str):
        name = actions.user.code_snake_case(text)
        actions.user.vim_insert_mode(f"self.{name}", "a")

    def code_constant_name(text: str):
        name = actions.user.code_screaming_case(text)
        actions.user.vim_insert_mode(f"{name}", "a")

    def code_class_name(text: str):
        name = actions.user.code_camel_case(text)
        actions.user.vim_insert_mode(f"{name}", "a")

