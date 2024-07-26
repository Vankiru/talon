from talon import Module

mod = Module()
mod.tag("code_methods", desc="Methods commands")

@mod.action_class
class Actions:
    def code_method_with_name(name: str):
        """Method with name"""

    def code_method():
        """Method"""

    def code_short_method_with_name(name: str):
        """Short method with name"""

    def code_short_method():
        """Short method"""

    def code_method_return():
        """Return statement"""

    def code_method_call(name: str):
        """Method call"""
