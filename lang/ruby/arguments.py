from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_arguments_default(name: str):
        actions.user.vim_insert_mode(f"{name} = ", "a")

    def code_arguments_default_sign():
        actions.user.vim_insert_mode(f" = ", "a")

