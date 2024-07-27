from talon import Module

mod = Module()
mod.tag("code_controls", desc="Controls commands")

@mod.action_class
class Actions:
    def code_controls_if():
        """if"""

    def code_controls_else():
        """else"""

    def code_controls_else_if():
        """else if"""

    def code_controls_while():
        """while"""

    def code_controls_for(item: str, list: str):
        """for in"""
