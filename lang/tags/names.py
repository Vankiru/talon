from talon import Context, Module, actions

mod = Module()
ctx = Context()
mod.tag("code_names", desc="Names commands")

@mod.action_class
class Actions:
    def code_snake_case(text: str):
        """Snake case"""

    def code_screaming_case(text: str):
        """Screaming snake case"""

    def code_camel_case(text: str):
        """Camel case"""

    def code_variable_name(text: str):
        """Variable name"""

    def code_instance_variable_name(text: str):
        """Instance variable name"""

    def code_self_name(text: str):
        """Self name (self.name)"""

    def code_constant_name(text: str):
        """Constant name"""

    def code_class_name(text: str):
        """Class name"""

@ctx.action_class("user")
class CodeActions:
    def code_snake_case(text: str):
        return actions.user.formatted_text(text, "SNAKE_CASE")

    def code_screaming_case(text: str):
        return actions.user.formatted_text(text, "ALL_CAPS,SNAKE_CASE")

    def code_camel_case(text: str):
        return actions.user.formatted_text(text, "PUBLIC_CAMEL_CASE")

