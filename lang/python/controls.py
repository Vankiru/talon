from talon import Context, actions

ctx = Context()
ctx.matches = "title: /.*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_controls_if():
        actions.user.vim_insert_mode("if :", "o")
        actions.insert("h")

    def code_controls_else():
        actions.user.vim_insert_mode("else:", "o")

    def code_controls_else_if():
        actions.user.vim_insert_mode("elif :", "o")
        actions.insert("h")

    def code_controls_while():
        actions.user.vim_insert_mode("while :", "o")
        actions.insert("h")

    def code_controls_for(item: str, list: str):
        actions.user.vim_insert_mode(f"for {item} in {list}:", "o")


