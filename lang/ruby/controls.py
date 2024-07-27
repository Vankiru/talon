from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_controls_if():
        actions.user.vim_insert_mode("if \nend", "o")
        actions.insert("k$")

    def code_controls_else():
        actions.user.vim_insert_mode("else", "o")

    def code_controls_else_if():
        actions.user.vim_insert_mode("elsif ", "o")

    def code_controls_while():
        actions.user.vim_insert_mode("while  do\nend", "o")
        actions.insert("k^el")

    def code_controls_for(item: str, list: str):
        actions.user.vim_insert_mode(f"for {item} in {list}\nend", "o")

