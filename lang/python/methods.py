from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_method_with_name(name: str):
        actions.user.vim_insert_mode(f"def {name}():", "o")

    def code_method():
        actions.user.vim_insert_mode("def ():", "o")
        actions.insert("2hi")

    def code_short_method_with_name(name: str):
        actions.user.vim_insert_mode(f"def {name}(): ", "o")

    def code_short_method():
        actions.user.vim_insert_mode("def (): ", "o")
        actions.insert("3hi")

    def code_method_return():
        actions.user.vim_insert_mode("return ", "o")

    def code_method_call(name: str):
        actions.user.vim_insert_mode(f".{name}", "a")
