from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.capture('user.class_name', rule="<user.camel_name> ((pack | back) <user.camel_name>)*")
def class_name(m) -> str:
    names = list(
        filter(
            lambda n: n not in ["pack", "back"],
            list(m)
        )
    )

    return "::".join(names)

@ctx.action_class("user")
class CodeActions:
    def code_variable_name(name: str):
        actions.user.vim_insert_mode(f"{name}", "a")

    def code_instance_variable_name(name: str):
        actions.user.vim_insert_mode(f"@{name}", "a")

    def code_self_name(name: str):
        actions.user.vim_insert_mode(f"self.{name}", "a")

    def code_constant_name(name: str):
        actions.user.vim_insert_mode(f"{name}", "a")

    def code_class_name(name: str):
        actions.user.vim_insert_mode(f"{name}", "a")

