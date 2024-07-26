from talon import Module

mod = Module()
mod.tag("code_arguments", desc="Arguments commands")

@mod.action_class
class Actions:
    def code_arguments_default(name: str):
        """Default argument"""

    def code_arguments_default_sign():
        """Default argument sign"""
