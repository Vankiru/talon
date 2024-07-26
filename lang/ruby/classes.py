from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_class():
        actions.user.vim_insert_mode("class \nend", "o")
        actions.insert("k$")

    def code_superclass():
        actions.user.vim_insert_mode(" < ", "a")

    def code_class_init():
        actions.user.vim_insert_mode("def initialize\nend", "o")
        actions.insert("k$")

    def code_class_private():
        actions.user.vim_insert_mode("private", "o")

    def code_class_protected():
        actions.user.vim_insert_mode("protected", "o")

    def code_class_public():
        actions.user.vim_insert_mode("public", "o")

