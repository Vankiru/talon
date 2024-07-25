from talon import Module

mod = Module()
mod.tag("code_methods", desc="Methods commands")

@mod.action_class
class Actions:
    def code_method_with_name(text: str):
        """Method"""

    def code_method():
        """Method"""

    def code_short_method_with_name(text: str):
        """Method"""

    def code_short_method():
        """Method"""

    def code_method_return():
        """Method"""

    def code_method_call(text: str):
        """Method"""
