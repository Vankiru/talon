from talon import Context, Module, actions

mod = Module()
ctx = Context()
mod.tag("code_names", desc="Names commands")

# Case captures

@mod.capture(rule="<user.text>")
def snake_name(m) -> str:
    return actions.user.code_snake_case(m.text)

@mod.capture(rule="<user.text>")
def screaming_name(m) -> str:
    return actions.user.code_screaming_case(m.text)

@mod.capture(rule="<user.text>")
def camel_name(m) -> str:
    return actions.user.code_camel_case(m.text)

# Names captures

@mod.capture(rule="<user.snake_name>")
def key_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.snake_name>")
def variable_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.snake_name>")
def method_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.screaming_name>")
def const_name(m) -> str:
    return m.screaming_name

@mod.capture(rule="<user.camel_name>")
def class_name(m) -> str:
    return m.camel_name

@mod.capture(rule="<user.snake_name>")
def file_name(m) -> str:
    return m.snake_name

@mod.capture(rule="<user.file_name> (slash <user.file_name>)")
def file_path(m) -> str:
    names = list(
        filter(
            lambda n: n != "slash",
            list(m)
        )
    )

    return "/".join(names)

@mod.action_class
class Actions:
    def code_snake_case(text: str):
        """Snake case"""

    def code_screaming_case(text: str):
        """Screaming snake case"""

    def code_camel_case(text: str):
        """Camel case"""

    def code_variable_name(name: str):
        """Variable name"""

    def code_instance_variable_name(name: str):
        """Instance variable name"""

    def code_self_name(name: str):
        """Self name (self.name)"""

    def code_constant_name(name: str):
        """Constant name"""

    def code_class_name(name: str):
        """Class name"""

@ctx.action_class("user")
class CodeActions:
    def code_snake_case(text: str):
        return actions.user.formatted_text(text, "SNAKE_CASE")

    def code_screaming_case(text: str):
        return actions.user.formatted_text(text, "ALL_CAPS,SNAKE_CASE")

    def code_camel_case(text: str):
        return actions.user.formatted_text(text, "PUBLIC_CAMEL_CASE")

