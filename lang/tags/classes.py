from talon import Module

mod = Module()
mod.tag("code_classes", desc="Classes commands")

@mod.action_class
class Actions:
    def code_class():
        """Class"""

    def code_superclass():
        """Superclass"""

    def code_class_init():
        """Class initialize method"""

    def code_class_private():
        """Class private"""

    def code_class_protected():
        """Class protected"""

    def code_class_public():
        """Class public"""
