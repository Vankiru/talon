from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_class_with_name(name: str):
        actions.user.vim_insert_mode(f"class {name}:", "o")
        actions.insert("h")

    def code_class():
        actions.user.vim_insert_mode("class :", "o")
        actions.insert("h")

    def code_superclass_with_name(name: str):
        actions.user.vim_insert_mode(f"({name})", "a")
        actions.insert("h")

    def code_superclass():
        actions.user.vim_insert_mode("()", "a")
        actions.insert("hi")

    def code_class_init():
        actions.user.vim_insert_mode("def __init__(self):", "o")
        actions.insert("2h")

    def code_class_private():
        actions.user.vim_insert_mode("private", "o")

    def code_class_protected():
        actions.user.vim_insert_mode("protected", "o")

    def code_class_public():
        actions.user.vim_insert_mode("public", "o")

    def code_class_new(name: str):
        actions.user.vim_insert_mode(f"{name}()", "a")

