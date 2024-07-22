from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_arguments_default(text: str):
        variable = actions.user.formatted_text(text, "SNAKE_CASE")
        actions.user.vim_insert_mode(f"{variable}=", "a")

    def code_arguments_default_sign():
        actions.user.vim_insert_mode(f"=", "a")

