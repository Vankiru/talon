from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_method_with_name(text: str):
        name = actions.user.code_snake_case(text)
        actions.user.vim_insert_mode(f"def {name}\nend", "o")
        actions.insert("k$")

    def code_method():
        actions.user.vim_insert_mode("def \nend", "o")
        actions.insert("k$a")

    def code_short_method_with_name(text: str):
        name = actions.user.code_snake_case(text)
        actions.user.vim_insert_mode(f"def {name} = ", "o")

    def code_short_method():
        actions.user.vim_insert_mode("def  = ", "o")
        actions.insert("2hi")

    def code_method_return():
        actions.user.vim_insert_mode("return ", "o")

    def code_method_call(text: str):
        name = actions.user.code_snake_case(text)
        actions.user.vim_insert_mode(f".{name}", "a")

